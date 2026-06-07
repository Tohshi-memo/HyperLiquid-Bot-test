# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T17:01:06.824016+00:00`
- Price records: `672`
- Market context records: `3198`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10001`

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

- `market_context_high->crypto_alt_24h` score `17.5508` n `100` status `ready` deltaP `13.8264` edge `2.368` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.4476` n `100` status `ready` deltaP `46.9444` edge `0.8505` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.2003` n `100` status `ready` deltaP `28.9444` edge `0.8574` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6599` n `100` status `ready` deltaP `13.3264` edge `1.3502` maxDD `-53.663`
- `market_context_high->unknown_24h` score `4.2847` n `100` status `ready` deltaP `17.1319` edge `0.6784` maxDD `-17.4635`
- `market_context_high->commodity_4h` score `3.3643` n `132` status `ready` deltaP `21.8034` edge `0.1808` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.938` n `100` status `ready` deltaP `14.4792` edge `0.0044` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5637` n `132` status `ready` deltaP `11.4745` edge `0.1927` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.45` n `135` status `ready` deltaP `7.179` edge `0.0319` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4176` n `135` status `ready` deltaP `5.4214` edge `0.0166` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6485` n `135` status `ready` deltaP `6.7532` edge `0.1139` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7627` n `135` status `ready` deltaP `5.2639` edge `0.0157` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9962` n `135` status `ready` deltaP `3.8367` edge `0.073` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2422` n `132` status `ready` deltaP `-9.6868` edge `-0.0062` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.3159` n `132` status `ready` deltaP `16.3571` edge `0.0722` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7194` n `135` status `ready` deltaP `-10.4258` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0255` n `135` status `ready` deltaP `-3.1836` edge `-0.0082` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.6402` n `132` status `ready` deltaP `15.3594` edge `0.3636` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.8232` n `135` status `ready` deltaP `2.3963` edge `-0.0486` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.8773` n `132` status `ready` deltaP `9.3265` edge `0.2331` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
