# Latest Sector Reactions

Sector reaction data tracks how ETF sector proxies moved after public conditions. It is a hypothesis dataset, not a trade signal.

- Generated: `2026-05-09T23:37:14.747750+00:00`
- Price records: `6500`
- Reaction rows: `120580`
- Stored reaction rows: `5000`
- Minimum samples: `20`
- Horizons: `1d, 5d, 20d, 60d, 120d, 252d`

## Sector Snapshot

- `SMH` semiconductors: 5d `10.8195`, 20d `29.3215`, 60d `36.212`
- `XLK` technology: 5d `8.1053`, 20d `22.6967`, 60d `22.5485`
- `QQQ` nasdaq_100: 5d `5.2704`, 20d `16.1373`, 60d `15.8968`
- `SPY` broad_market: 5d `2.2965`, 20d `8.4979`, 60d `6.8289`
- `IWM` small_caps: 5d `1.5074`, 20d `8.4922`, 60d `7.1879`
- `XLY` consumer_discretionary: 5d `1.5637`, 20d `6.7278`, 60d `2.5196`
- `XLU` utilities: 5d `-3.5553`, 20d `-4.3974`, 60d `1.3879`
- `XLRE` real_estate: 5d `0.5415`, 20d `4.0635`, 60d `4.8119`
- `IYR` real_estate_broad: 5d `0.6594`, 20d `4.0547`, 60d `4.4417`
- `XLV` healthcare: 5d `-1.2262`, 20d `-2.6678`, 60d `-7.8596`
- `XLP` consumer_staples: 5d `0.4455`, 20d `2.6405`, 60d `-3.8225`
- `XLC` communication_services: 5d `0.0427`, 20d `2.4747`, 60d `0.3448`

## Top Delayed-Reaction Patterns

- `small_caps_5d_up->XLC_252d` score `377.8964`, n `275`, avg `23.4358`, up `86.5455`, status `ready`
- `broad_risk_on_20d->XLC_252d` score `376.1455`, n `389`, avg `23.3375`, up `84.3188`, status `ready`
- `semis_5d_up->XLC_252d` score `342.5965`, n `362`, avg `21.2493`, up `82.5967`, status `ready`
- `rates_sensitive_rebound->XLC_252d` score `339.0965`, n `431`, avg `21.0375`, up `81.2065`, status `ready`
- `broad_risk_on_20d->SMH_252d` score `337.51`, n `1043`, avg `20.9786`, up `73.1544`, status `ready`
- `rates_sensitive_rebound->SMH_252d` score `328.3892`, n `1281`, avg `20.4125`, up `72.3653`, status `ready`
- `small_caps_5d_up->SMH_252d` score `326.5129`, n `904`, avg `20.2898`, up `73.4513`, status `ready`
- `broad_risk_on_20d->XHB_252d` score `295.3852`, n `828`, avg `18.3565`, up `71.0145`, status `ready`
- `defensive_rotation->SMH_252d` score `290.6996`, n `1953`, avg `18.0644`, up `70.8653`, status `ready`
- `semis_5d_up->XHB_252d` score `280.3342`, n `689`, avg `17.4124`, up `71.6981`, status `ready`
- `small_caps_5d_up->XHB_252d` score `280.0744`, n `694`, avg `17.3937`, up `72.1902`, status `ready`
- `defensive_rotation->XLC_252d` score `279.4704`, n `555`, avg `17.3187`, up `79.6396`, status `ready`
- `semis_5d_up->SMH_252d` score `278.3131`, n `1007`, avg `17.3114`, up `66.6336`, status `ready`
- `rates_sensitive_rebound->QQQ_252d` score `277.3879`, n `1281`, avg `17.1652`, up `84.3091`, status `ready`
- `rates_sensitive_rebound->XLK_252d` score `264.5611`, n `1281`, avg `16.3686`, up `83.2943`, status `ready`
- `small_caps_5d_up->QQQ_252d` score `263.1808`, n `904`, avg `16.279`, up `83.9602`, status `ready`
- `broad_risk_on_20d->QQQ_252d` score `262.1864`, n `1043`, avg `16.2239`, up `82.5503`, status `ready`
- `small_caps_5d_up->XLE_252d` score `253.9298`, n `904`, avg `15.7611`, up `71.9027`, status `ready`
- `small_caps_5d_up->XLY_252d` score `253.7769`, n `904`, avg `15.6813`, up `85.9513`, status `ready`
- `small_caps_5d_up->XLK_252d` score `250.5003`, n `904`, avg `15.492`, up `82.854`, status `ready`
- `broad_risk_on_20d->XLK_252d` score `244.0798`, n `1043`, avg `15.1023`, up `80.5369`, status `ready`
- `broad_risk_on_20d->XLY_252d` score `242.5707`, n `1043`, avg `14.9936`, up `83.4132`, status `ready`
- `energy_5d_up->XLC_252d` score `238.3088`, n `379`, avg `14.7881`, up `71.2401`, status `ready`
- `small_caps_5d_up->XLI_252d` score `236.1655`, n `904`, avg `14.6005`, up `81.969`, status `ready`
- `small_caps_5d_up->IYR_252d` score `234.4052`, n `904`, avg `14.5032`, up `79.4248`, status `ready`

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
