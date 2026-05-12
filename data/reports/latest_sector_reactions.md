# Latest Sector Reactions

Sector reaction data tracks how ETF sector proxies moved after public conditions. It is a hypothesis dataset, not a trade signal.

- Generated: `2026-05-12T03:07:23.507617+00:00`
- Price records: `6500`
- Reaction rows: `120572`
- Stored reaction rows: `5000`
- Minimum samples: `20`
- Horizons: `1d, 5d, 20d, 60d, 120d, 252d`

## Sector Snapshot

- `SMH` semiconductors: 5d `13.7177`, 20d `29.9928`, 60d `41.9098`
- `XLK` technology: 5d `9.7686`, 20d `22.1619`, 60d `27.937`
- `QQQ` nasdaq_100: 5d `6.0055`, 20d `15.5331`, 60d `18.9047`
- `SPY` broad_market: 5d `2.9651`, 20d `7.754`, 60d `8.8143`
- `IWM` small_caps: 5d `2.681`, 20d `7.6433`, 60d `10.1324`
- `XLY` consumer_discretionary: 5d `1.4016`, 20d `4.7841`, 60d `2.9965`
- `XHB` homebuilders: 5d `0.1874`, 20d `-3.7335`, 60d `-14.4509`
- `XLRE` real_estate: 5d `1.1116`, 20d `3.603`, 60d `4.6643`
- `IYR` real_estate_broad: 5d `1.1906`, 20d `3.4087`, 60d `4.3073`
- `XLV` healthcare: 5d `-1.1677`, 20d `-3.3318`, 60d `-7.9308`
- `XLU` utilities: 5d `-2.6526`, 20d `-2.6945`, 60d `0.4543`
- `XLP` consumer_staples: 5d `-0.2035`, 20d `2.2318`, 60d `-6.0203`

## Top Delayed-Reaction Patterns

- `small_caps_5d_up->XLC_252d` score `377.8964`, n `275`, avg `23.4358`, up `86.5455`, status `ready`
- `broad_risk_on_20d->XLC_252d` score `376.1519`, n `389`, avg `23.3379`, up `84.3188`, status `ready`
- `semis_5d_up->XLC_252d` score `342.5444`, n `363`, avg `21.2458`, up `82.6446`, status `ready`
- `rates_sensitive_rebound->XLC_252d` score `339.0965`, n `431`, avg `21.0375`, up `81.2065`, status `ready`
- `broad_risk_on_20d->SMH_252d` score `337.5212`, n `1043`, avg `20.9793`, up `73.1544`, status `ready`
- `rates_sensitive_rebound->SMH_252d` score `328.3892`, n `1281`, avg `20.4125`, up `72.3653`, status `ready`
- `small_caps_5d_up->SMH_252d` score `327.7962`, n `903`, avg `20.3696`, up `73.5327`, status `ready`
- `broad_risk_on_20d->XHB_252d` score `295.374`, n `828`, avg `18.3558`, up `71.0145`, status `ready`
- `defensive_rotation->SMH_252d` score `291.8656`, n `1954`, avg `18.1372`, up `70.8802`, status `ready`
- `semis_5d_up->SMH_252d` score `281.7034`, n `1007`, avg `17.5228`, up `66.7329`, status `ready`
- `small_caps_5d_up->XHB_252d` score `280.0744`, n `694`, avg `17.3937`, up `72.1902`, status `ready`
- `semis_5d_up->XHB_252d` score `280.0559`, n `690`, avg `17.3948`, up `71.7391`, status `ready`
- `defensive_rotation->XLC_252d` score `279.5453`, n `556`, avg `17.3232`, up `79.6763`, status `ready`
- `rates_sensitive_rebound->QQQ_252d` score `277.3879`, n `1281`, avg `17.1652`, up `84.3091`, status `ready`
- `rates_sensitive_rebound->XLK_252d` score `264.5611`, n `1281`, avg `16.3686`, up `83.2943`, status `ready`
- `small_caps_5d_up->QQQ_252d` score `264.4539`, n `903`, avg `16.3581`, up `84.0532`, status `ready`
- `broad_risk_on_20d->QQQ_252d` score `262.1912`, n `1043`, avg `16.2242`, up `82.5503`, status `ready`
- `small_caps_5d_up->XLE_252d` score `254.2434`, n `903`, avg `15.7803`, up `71.9823`, status `ready`
- `small_caps_5d_up->XLY_252d` score `254.0493`, n `903`, avg `15.6984`, up `85.9358`, status `ready`
- `small_caps_5d_up->XLK_252d` score `251.6741`, n `903`, avg `15.5649`, up `82.9457`, status `ready`
- `broad_risk_on_20d->XLK_252d` score `244.0878`, n `1043`, avg `15.1028`, up `80.5369`, status `ready`
- `broad_risk_on_20d->XLY_252d` score `242.5659`, n `1043`, avg `14.9933`, up `83.4132`, status `ready`
- `energy_5d_up->XLC_252d` score `238.3088`, n `379`, avg `14.7881`, up `71.2401`, status `ready`
- `small_caps_5d_up->XLI_252d` score `236.4336`, n `903`, avg `14.6168`, up `82.0598`, status `ready`
- `small_caps_5d_up->IYR_252d` score `234.3362`, n `903`, avg `14.499`, up `79.402`, status `ready`

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
