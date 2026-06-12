# Latest Sector Reactions

Sector reaction data tracks how ETF sector proxies moved after public conditions. It is a hypothesis dataset, not a trade signal.

- Generated: `2026-06-12T04:07:31.421167+00:00`
- Price records: `6500`
- Reaction rows: `120672`
- Stored reaction rows: `5000`
- Minimum samples: `20`
- Horizons: `1d, 5d, 20d, 60d, 120d, 252d`

## Sector Snapshot

- `SMH` semiconductors: 5d `-1.8004`, 20d `19.8595`, 60d `35.6265`
- `XLK` technology: 5d `0.4216`, 20d `14.195`, 60d `25.8677`
- `XHB` homebuilders: 5d `-6.0384`, 20d `-10.1911`, 60d `-18.0215`
- `QQQ` nasdaq_100: 5d `-0.3234`, 20d `9.2595`, 60d `17.6237`
- `XLE` energy: 5d `6.7145`, 20d `8.0334`, 60d `8.424`
- `XLU` utilities: 5d `-1.9007`, 20d `-4.961`, 60d `-4.1928`
- `SPY` broad_market: 5d `0.2101`, 20d `4.0879`, 60d `8.2849`
- `XLY` consumer_discretionary: 5d `-3.0532`, 20d `-3.2223`, 60d `0.4509`
- `IYR` real_estate_broad: 5d `-2.8899`, 20d `-3.088`, 60d `0.2505`
- `XLB` materials: 5d `-2.5005`, 20d `-3.0455`, 60d `-4.3655`
- `XLRE` real_estate: 5d `-2.6571`, 20d `-2.8103`, 60d `0.742`
- `XLP` consumer_staples: 5d `0.5464`, 20d `2.6437`, 60d `-2.9127`

## Top Delayed-Reaction Patterns

- `small_caps_5d_up->XLC_252d` score `376.9832`, n `278`, avg `23.378`, up `86.6906`, status `ready`
- `broad_risk_on_20d->XLC_252d` score `375.4159`, n `393`, avg `23.2911`, up `84.4784`, status `ready`
- `broad_risk_on_20d->SMH_252d` score `344.731`, n `1047`, avg `21.4294`, up `73.2569`, status `ready`
- `semis_5d_up->XLC_252d` score `342.1398`, n `366`, avg `21.2198`, up `82.7869`, status `ready`
- `rates_sensitive_rebound->XLC_252d` score `338.7805`, n `434`, avg `21.0171`, up `81.3364`, status `ready`
- `small_caps_5d_up->SMH_252d` score `335.1649`, n `905`, avg `20.8293`, up `73.7017`, status `ready`
- `rates_sensitive_rebound->SMH_252d` score `332.6552`, n `1284`, avg `20.6788`, up `72.4299`, status `ready`
- `broad_risk_on_20d->XHB_252d` score `293.9723`, n `832`, avg `18.2693`, up `70.7933`, status `ready`
- `semis_5d_up->SMH_252d` score `291.9806`, n `1006`, avg `18.1633`, up `67.0974`, status `ready`
- `defensive_rotation->SMH_252d` score `291.8656`, n `1954`, avg `18.1372`, up `70.8802`, status `ready`
- `defensive_rotation->XLC_252d` score `279.5453`, n `556`, avg `17.3232`, up `79.6763`, status `ready`
- `small_caps_5d_up->XHB_252d` score `278.7824`, n `697`, avg `17.3145`, up `71.8795`, status `ready`
- `semis_5d_up->XHB_252d` score `278.7559`, n `693`, avg `17.3151`, up `71.4286`, status `ready`
- `rates_sensitive_rebound->QQQ_252d` score `278.2325`, n `1284`, avg `17.2178`, up `84.3458`, status `ready`
- `small_caps_5d_up->QQQ_252d` score `266.9855`, n `905`, avg `16.5156`, up `84.1989`, status `ready`
- `rates_sensitive_rebound->XLK_252d` score `265.9819`, n `1284`, avg `16.4572`, up `83.3333`, status `ready`
- `broad_risk_on_20d->QQQ_252d` score `263.7214`, n `1047`, avg `16.3195`, up `82.617`, status `ready`
- `small_caps_5d_up->XLE_252d` score `255.8835`, n `905`, avg `15.8825`, up `72.0442`, status `ready`
- `small_caps_5d_up->XLK_252d` score `254.9179`, n `905`, avg `15.7669`, up `83.0939`, status `ready`
- `small_caps_5d_up->XLY_252d` score `254.0038`, n `905`, avg `15.6954`, up `85.9669`, status `ready`
- `broad_risk_on_20d->XLK_252d` score `246.6057`, n `1047`, avg `15.2598`, up `80.6113`, status `ready`
- `broad_risk_on_20d->XLY_252d` score `242.4221`, n `1047`, avg `14.984`, up `83.4766`, status `ready`
- `energy_5d_up->XLC_252d` score `238.7413`, n `382`, avg `14.814`, up `71.466`, status `ready`
- `small_caps_5d_up->XLI_252d` score `237.2424`, n `905`, avg `14.6666`, up `82.2099`, status `ready`
- `small_caps_5d_up->IYR_252d` score `234.0486`, n `905`, avg `14.4808`, up `79.4475`, status `ready`

## Conditions

- `news_risk_high`: Collected news risk score is elevated.
- `macro_risk_high`: Collected macro risk score is elevated.
- `risk_on_high`: Collected risk-on score is elevated.
- `market_context_high`: Collected market context score is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow alert score is elevated.
- `energy_5d_up`: Energy proxy XLE rose at least 3% over 5 trading days.
- `semis_5d_up`: Semiconductor proxy SMH rose at least 4% over 5 trading days.
- `rates_sensitive_rebound`: Homebuilders or real estate rebounded at least 3% over 5 trading days.
- `defensive_rotation`: Utilities outperformed SPY by at least 2% over 20 trading days.
- `broad_risk_on_20d`: SPY and QQQ both rose strongly over 20 trading days.
- `small_caps_5d_up`: IWM rose at least 3% over 5 trading days.
