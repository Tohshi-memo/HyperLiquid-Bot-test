# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T08:07:22.074123+00:00`
- Price records: `672`
- Market context records: `3159`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8852`

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

- `market_context_high->commodity_24h` score `13.9338` n `106` status `ready` deltaP `47.3368` edge `0.8884` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1044` n `106` status `ready` deltaP `15.114` edge `2.4487` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.8235` n `106` status `ready` deltaP `21.4786` edge `0.8909` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.4075` n `106` status `ready` deltaP `30.5293` edge `0.8734` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8808` n `106` status `ready` deltaP `13.1649` edge `1.3796` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9155` n `139` status `ready` deltaP `18.6985` edge `0.1641` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.3157` n `106` status `ready` deltaP `10.2005` edge `0.0019` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.1622` n `139` status `ready` deltaP `3.9568` edge `0.0294` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3822` n `139` status `ready` deltaP `6.0236` edge `0.1238` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4697` n `139` status `ready` deltaP `4.435` edge `0.0165` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8978` n `139` status `ready` deltaP `3.1168` edge `0.0127` maxDD `-8.8863`
- `market_context_high->unknown_4h` score `-0.9981` n `139` status `ready` deltaP `9.0225` edge `0.0789` maxDD `-14.7778`
- `market_context_high->crypto_major_1h` score `-1.0558` n `139` status `ready` deltaP `2.3306` edge `0.0754` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.0647` n `139` status `ready` deltaP `13.4859` edge `0.0645` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.1335` n `139` status `ready` deltaP `-10.7645` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.411` n `139` status `ready` deltaP `-12.7237` edge `-0.0076` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.1163` n `139` status `ready` deltaP `-4.4684` edge `-0.0072` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.9108` n `139` status `ready` deltaP `13.7667` edge `0.0656` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9559` n `139` status `ready` deltaP `19.3587` edge `0.4291` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.3121` n `139` status `ready` deltaP `1.4744` edge `-0.0832` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
