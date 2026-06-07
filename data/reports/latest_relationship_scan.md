# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T09:07:24.671332+00:00`
- Price records: `672`
- Market context records: `3163`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.7681` n `102` status `ready` deltaP `47.1405` edge `0.8759` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0771` n `102` status `ready` deltaP `15.7884` edge `2.4407` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7502` n `102` status `ready` deltaP `20.5167` edge `0.8912` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.2507` n `102` status `ready` deltaP `29.4934` edge `0.8602` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.82` n `102` status `ready` deltaP `14.2463` edge `1.3646` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9535` n `135` status `ready` deltaP `18.4982` edge `0.1686` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.732` n `102` status `ready` deltaP `12.7247` edge `0.0031` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2525` n `135` status `ready` deltaP `4.8148` edge `0.0312` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4054` n `135` status `ready` deltaP `6.0124` edge `0.1209` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4133` n `135` status `ready` deltaP `5.4136` edge `0.0172` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.5523` n `135` status `ready` deltaP `10.3952` edge `0.1069` maxDD `-14.7778`
- `market_context_high->equity_1h` score `-0.8678` n `135` status `ready` deltaP `3.7824` edge `0.0121` maxDD `-8.8863`
- `market_context_high->index_4h` score `-0.9854` n `135` status `ready` deltaP `14.8159` edge `0.0658` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0409` n `135` status `ready` deltaP `3.096` edge `0.0722` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0848` n `135` status `ready` deltaP `-9.827` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.3713` n `135` status `ready` deltaP `-12.0054` edge `-0.0073` maxDD `-1.4115`
- `market_context_high->crypto_alt_4h` score `-2.0358` n `135` status `ready` deltaP `18.7319` edge `0.4186` maxDD `-58.6918`
- `market_context_high->metal_1h` score `-2.077` n `135` status `ready` deltaP `-3.7669` edge `-0.0086` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.924` n `135` status `ready` deltaP `14.4444` edge `0.0594` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.0404` n `135` status `ready` deltaP `2.546` edge `-0.0677` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
