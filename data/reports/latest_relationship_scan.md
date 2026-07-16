# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T12:22:26.032650+00:00`
- Price records: `672`
- Market context records: `6917`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1701` n `224` status `ready` deltaP `3.5848` edge `0.0028` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2089` n `201` status `ready` deltaP `-5.1208` edge `0.409` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3911` n `224` status `ready` deltaP `2.9593` edge `0.0241` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4831` n `224` status `ready` deltaP `4.4456` edge `0.0205` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6073` n `224` status `ready` deltaP `-0.5988` edge `-0.0054` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7347` n `224` status `ready` deltaP `-0.2807` edge `-0.0012` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7378` n `224` status `ready` deltaP `15.2222` edge `0.0103` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8074` n `224` status `ready` deltaP `-3.395` edge `-0.0041` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3947` n `224` status `ready` deltaP `-2.4935` edge `-0.0132` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5343` n `224` status `ready` deltaP `-2.3631` edge `-0.022` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.657` n `224` status `ready` deltaP `3.2827` edge `-0.0163` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8035` n `224` status `ready` deltaP `6.5331` edge `-0.0168` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.0882` n `224` status `ready` deltaP `3.6912` edge `0.006` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6596` n `224` status `ready` deltaP `2.5152` edge `0.0006` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7838` n `224` status `ready` deltaP `-0.0871` edge `-0.0236` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.8638` n `201` status `ready` deltaP `-2.5393` edge `-0.0349` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9293` n `224` status `ready` deltaP `-7.2082` edge `0.0405` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0488` n `201` status `ready` deltaP `-4.181` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.9177` n `224` status `ready` deltaP `3.9308` edge `-0.1186` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2023` n `201` status `ready` deltaP `-11.8558` edge `-0.1111` maxDD `-28.5814`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
