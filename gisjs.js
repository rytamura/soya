<!--    
    <script type="text/javascript">
    function map_init_default (map, options) {
      Lfeatures = makeFeatureLayer("{% url 'features' %}");
      Lsections1920 = makeSectionLayer("{% url 'sections' 1920 1950 %}");
      Lsections1950 = makeSectionLayer("{% url 'sections' 1951 1970 %}");
      Lsections1995 = makeSectionLayer("{% url 'sections' 1971 1990 %}");
      Lsections2017 = makeSectionLayer("{% url 'sections' 1991 2017 %}");

      Lstations1920 = makeStationLayer("{% url 'stations' 1920 1950 %}");
      Lstations1950 = makeStationLayer("{% url 'stations' 1951 1970 %}");
      Lstations1995 = makeStationLayer("{% url 'stations' 1971 1990 %}");
      Lstations2017 = makeStationLayer("{% url 'stations' 1991 2017 %}");

      LsectionsBase = makeSectionLayer("{% url 'sections' 1920 2017 %}");
      LstationsBase = makeStationLayer("{% url 'stations' 1920 2017 %}");

      Ladm1920  = makeAdmLayer("{% url 'adm1920' %}", 1920, "1920");
      Ladm1950  = makeAdmLayer("{% url 'adm1950' %}", 1950, "1950");
      Ladm1995  = makeAdmLayer("{% url 'adm1995' %}", 1995, "1995");
      Ladm2017  = makeAdmLayer("{% url 'adm2017' %}", 2017, "2017");

      g2017 = L.layerGroup([Lsections2017]);
      g1995 = L.layerGroup([Lsections1995]);
      g1950 = L.layerGroup([Lsections1950]);
      g1920 = L.layerGroup([Lsections1920]);

      var baseL = {
        '1991年〜現在': g2017,
        '1971〜1990年': g1995,
        '1951〜1970年': g1950,
        '1950年以前': g1920
      }

      cntl = L.control.layers(baseL,null,{collapsed:false});

      cntl.addTo(map);

      Lfeatures.addTo(map);

      gdefault = L.layerGroup([LsectionsBase]);
      gdefault.addTo(map);

      map.on('baselayerchange', function(e) {
        // if at least one layer change occured,
        // we discard the gdefault layer!
        if (map.hasLayer(gdefault)) {
          map.removeLayer(gdefault);
        }
        // console.log(e.name);
        // console.log(map.getZoom());

        if (map.getZoom()>=10){
          switch(e.name) {
            case '1950年以前':
              if (!g1920.hasLayer(Ladm1920))      g1920.addLayer(Ladm1920);
              if (!g1920.hasLayer(Lstations1920)) g1920.addLayer(Lstations1920);
              Ladm1920.bringToBack();
              break;
            case '1951〜1970年':
              if (!g1950.hasLayer(Ladm1950))      g1950.addLayer(Ladm1950);
              if (!g1950.hasLayer(Lstations1950)) g1950.addLayer(Lstations1950);
              break;
            case '1971〜1990年':
              if (!g1995.hasLayer(Ladm1995))      g1995.addLayer(Ladm1995);
              if (!g1995.hasLayer(Lstations1995)) g1995.addLayer(Lstations1995);
              break;
            case '1990年〜現在':
              if (!g2017.hasLayer(Ladm2017))      g2017.addLayer(Ladm2017);
              if (!g2017.hasLayer(Lstations2017)) g2017.addLayer(Lstations2017);
              break;
            default:
              console.log("SOYALAB ERROR: UNKNOWN PERIOD SELECTED!!!: " + e.name);
              // do nothing
          }
        }
        else {
          switch(e.name) {
            case '1950年以前':
              g1920.removeLayer(Ladm1920);
              g1920.removeLayer(Lstations1920);
              break;
            case '1951〜1970年':
              g1950.removeLayer(Ladm1950);
              g1950.removeLayer(Lstations1950);
              break;
            case '1971〜1990年':
              g1995.removeLayer(Ladm1995);
              g1995.removeLayer(Lstations1995);
              break;
            case '1990年〜現在':
              g2017.removeLayer(Ladm2017);
              g2017.removeLayer(Lstations2017);
              break;
            default:
              console.log("SOYALAB ERROR: UNKNOWN PERIOD SELECTED!!!: " + e.name);
              // do nothing
          }
        }
      })

      map.on('zoomend', function(){
        if (map.getZoom()>=10){
          console.log(map.getZoom());

          if (map.hasLayer(gdefault)) gdefault.addLayer(LstationsBase);

          if (map.hasLayer(g1920)){
            if (!g1920.hasLayer(Ladm1920))      g1920.addLayer(Ladm1920);
            if (!g1920.hasLayer(Lstations1920)) g1920.addLayer(Lstations1920);
          }
          if (map.hasLayer(g1950)){
            if (!g1920.hasLayer(Ladm1950))      g1950.addLayer(Ladm1950);
            if (!g1920.hasLayer(Lstations1950)) g1950.addLayer(Lstations1950);
          }
          if (map.hasLayer(g1995)){
            if (!g1920.hasLayer(Ladm1995))      g1995.addLayer(Ladm1995);
            if (!g1920.hasLayer(Lstations1995)) g1995.addLayer(Lstations1995);
          }
          if (map.hasLayer(g2017)){
            if (!g1920.hasLayer(Ladm2017))      g2017.addLayer(Ladm2017);
            if (!g1920.hasLayer(Lstations2017)) g2017.addLayer(Lstations2017);
          }
        }
        else {
          if (map.hasLayer(gdefault)) gdefault.removeLayer(LstationsBase);

          if (map.hasLayer(g1920)){
            if (g1920.hasLayer(Ladm1920))      g1920.removeLayer(Ladm1920);
            if (g1920.hasLayer(Lstations1920)) g1920.removeLayer(Lstations1920);
          }
          if (map.hasLayer(g1950)){
            if (g1950.hasLayer(Ladm1950))      g1950.removeLayer(Ladm1950);
            if (g1950.hasLayer(Lstations1950)) g1950.removeLayer(Lstations1950);
          }
          if (map.hasLayer(g1995)){
            if (g1995.hasLayer(Ladm1995))      g1995.removeLayer(Ladm1995);
            if (g1995.hasLayer(Lstations1995)) g1995.removeLayer(Lstations1995);
          }
          if (map.hasLayer(g2017)){
            if (g2017.hasLayer(Ladm2017))      g2017.removeLayer(Ladm2017);
            if (g2017.hasLayer(Lstations2017)) g2017.removeLayer(Lstations2017);
          }
        }

      })

    }
    </script>
