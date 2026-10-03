# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T01:52:30.376504+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.8946` n `50` status `ready` deltaP `10.5749` edge `30.3423` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.2021` n `50` status `ready` deltaP `10.3659` edge `24.3644` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.7429` n `70` status `ready` deltaP `32.9365` edge `1.0671` maxDD `-2.3147`
- `market_context_high->crypto_alt_24h` score `10.8737` n `50` status `ready` deltaP `21.2222` edge `0.935` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.9326` n `70` status `ready` deltaP `33.7351` edge `0.6513` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.8942` n `50` status `ready` deltaP `31.3056` edge `0.6741` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.6797` n `102` status `ready` deltaP `31.4831` edge `0.5645` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4801` n `50` status `ready` deltaP `17.8476` edge `0.5747` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.6633` n `70` status `ready` deltaP `12.1627` edge `0.6037` maxDD `-5.6942`
- `market_context_high->crypto_alt_4h` score `5.8921` n `50` status `ready` deltaP `16.189` edge `0.512` maxDD `-7.6465`
- `news_risk_high->crypto_major_4h` score `5.5972` n `102` status `ready` deltaP `23.377` edge `0.4113` maxDD `-4.7236`
- `market_context_high->crypto_alt_1h` score `3.229` n `50` status `ready` deltaP `14.8024` edge `0.2367` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.0823` n `102` status `ready` deltaP `25.1883` edge `0.1502` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0037` n `50` status `ready` deltaP `13.4012` edge `0.206` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8165` n `50` status `ready` deltaP `31.4695` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->index_24h` score `1.8348` n `70` status `ready` deltaP `19.2361` edge `0.0697` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.7113` n `70` status `ready` deltaP `9.6329` edge `0.2001` maxDD `-2.0701`
- `market_context_high->fx_1h` score `1.422` n `50` status `ready` deltaP `20.0419` edge `0.0113` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.3976` n `102` status `ready` deltaP `5.6651` edge `0.1306` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2382` n `50` status `ready` deltaP `6.0208` edge `0.3048` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
