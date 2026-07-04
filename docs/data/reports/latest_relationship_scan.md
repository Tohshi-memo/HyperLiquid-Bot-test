# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T16:07:29.039055+00:00`
- Price records: `672`
- Market context records: `5679`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `1.9113` n `202` status `ready` deltaP `15.9551` edge `0.5608` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8963` n `252` status `ready` deltaP `11.6942` edge `0.2195` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4432` n `252` status `ready` deltaP `8.7665` edge `0.1595` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.1936` n `252` status `ready` deltaP `5.7443` edge `0.1417` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2476` n `264` status `ready` deltaP `2.2024` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4157` n `264` status `ready` deltaP `2.8375` edge `0.0426` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.4789` n `264` status `ready` deltaP `4.6181` edge `0.03` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.4899` n `264` status `ready` deltaP `0.7667` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.5828` n `264` status `ready` deltaP `1.0842` edge `0.0049` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.611` n `264` status `ready` deltaP `4.4751` edge `0.0438` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9334` n `264` status `ready` deltaP `0.3697` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9687` n `202` status `ready` deltaP `14.5111` edge `0.0479` maxDD `-3.0295`
- `market_context_high->fx_4h` score `-1.1706` n `252` status `ready` deltaP `3.9683` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.261` n `252` status `ready` deltaP `-0.3605` edge `0.0079` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4906` n `202` status `ready` deltaP `6.4734` edge `0.0374` maxDD `-16.9893`
- `market_context_high->metal_4h` score `-2.89` n `252` status `ready` deltaP `-11.9023` edge `-0.0536` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7797` n `252` status `ready` deltaP `-2.2986` edge `-0.0321` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.782` n `202` status `ready` deltaP `3.9896` edge `0.0206` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3224` n `202` status `ready` deltaP `-12.5567` edge `-0.2487` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.1301` n `202` status `ready` deltaP `-10.537` edge `-0.0797` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
