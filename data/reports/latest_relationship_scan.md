# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T09:52:17.718709+00:00`
- Price records: `672`
- Market context records: `1106`
- Flow alert records: `5088`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `17.458` n `150` status `ready` deltaP `37.9028` edge `1.2485` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.9479` n `150` status `ready` deltaP `14.2639` edge `0.6073` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.1943` n `150` status `ready` deltaP `15.6527` edge `0.4615` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.3533` n `150` status `ready` deltaP `-2.7569` edge `0.6312` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.9377` n `150` status `ready` deltaP `15.1319` edge `0.3414` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.7988` n `168` status `ready` deltaP `10.4893` edge `0.1463` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9639` n `168` status `ready` deltaP `8.8995` edge `0.0893` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4654` n `168` status `ready` deltaP `7.4957` edge `0.0205` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.256` n `168` status `ready` deltaP `2.5805` edge `0.0419` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1364` n `168` status `ready` deltaP `8.3155` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1137` n `168` status `ready` deltaP `7.4316` edge `0.0365` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0504` n `168` status `ready` deltaP `8.4567` edge `0.1422` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1944` n `168` status `ready` deltaP `6.9504` edge `-0.0015` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.237` n `168` status `ready` deltaP `3.0938` edge `0.0439` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.67` n `168` status `ready` deltaP `1.851` edge `0.0014` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7185` n `168` status `ready` deltaP `-1.4756` edge `-0.0015` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0569` n `168` status `ready` deltaP `5.2338` edge `0.1261` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3051` n `168` status `ready` deltaP `7.1574` edge `-0.0444` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1313` n `168` status `ready` deltaP `-10.6635` edge `-0.0136` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2922` n `150` status `ready` deltaP `1.868` edge `-0.0269` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
