# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T11:52:26.151879+00:00`
- Price records: `672`
- Market context records: `7561`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `-0.075` n `176` status `ready` deltaP `7.1935` edge `0.0218` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1294` n `176` status `ready` deltaP `5.3081` edge `0.0076` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.3091` n `176` status `ready` deltaP `3.5063` edge `0.0008` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.3483` n `176` status `ready` deltaP `3.29` edge `0.0114` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.3565` n `176` status `ready` deltaP `12.4307` edge `0.1073` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.4363` n `176` status `ready` deltaP `2.9791` edge `0.001` maxDD `-1.5775`
- `market_context_high->commodity_24h` score `-0.585` n `153` status `ready` deltaP `10.4848` edge `0.0397` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `-0.5998` n `176` status `ready` deltaP `0.8676` edge `0.0212` maxDD `-5.9775`
- `market_context_high->fx_24h` score `-0.6239` n `153` status `ready` deltaP `11.3457` edge `0.0164` maxDD `-3.8554`
- `market_context_high->index_4h` score `-0.9499` n `176` status `ready` deltaP `9.0023` edge `0.0208` maxDD `-5.874`
- `market_context_high->crypto_major_1h` score `-0.9631` n `176` status `ready` deltaP `5.2327` edge `0.0259` maxDD `-7.6171`
- `market_context_high->metal_1h` score `-0.996` n `176` status `ready` deltaP `1.8576` edge `0.015` maxDD `-1.4971`
- `market_context_high->fx_4h` score `-1.2149` n `176` status `ready` deltaP `1.1555` edge `0.005` maxDD `-2.1439`
- `market_context_high->metal_4h` score `-1.448` n `176` status `ready` deltaP `1.9124` edge `0.0498` maxDD `-4.8549`
- `market_context_high->equity_1h` score `-1.4816` n `176` status `ready` deltaP `3.7538` edge `0.0261` maxDD `-14.6193`
- `market_context_high->crypto_alt_4h` score `-1.7132` n `176` status `ready` deltaP `1.5244` edge `0.0445` maxDD `-15.2776`
- `market_context_high->unknown_24h` score `-1.7851` n `154` status `ready` deltaP `3.5602` edge `0.0223` maxDD `-9.9917`
- `market_context_high->crypto_major_4h` score `-2.3014` n `176` status `ready` deltaP `5.3077` edge `0.059` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-4.1658` n `176` status `ready` deltaP `1.2441` edge `0.1251` maxDD `-40.3975`
- `market_context_high->index_24h` score `-4.6683` n `153` status `ready` deltaP `-19.7604` edge `-0.0209` maxDD `-20.3362`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
