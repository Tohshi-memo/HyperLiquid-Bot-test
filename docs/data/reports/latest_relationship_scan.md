# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T09:07:35.474420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2566`

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

- `market_context_high->unknown_1h` score `11490.1698` n `112` status `ready` deltaP `1.1175` edge `957.5265` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7252.4579` n `110` status `ready` deltaP `0.1968` edge `604.3986` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.3904` n `98` status `ready` deltaP `39.594` edge `1.6516` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.506` n `98` status `ready` deltaP `22.1833` edge `1.4114` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2451` n `112` status `ready` deltaP `3.2934` edge `0.0131` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2552` n `110` status `ready` deltaP `13.8664` edge `0.0173` maxDD `-6.1475`
- `market_context_high->metal_24h` score `-0.2941` n `98` status `ready` deltaP `15.3557` edge `0.1956` maxDD `-15.7982`
- `market_context_high->crypto_major_4h` score `-0.3568` n `110` status `ready` deltaP `1.0947` edge `0.3052` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.6089` n `110` status `ready` deltaP `1.5521` edge `0.1926` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8178` n `112` status `ready` deltaP `2.6946` edge `0.0639` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8307` n `112` status `ready` deltaP `-1.62` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0634` n `112` status `ready` deltaP `-1.9247` edge `0.0268` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3925` n `112` status `ready` deltaP `-9.0516` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.0132` n `110` status `ready` deltaP `-4.5343` edge `-0.0032` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5043` n `112` status `ready` deltaP `-11.142` edge `-0.0266` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.76` n `112` status `ready` deltaP `1.358` edge `-0.0213` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-3.7943` n `110` status `ready` deltaP `-16.1391` edge `-0.0043` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6775` n `98` status `ready` deltaP `-18.293` edge `-0.0036` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3151` n `110` status `ready` deltaP `-22.9933` edge `-0.0969` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1563` n `98` status `ready` deltaP `-16.7694` edge `-0.109` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
