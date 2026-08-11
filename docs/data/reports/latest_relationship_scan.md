# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T05:41:02.798964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_24h` score `31.8732` n `133` status `ready` deltaP `-17.2789` edge `3.0167` maxDD `-9.6329`
- `market_context_high->commodity_1h` score `0.6669` n `180` status `ready` deltaP `9.3114` edge `0.0278` maxDD `-0.7439`
- `market_context_high->commodity_4h` score `0.6538` n `169` status `ready` deltaP `10.3267` edge `0.0571` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.5602` n `133` status `ready` deltaP `18.088` edge `0.032` maxDD `-1.4613`
- `market_context_high->commodity_24h` score `0.2915` n `133` status `ready` deltaP `12.0457` edge `0.1615` maxDD `-11.0218`
- `market_context_high->fx_4h` score `-0.2201` n `169` status `ready` deltaP `4.2077` edge `0.0042` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.277` n `180` status `ready` deltaP `1.6866` edge `-0.0016` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8615` n `180` status `ready` deltaP `-7.0758` edge `-0.0049` maxDD `-1.0034`
- `market_context_high->metal_1h` score `-0.951` n `180` status `ready` deltaP `-6.843` edge `-0.0127` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.4177` n `169` status `ready` deltaP `-3.0622` edge `-0.0083` maxDD `-1.4875`
- `market_context_high->equity_1h` score `-1.5106` n `180` status `ready` deltaP `-6.8662` edge `-0.0202` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.4042` n `133` status `ready` deltaP `0.3877` edge `-0.0705` maxDD `-2.9283`
- `market_context_high->crypto_alt_1h` score `-2.6333` n `180` status `ready` deltaP `-9.1084` edge `-0.0402` maxDD `-6.4812`
- `market_context_high->index_24h` score `-2.7225` n `133` status `ready` deltaP `-13.5313` edge `-0.0493` maxDD `-6.7627`
- `market_context_high->metal_4h` score `-3.4173` n `169` status `ready` deltaP `-9.6584` edge `-0.044` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.4599` n `180` status `ready` deltaP `-7.8011` edge `-0.0459` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-3.994` n `169` status `ready` deltaP `-12.5467` edge `-0.1175` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.639` n `169` status `ready` deltaP `-12.4116` edge `-0.1357` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.086` n `133` status `ready` deltaP `-15.2744` edge `-0.2295` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.0785` n `133` status `ready` deltaP `-11.3433` edge `-0.2011` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
