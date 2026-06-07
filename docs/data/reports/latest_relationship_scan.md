# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T02:52:25.659885+00:00`
- Price records: `672`
- Market context records: `3137`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7126`

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

- `market_context_high->commodity_24h` score `14.3955` n `106` status `ready` deltaP `47.933` edge `0.9229` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9099` n `106` status `ready` deltaP `21.4786` edge `0.8981` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7472` n `106` status `ready` deltaP `10.0727` edge `2.3083` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4278` n `106` status `ready` deltaP `30.5293` edge `0.876` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.2896` n `106` status `ready` deltaP `10.8556` edge `1.3192` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9489` n `140` status `ready` deltaP `19.4164` edge `0.1621` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1223` n `146` status `ready` deltaP `3.8328` edge `0.0269` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4094` n `146` status `ready` deltaP `5.906` edge `0.1211` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4645` n `106` status `ready` deltaP `5.3328` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.472` n `146` status `ready` deltaP `4.1506` edge `0.0181` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8114` n `146` status `ready` deltaP `3.4882` edge `0.0213` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9492` n `146` status `ready` deltaP `3.3754` edge `0.0821` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1431` n `146` status `ready` deltaP `-10.9179` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2379` n `140` status `ready` deltaP `11.3241` edge `0.0567` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5281` n `140` status `ready` deltaP `-14.8083` edge `-0.0088` maxDD `-1.404`
- `market_context_high->unknown_4h` score `-2.0116` n `140` status `ready` deltaP `4.8737` edge `0.0221` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0456` n `146` status `ready` deltaP `-4.1547` edge `-0.0034` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2128` n `140` status `ready` deltaP `18.8241` edge `0.3953` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.0551` n `140` status `ready` deltaP `12.3432` edge `0.0566` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.0746` n `146` status `ready` deltaP `2.2086` edge `-0.0683` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