-->    


    <script type="text/javascript">
    function map_init_default (map, options) {
      Lfeatures = makeFeatureLayer("{% url 'features' %}");
      Lsections1920 = makeSectionLayer("{% url 'sections' 1920 1950 %}");
      Lsections1950 = makeSectionLayer("{% url 'sections' 1951 1970 %}");
      Lsections1995 = makeSectionLayer("{% url 'sections' 1971 1990 %}");
      Lsections2017 = makeSectionLayer("{% url 'sections' 1991 2017 %}");

      Lstations1920 = makeStationLayer("{% url 'stations' 1920 1950 %}");
      Lstations1950 = makeStationLayer("{% url 'stations' 1951 1970 %}");
      Lstations1995 = makeStationLayer("{% url 'stations' 1971 1990 %}");
      Lstations2017 = makeStationLayer("{% url 'stations' 1991 2017 %}");

      LsectionsBase = makeSectionLayer("{% url 'sections' 1920 2017 %}");
      LstationsBase = makeStationLayer("{% url 'stations' 1920 2017 %}");

      Ladm1920  = makeAdmLayer("{% url 'adm1920' %}", 1920, "1920");
      Ladm1950  = makeAdmLayer("{% url 'adm1950' %}", 1950, "1950");
      Ladm1995  = makeAdmLayer("{% url 'adm1995' %}", 1995, "1995");
      Ladm2017  = makeAdmLayer("{% url 'adm2017' %}", 2017, "2017");

      g2017 = L.layerGroup([Lsections2017]);
      g1995 = L.layerGroup([Lsections1995]);
      g1950 = L.layerGroup([Lsections1950]);
      g1920 = L.layerGroup([Lsections1920]);

      var baseL = {
        '1991年〜現在': g2017,
        '1971〜1990年': g1995,
        '1951〜1970年': g1950,
        '1950年以前': g1920
      }

      cntl = L.control.layers(baseL,null,{collapsed:false});

      cntl.addTo(map);

      Lfeatures.addTo(map);

      gdefault = L.layerGroup([LsectionsBase]);
      gdefault.addTo(map);
      // map.fitBounds(Lfeatures.getBounds());

      map.on('baselayerchange', function(e) {
        // if at least one layer change occured,
        // we discard the gdefault layer!
        if (map.hasLayer(gdefault)) {
          map.removeLayer(gdefault);
        }
        // console.log(e.name);
        // console.log(map.getZoom());

        if (map.getZoom()>=10){
          switch(e.name) {
            case '1950年以前':
              if (!g1920.hasLayer(Ladm1920))      g1920.addLayer(Ladm1920);
              if (!g1920.hasLayer(Lstations1920)) g1920.addLayer(Lstations1920);
              Ladm1920.bringToBack();
              break;
            case '1951〜1970年':
              if (!g1950.hasLayer(Ladm1950))      g1950.addLayer(Ladm1950);
              if (!g1950.hasLayer(Lstations1950)) g1950.addLayer(Lstations1950);
              break;
            case '1971〜1990年':
              if (!g1995.hasLayer(Ladm1995))      g1995.addLayer(Ladm1995);
              if (!g1995.hasLayer(Lstations1995)) g1995.addLayer(Lstations1995);
              break;
            case '1990年〜現在':
              if (!g2017.hasLayer(Ladm2017))      g2017.addLayer(Ladm2017);
              if (!g2017.hasLayer(Lstations2017)) g2017.addLayer(Lstations2017);
              break;
            default:
              console.log("SOYALAB ERROR: UNKNOWN PERIOD SELECTED!!!: " + e.name);
              // do nothing
          }
        }
        else {
          switch(e.name) {
            case '1950年以前':
              g1920.removeLayer(Ladm1920);
              g1920.removeLayer(Lstations1920);
              break;
            case '1951〜1970年':
              g1950.removeLayer(Ladm1950);
              g1950.removeLayer(Lstations1950);
              break;
            case '1971〜1990年':
              g1995.removeLayer(Ladm1995);
              g1995.removeLayer(Lstations1995);
              break;
            case '1990年〜現在':
              g2017.removeLayer(Ladm2017);
              g2017.removeLayer(Lstations2017);
              break;
            default:
              console.log("SOYALAB ERROR: UNKNOWN PERIOD SELECTED!!!: " + e.name);
              // do nothing
          }
        }
      })

      map.on('zoomend', function(){
        if (map.getZoom()>=10){
          console.log(map.getZoom());

          if (map.hasLayer(gdefault)) gdefault.addLayer(LstationsBase);

          if (map.hasLayer(g1920)){
            if (!g1920.hasLayer(Ladm1920))      g1920.addLayer(Ladm1920);
            if (!g1920.hasLayer(Lstations1920)) g1920.addLayer(Lstations1920);
          }
          if (map.hasLayer(g1950)){
            if (!g1920.hasLayer(Ladm1950))      g1950.addLayer(Ladm1950);
            if (!g1920.hasLayer(Lstations1950)) g1950.addLayer(Lstations1950);
          }
          if (map.hasLayer(g1995)){
            if (!g1920.hasLayer(Ladm1995))      g1995.addLayer(Ladm1995);
            if (!g1920.hasLayer(Lstations1995)) g1995.addLayer(Lstations1995);
          }
          if (map.hasLayer(g2017)){
            if (!g1920.hasLayer(Ladm2017))      g2017.addLayer(Ladm2017);
            if (!g1920.hasLayer(Lstations2017)) g2017.addLayer(Lstations2017);
          }
        }
        else {
          if (map.hasLayer(gdefault)) gdefault.removeLayer(LstationsBase);

          if (map.hasLayer(g1920)){
            if (g1920.hasLayer(Ladm1920))      g1920.removeLayer(Ladm1920);
            if (g1920.hasLayer(Lstations1920)) g1920.removeLayer(Lstations1920);
          }
          if (map.hasLayer(g1950)){
            if (g1950.hasLayer(Ladm1950))      g1950.removeLayer(Ladm1950);
            if (g1950.hasLayer(Lstations1950)) g1950.removeLayer(Lstations1950);
          }
          if (map.hasLayer(g1995)){
            if (g1995.hasLayer(Ladm1995))      g1995.removeLayer(Ladm1995);
            if (g1995.hasLayer(Lstations1995)) g1995.removeLayer(Lstations1995);
          }
          if (map.hasLayer(g2017)){
            if (g2017.hasLayer(Ladm2017))      g2017.removeLayer(Ladm2017);
            if (g2017.hasLayer(Lstations2017)) g2017.removeLayer(Lstations2017);
          }
        }

      })

    }
    </script>