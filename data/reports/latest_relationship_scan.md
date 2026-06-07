# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T02:37:19.395279+00:00`
- Price records: `672`
- Market context records: `3136`
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

- `market_context_high->commodity_24h` score `14.3624` n `106` status `ready` deltaP `47.7594` edge `0.9213` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.8588` n `106` status `ready` deltaP `21.305` edge `0.895` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7394` n `106` status `ready` deltaP `10.0727` edge `2.3073` maxDD `-71.142`
- `market_context_high->index_24h` score `6.427` n `106` status `ready` deltaP `30.5293` edge `0.8759` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3029` n `106` status `ready` deltaP `10.8556` edge `1.3209` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0023` n `139` status `ready` deltaP `19.8138` edge `0.1639` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1223` n `146` status `ready` deltaP `3.8328` edge `0.0269` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4265` n `146` status `ready` deltaP `5.7563` edge `0.1199` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4645` n `106` status `ready` deltaP `5.3328` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.4797` n `146` status `ready` deltaP `4.0009` edge `0.0181` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8207` n `146` status `ready` deltaP `3.3385` edge `0.0211` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9608` n `146` status `ready` deltaP `3.2257` edge `0.0816` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1508` n `146` status `ready` deltaP `-11.0676` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2597` n `139` status `ready` deltaP `11.0415` edge `0.0558` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.524` n `139` status `ready` deltaP `-14.7296` edge `-0.0089` maxDD `-1.3966`
- `market_context_high->metal_1h` score `-2.0444` n `146` status `ready` deltaP `-4.1547` edge `-0.0033` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.0504` n `139` status `ready` deltaP `4.7487` edge `0.0197` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.3175` n `139` status `ready` deltaP `18.5055` edge `0.384` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0734` n `146` status `ready` deltaP `2.2086` edge `-0.0682` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.1116` n `139` status `ready` deltaP `12.0657` edge `0.0512` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
