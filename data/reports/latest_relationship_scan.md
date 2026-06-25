# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T13:22:31.917727+00:00`
- Price records: `672`
- Market context records: `4727`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `77.8575` n `143` status `ready` deltaP `15.2381` edge `6.4283` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.6344` n `143` status `ready` deltaP `14.8463` edge `0.4916` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2802` n `134` status `ready` deltaP `16.6925` edge `0.2544` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2871` n `143` status `ready` deltaP `2.593` edge `0.0255` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.651` n `143` status `ready` deltaP `4.6084` edge `-0.0019` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.8792` n `143` status `ready` deltaP `-0.4296` edge `-0.0019` maxDD `-1.9695`
- `market_context_high->commodity_4h` score `-0.8894` n `143` status `ready` deltaP `9.3797` edge `0.0342` maxDD `-9.1941`
- `market_context_high->equity_1h` score `-0.9514` n `143` status `ready` deltaP `-1.7975` edge `-0.0113` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.1446` n `143` status `ready` deltaP `3.2364` edge `0.0086` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3183` n `143` status `ready` deltaP `-5.3987` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6217` n `143` status `ready` deltaP `-3.8441` edge `-0.0091` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1613` n `143` status `ready` deltaP `-0.7004` edge `-0.0719` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.6457` n `143` status `ready` deltaP `-0.7517` edge `-0.0871` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3135` n `134` status `ready` deltaP `17.102` edge `0.0689` maxDD `-30.0562`
- `market_context_high->metal_1h` score `-4.4225` n `143` status `ready` deltaP `-5.7986` edge `-0.0783` maxDD `-16.7937`
- `market_context_high->fx_24h` score `-4.8025` n `134` status `ready` deltaP `-13.5339` edge `-0.0185` maxDD `-5.3183`
- `market_context_high->crypto_alt_4h` score `-7.8129` n `143` status `ready` deltaP `-1.7121` edge `-0.1379` maxDD `-62.8536`
- `market_context_high->index_24h` score `-8.4466` n `134` status `ready` deltaP `-11.352` edge `-0.1008` maxDD `-28.859`
- `market_context_high->metal_4h` score `-8.6964` n `143` status `ready` deltaP `1.9827` edge `-0.2556` maxDD `-63.8028`
- `market_context_high->crypto_major_4h` score `-10.4877` n `143` status `ready` deltaP `-1.2814` edge `-0.246` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
