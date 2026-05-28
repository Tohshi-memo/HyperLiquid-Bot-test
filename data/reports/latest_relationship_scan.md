# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T03:52:16.376703+00:00`
- Price records: `672`
- Market context records: `2105`
- Flow alert records: `7954`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.7935` n `176` status `ready` deltaP `31.2639` edge `0.8055` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.5746` n `176` status `ready` deltaP `37.8464` edge `0.6819` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7889` n `176` status `ready` deltaP `23.628` edge `0.3998` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1872` n `176` status `ready` deltaP `22.7827` edge `0.3065` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5414` n `176` status `ready` deltaP `19.0272` edge `0.1533` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.3647` n `175` status `ready` deltaP `11.8497` edge `0.2409` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.276` n `175` status `ready` deltaP `23.221` edge `0.5669` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `2.1861` n `176` status `ready` deltaP `15.4634` edge `0.1777` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.0131` n `176` status `ready` deltaP `12.4694` edge `0.196` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6034` n `175` status `ready` deltaP `23.0796` edge `0.4696` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.2314` n `176` status `ready` deltaP `16.3525` edge `0.1878` maxDD `-9.2029`
- `market_context_high->equity_1h` score `0.8325` n `176` status `ready` deltaP `10.8771` edge `0.0757` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.2116` n `175` status `ready` deltaP `20.868` edge `0.7371` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.1523` n `176` status `ready` deltaP `6.1548` edge `0.0307` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `0.0889` n `176` status `ready` deltaP `5.1409` edge `0.0451` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0754` n `175` status `ready` deltaP `14.8858` edge `0.0304` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2449` n `176` status `ready` deltaP `6.6106` edge `0.0376` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.5806` n `176` status `ready` deltaP `-1.8542` edge `0.0007` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-0.8723` n `175` status `ready` deltaP `9.9792` edge `0.2509` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0669` n `176` status `ready` deltaP `-6.8459` edge `-0.003` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
