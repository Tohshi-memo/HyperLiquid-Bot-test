# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T17:52:27.597824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4086`

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

- `news_risk_high->equity_4h` score `2.5517` n `99` status `ready` deltaP `17.3719` edge `0.3019` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.1123` n `99` status `ready` deltaP `16.7052` edge `0.0291` maxDD `-0.4888`
- `news_risk_high->equity_24h` score `0.6453` n `99` status `ready` deltaP `29.8304` edge `1.0425` maxDD `-86.0244`
- `news_risk_high->equity_1h` score `0.4622` n `99` status `ready` deltaP `4.9568` edge `0.0882` maxDD `-1.9596`
- `news_risk_high->index_1h` score `0.2503` n `99` status `ready` deltaP `10.6817` edge `0.0066` maxDD `-0.3245`
- `news_risk_high->index_24h` score `-0.1383` n `99` status `ready` deltaP `3.9092` edge `0.1459` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.3004` n `99` status `ready` deltaP `0.2042` edge `0.0001` maxDD `-0.1984`
- `news_risk_high->metal_1h` score `-0.3218` n `99` status `ready` deltaP `-0.0937` edge `-0.0049` maxDD `-0.5256`
- `news_risk_high->crypto_major_4h` score `-0.3354` n `99` status `ready` deltaP `2.0864` edge `0.1117` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5351` n `99` status `ready` deltaP `2.3159` edge `0.1796` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6839` n `99` status `ready` deltaP `1.7404` edge `0.0235` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7621` n `99` status `ready` deltaP `-2.0664` edge `-0.003` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.8283` n `99` status `ready` deltaP `1.4782` edge `-0.0255` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-0.8787` n `99` status `ready` deltaP `-3.0107` edge `0.0013` maxDD `-4.1772`
- `news_risk_high->fx_24h` score `-1.6292` n `99` status `ready` deltaP `-12.3873` edge `0.0093` maxDD `-0.3321`
- `news_risk_high->metal_24h` score `-2.7937` n `99` status `ready` deltaP `5.1066` edge `-0.2026` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.3765` n `99` status `ready` deltaP `-19.3976` edge `-0.0154` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.0089` n `99` status `ready` deltaP `-27.4544` edge `-0.0237` maxDD `-8.1879`
- `news_risk_high->crypto_major_24h` score `-6.0184` n `99` status `ready` deltaP `-14.4706` edge `0.1752` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.8586` n `99` status `ready` deltaP `-24.8184` edge `-0.0145` maxDD `-33.9945`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
