# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T16:52:23.456245+00:00`
- Price records: `672`
- Market context records: `3197`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->crypto_alt_24h` score `17.8787` n `101` status `ready` deltaP `14.4304` edge `2.3913` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.4568` n `101` status `ready` deltaP `47.0434` edge `0.8506` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `6.8325` n `101` status `ready` deltaP `17.2751` edge `0.6975` maxDD `-17.4635`
- `market_context_high->index_24h` score `6.2202` n `101` status `ready` deltaP `29.2216` edge `0.8581` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.7467` n `101` status `ready` deltaP `13.8115` edge `1.3581` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3138` n `133` status `ready` deltaP `21.3976` edge `0.1793` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.9296` n `101` status `ready` deltaP `14.4046` edge `0.0042` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6044` n `133` status `ready` deltaP `11.7138` edge `0.1945` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.4572` n `135` status `ready` deltaP `7.179` edge `0.0325` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4051` n `135` status `ready` deltaP `6.7532` edge `0.116` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4199` n `135` status `ready` deltaP `5.4214` edge `0.0163` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.7698` n `135` status `ready` deltaP `5.2639` edge `0.0148` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9985` n `135` status `ready` deltaP `3.8367` edge `0.0727` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2589` n `133` status `ready` deltaP `-9.9773` edge `-0.0064` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.2831` n `133` status `ready` deltaP `16.6021` edge `0.0733` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7194` n `135` status `ready` deltaP `-10.4258` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0836` n `135` status `ready` deltaP `-3.7747` edge `-0.0091` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.5583` n `133` status `ready` deltaP `15.6898` edge `0.3719` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2316` n `135` status `ready` deltaP `1.8053` edge `-0.0787` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.8053` n `133` status `ready` deltaP `9.7367` edge `0.2396` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
