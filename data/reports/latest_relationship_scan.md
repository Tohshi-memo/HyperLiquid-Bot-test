# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T19:07:31.807389+00:00`
- Price records: `672`
- Market context records: `7593`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->commodity_24h` score `0.2701` n `145` status `ready` deltaP `14.8432` edge `0.0819` maxDD `-7.0012`
- `market_context_high->unknown_24h` score `0.2212` n `146` status `ready` deltaP `11.7532` edge `0.111` maxDD `-6.5466`
- `market_context_high->index_1h` score `0.0272` n `151` status `ready` deltaP `6.1333` edge `0.011` maxDD `-0.8721`
- `market_context_high->commodity_4h` score `-0.0039` n `151` status `ready` deltaP `8.1718` edge `0.0212` maxDD `-2.4139`
- `market_context_high->commodity_1h` score `-0.261` n `151` status `ready` deltaP `4.9748` edge `0.0023` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.3431` n `145` status `ready` deltaP `9.2803` edge `0.0183` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.4293` n `151` status `ready` deltaP `0.7802` edge `0.0129` maxDD `-3.5174`
- `market_context_high->crypto_major_1h` score `-0.4355` n `151` status `ready` deltaP `6.6542` edge `0.0129` maxDD `-5.3808`
- `market_context_high->equity_1h` score `-0.602` n `151` status `ready` deltaP `5.9215` edge `0.0501` maxDD `-8.6735`
- `market_context_high->metal_1h` score `-0.6338` n `151` status `ready` deltaP `1.4246` edge `0.0138` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6641` n `151` status `ready` deltaP `8.7885` edge `0.0289` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.7068` n `151` status `ready` deltaP `-1.0898` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->equity_24h` score `-0.9649` n `145` status `ready` deltaP `16.9771` edge `0.4983` maxDD `-52.8144`
- `market_context_high->crypto_alt_4h` score `-1.177` n `151` status `ready` deltaP `1.6556` edge `0.0466` maxDD `-10.0162`
- `market_context_high->crypto_major_4h` score `-1.441` n `151` status `ready` deltaP `7.1586` edge `0.0554` maxDD `-16.0298`
- `market_context_high->unknown_1h` score `-1.448` n `151` status `ready` deltaP `0.2677` edge `-0.0601` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7097` n `151` status `ready` deltaP `-2.0706` edge `0.0428` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.7273` n `151` status `ready` deltaP `2.2683` edge `0.2` maxDD `-21.9254`
- `market_context_high->fx_4h` score `-2.4332` n `151` status `ready` deltaP `-4.6054` edge `-0.0036` maxDD `-2.1439`
- `market_context_high->metal_24h` score `-2.447` n `146` status `ready` deltaP `-2.5352` edge `0.1003` maxDD `-11.4363`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
