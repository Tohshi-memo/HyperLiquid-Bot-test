# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T20:02:53.421995+00:00`
- Price records: `672`
- Market context records: `5698`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.3058` n `258` status `ready` deltaP `13.2563` edge `0.2409` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.1533` n `208` status `ready` deltaP `16.2527` edge `0.5474` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.1129` n `258` status `ready` deltaP `10.5821` edge `0.1831` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2603` n `258` status `ready` deltaP `6.998` edge `0.1389` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.1618` n `270` status `ready` deltaP `4.287` edge `0.0452` maxDD `-3.9811`
- `market_context_high->fx_1h` score `-0.2567` n `270` status `ready` deltaP `2.0725` edge `0.0009` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.2604` n `270` status `ready` deltaP `2.6325` edge `0.0426` maxDD `-3.8812`
- `market_context_high->metal_1h` score `-0.4413` n `270` status `ready` deltaP `1.6866` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5358` n `270` status `ready` deltaP `4.012` edge `0.0293` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6079` n `270` status `ready` deltaP `0.6465` edge `0.0046` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9387` n `208` status `ready` deltaP `13.2212` edge `0.046` maxDD `-3.3591`
- `market_context_high->commodity_1h` score `-1.1046` n `270` status `ready` deltaP `-1.0246` edge `-0.0045` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.177` n `258` status `ready` deltaP `3.876` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.338` n `258` status `ready` deltaP `-1.4027` edge `0.0065` maxDD `-3.1621`
- `market_context_high->metal_4h` score `-2.7469` n `258` status `ready` deltaP `-9.3898` edge `-0.052` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8777` n `208` status `ready` deltaP `2.6442` edge `0.026` maxDD `-18.005`
- `market_context_high->crypto_major_24h` score `-3.7403` n `208` status `ready` deltaP `6.6907` edge `0.0894` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.977` n `258` status `ready` deltaP `-4.4196` edge `-0.0344` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0582` n `208` status `ready` deltaP `-9.1346` edge `-0.2446` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.3166` n `208` status `ready` deltaP `-12.6736` edge `-0.081` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
