# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T02:37:18.541605+00:00`
- Price records: `672`
- Market context records: `1692`
- Flow alert records: `6779`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `6.8857` n `143` status `ready` deltaP `25.9213` edge `0.6436` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.8113` n `143` status `ready` deltaP `17.9774` edge `0.9798` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `5.2505` n `192` status `ready` deltaP `22.4339` edge `0.5544` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9815` n `192` status `ready` deltaP `22.1671` edge `0.4549` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8759` n `143` status `ready` deltaP `17.249` edge `0.3458` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9799` n `192` status `ready` deltaP `15.7012` edge `0.2531` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8964` n `143` status `ready` deltaP `16.1819` edge `0.54` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6721` n `199` status `ready` deltaP `6.5056` edge `0.115` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4014` n `143` status `ready` deltaP `24.2493` edge `1.0527` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.3486` n `192` status `ready` deltaP `7.3424` edge `0.089` maxDD `-3.7119`
- `market_context_high->equity_1h` score `0.0185` n `199` status `ready` deltaP `4.634` edge `0.0515` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.1214` n `199` status `ready` deltaP `3.9825` edge `0.0815` maxDD `-4.7865`
- `market_context_high->index_1h` score `-0.5378` n `199` status `ready` deltaP `0.3679` edge `0.0159` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.5782` n `192` status `ready` deltaP `12.0299` edge `0.1408` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5879` n `199` status `ready` deltaP `6.1957` edge `0.0169` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-0.5907` n `143` status `ready` deltaP `22.6269` edge `0.632` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.6636` n `199` status `ready` deltaP `-2.903` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7982` n `143` status `ready` deltaP `4.8431` edge `0.0061` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.7044` n `192` status `ready` deltaP `-5.8562` edge `-0.0101` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1235` n `199` status `ready` deltaP `0.4649` edge `-0.0299` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
