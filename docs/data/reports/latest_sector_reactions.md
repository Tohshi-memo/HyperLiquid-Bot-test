# Latest Sector Reactions

Sector reaction data tracks how ETF sector proxies moved after public conditions. It is a hypothesis dataset, not a trade signal.

- Generated: `2026-07-15T10:52:25.885077+00:00`
- Price records: `6500`
- Reaction rows: `121162`
- Stored reaction rows: `5000`
- Minimum samples: `20`
- Horizons: `1d, 5d, 20d, 60d, 120d, 252d`

## Sector Snapshot

- `SMH` semiconductors: 5d `8.2747`, 20d `16.8633`, 60d `67.2318`
- `XHB` homebuilders: 5d `2.9769`, 20d `12.2523`, 60d `11.4695`
- `XLE` energy: 5d `-5.8648`, 20d `-10.0836`, 60d `-11.6206`
- `XLK` technology: 5d `4.4921`, 20d `8.0727`, 60d `40.6096`
- `XLI` industrials: 5d `3.2886`, 20d `5.9626`, 60d `10.311`
- `IWM` small_caps: 5d `2.0257`, 20d `5.8681`, 60d `19.0984`
- `XLC` communication_services: 5d `-2.3814`, 20d `-5.7278`, 60d `-1.5117`
- `XLB` materials: 5d `1.1519`, 20d `4.2035`, 60d `6.935`
- `QQQ` nasdaq_100: 5d `3.277`, 20d `3.8519`, 60d `26.8228`
- `XLF` financials: 5d `1.8054`, 20d `3.6973`, 60d `8.7054`
- `XLP` consumer_staples: 5d `-2.3103`, 20d `-2.5959`, 60d `2.7`
- `XLV` healthcare: 5d `-3.0437`, 20d `1.5428`, 60d `3.1839`

## Top Delayed-Reaction Patterns

- `broad_risk_on_20d->SMH_252d` score `382.3794`, n `1058`, avg `23.7782`, up `74.1021`, status `ready`
- `small_caps_5d_up->XLC_252d` score `374.5232`, n `282`, avg `23.2233`, up `86.8794`, status `ready`
- `broad_risk_on_20d->XLC_252d` score `369.1986`, n `410`, avg `22.8993`, up `85.122`, status `ready`
- `small_caps_5d_up->SMH_252d` score `342.5182`, n `909`, avg `21.2883`, up `73.8174`, status `ready`
- `rates_sensitive_rebound->SMH_252d` score `339.8368`, n `1283`, avg `21.1262`, up `72.7202`, status `ready`
- `semis_5d_up->XLC_252d` score `339.0584`, n `373`, avg `21.0256`, up `83.1099`, status `ready`
- `rates_sensitive_rebound->XLC_252d` score `337.6644`, n `437`, avg `20.9467`, up `81.4645`, status `ready`
- `semis_5d_up->SMH_252d` score `311.1013`, n `1007`, avg `19.3552`, up `67.7259`, status `ready`
- `defensive_rotation->SMH_252d` score `295.9356`, n `1947`, avg `18.3903`, up `71.1351`, status `ready`
- `broad_risk_on_20d->XHB_252d` score `290.378`, n `849`, avg `18.0435`, up `71.0247`, status `ready`
- `rates_sensitive_rebound->QQQ_252d` score `282.4116`, n `1283`, avg `17.4775`, up `84.6454`, status `ready`
- `defensive_rotation->XLC_252d` score `279.5453`, n `556`, avg `17.3232`, up `79.6763`, status `ready`
- `small_caps_5d_up->XHB_252d` score `277.5212`, n `701`, avg `17.2363`, up `71.7546`, status `ready`
- `semis_5d_up->XHB_252d` score `277.1383`, n `700`, avg `17.214`, up `71.4286`, status `ready`
- `broad_risk_on_20d->QQQ_252d` score `276.802`, n `1058`, avg `17.1333`, up `83.3648`, status `ready`
- `rates_sensitive_rebound->XLK_252d` score `270.5146`, n `1283`, avg `16.739`, up `83.6321`, status `ready`
- `small_caps_5d_up->QQQ_252d` score `268.2455`, n `909`, avg `16.594`, up `84.2684`, status `ready`
- `broad_risk_on_20d->XLK_252d` score `264.4928`, n `1058`, avg `16.3739`, up `81.38`, status `ready`
- `small_caps_5d_up->XLE_252d` score `257.943`, n `909`, avg `16.0106`, up `72.1672`, status `ready`
- `small_caps_5d_up->XLK_252d` score `257.3127`, n `909`, avg `15.9162`, up `83.1683`, status `ready`
- `small_caps_5d_up->XLY_252d` score `253.4727`, n `909`, avg `15.6619`, up `86.0286`, status `ready`
- `energy_5d_up->SMH_252d` score `245.822`, n `1193`, avg `15.2987`, up `63.0344`, status `ready`
- `broad_risk_on_20d->XLY_252d` score `242.1815`, n `1058`, avg `14.9681`, up `83.6484`, status `ready`
- `small_caps_5d_up->XLI_252d` score `237.6631`, n `909`, avg `14.6925`, up `82.2882`, status `ready`
- `energy_5d_up->XLC_252d` score `237.5648`, n `389`, avg `14.7379`, up `71.9794`, status `ready`

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
