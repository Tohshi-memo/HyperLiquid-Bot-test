# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T16:22:25.791160+00:00`
- Price records: `672`
- Market context records: `1954`
- Flow alert records: `7521`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `7.0076` n `232` status `ready` deltaP `21.6495` edge `0.5541` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4672` n `232` status `ready` deltaP `25.3254` edge `0.4947` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3387` n `232` status `ready` deltaP `13.2577` edge `0.3089` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0988` n `232` status `ready` deltaP `14.2425` edge `0.1894` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.0935` n `199` status `ready` deltaP `16.4203` edge `0.5137` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8193` n `234` status `ready` deltaP `8.3538` edge `0.1112` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6504` n `234` status `ready` deltaP `7.6463` edge `0.1146` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3523` n `199` status `ready` deltaP `12.1584` edge `0.1909` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.147` n `232` status `ready` deltaP `8.437` edge `0.0649` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1369` n `199` status `ready` deltaP `4.1922` edge `0.1063` maxDD `-4.1604`
- `market_context_high->equity_24h` score `-0.1944` n `199` status `ready` deltaP `10.8368` edge `0.4014` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.2494` n `234` status `ready` deltaP `4.6497` edge `0.0276` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2591` n `199` status `ready` deltaP `9.9323` edge `0.0171` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6421` n `234` status `ready` deltaP `-2.8635` edge `0.0` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6581` n `234` status `ready` deltaP `0.485` edge `0.0051` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.0757` n `232` status `ready` deltaP `-6.8985` edge `-0.0031` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2412` n `234` status `ready` deltaP `3.5468` edge `0.0065` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5863` n `234` status `ready` deltaP `0.2099` edge `-0.0384` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.6219` n `199` status `ready` deltaP `15.3783` edge `0.6209` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.8443` n `232` status `ready` deltaP `6.7194` edge `0.0707` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
