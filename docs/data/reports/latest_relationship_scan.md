# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T01:28:39.916369+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6231`

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

- `market_context_high->unknown_24h` score `4391.7885` n `77` status `ready` deltaP `-9.765` edge `366.0849` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `174.285` n `77` status `ready` deltaP `1.2809` edge `14.5285` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.4764` n `108` status `ready` deltaP `-5.1951` edge `6.4363` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7853` n `92` status `ready` deltaP `35.0921` edge `1.1155` maxDD `-6.3871`
- `market_context_high->equity_24h` score `11.6034` n `77` status `ready` deltaP `22.2132` edge `1.0733` maxDD `-13.0219`
- `market_context_high->unknown_1h` score `7.4491` n `77` status `ready` deltaP `4.2325` edge `0.6036` maxDD `-0.2178`
- `news_risk_high->crypto_alt_4h` score `5.5222` n `108` status `ready` deltaP `20.8841` edge `0.4596` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.287` n `77` status `ready` deltaP `46.2144` edge `0.1508` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.5295` n `77` status `ready` deltaP `25.3188` edge `0.0754` maxDD `-0.3387`
- `market_context_high->fx_1h` score `0.898` n `77` status `ready` deltaP `13.9883` edge `0.0` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8553` n `108` status `ready` deltaP `8.8767` edge `0.1075` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.7301` n `77` status `ready` deltaP `14.0086` edge `0.0427` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.6561` n `77` status `ready` deltaP `9.5381` edge `0.0201` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.6131` n `77` status `ready` deltaP `13.185` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.1778` n `77` status `ready` deltaP `-0.0506` edge `0.1107` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1575` n `77` status `ready` deltaP `-5.082` edge `0.1934` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.1528` n `77` status `ready` deltaP `2.5469` edge `0.0662` maxDD `-5.2213`
- `market_context_high->commodity_24h` score `-0.173` n `77` status `ready` deltaP `23.4556` edge `0.0784` maxDD `-13.2226`
- `market_context_high->commodity_1h` score `-0.3438` n `77` status `ready` deltaP `0.7465` edge `0.0178` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4398` n `77` status `ready` deltaP `-0.35` edge `0.0018` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
