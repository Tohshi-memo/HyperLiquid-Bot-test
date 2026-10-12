# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T18:52:33.202228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `7.5257` n `61` status `ready` deltaP `26.0673` edge `1.2392` maxDD `-29.8524`
- `risk_on_high->crypto_alt_4h` score `4.4992` n `48` status `ready` deltaP `19.4106` edge `0.2903` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.4992` n `48` status `ready` deltaP `19.4106` edge `0.2903` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.8033` n `48` status `ready` deltaP `34.0447` edge `0.3459` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8033` n `48` status `ready` deltaP `34.0447` edge `0.3459` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.7973` n `100` status `ready` deltaP `14.4939` edge `0.3647` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.4606` n `100` status `ready` deltaP `17.878` edge `0.3251` maxDD `-7.4722`
- `market_context_high->crypto_alt_24h` score `3.2941` n `61` status `ready` deltaP `14.0881` edge `0.9647` maxDD `-44.5707`
- `market_context_high->crypto_alt_1h` score `1.6029` n `100` status `ready` deltaP `12.0539` edge `0.1483` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9815` n `48` status `ready` deltaP `6.3872` edge `0.0989` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9815` n `48` status `ready` deltaP `6.3872` edge `0.0989` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.9409` n `100` status `ready` deltaP `-3.7744` edge `0.1682` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.6992` n `100` status `ready` deltaP `4.497` edge `0.1046` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4428` n `48` status `ready` deltaP `5.6637` edge `0.0843` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4428` n `48` status `ready` deltaP `5.6637` edge `0.0843` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0344` n `100` status `ready` deltaP `5.0511` edge `0.0038` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1357` n `100` status `ready` deltaP `6.1018` edge `0.0041` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.269` n `100` status `ready` deltaP `9.372` edge `0.0104` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3183` n `48` status `ready` deltaP `3.2685` edge `0.0036` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3183` n `48` status `ready` deltaP `3.2685` edge `0.0036` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
