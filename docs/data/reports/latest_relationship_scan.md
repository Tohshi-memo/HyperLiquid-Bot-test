# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T01:37:20.755742+00:00`
- Price records: `672`
- Market context records: `1996`
- Flow alert records: `7636`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.4595` n `223` status `ready` deltaP `29.6784` edge `0.5601` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.9176` n `223` status `ready` deltaP `23.8755` edge `0.6151` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `4.7298` n `223` status `ready` deltaP `16.7006` edge `0.3747` maxDD `-4.0178`
- `market_context_high->equity_4h` score `2.4885` n `223` status `ready` deltaP `15.1687` edge `0.2157` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.3739` n `188` status `ready` deltaP `15.9101` edge `0.6238` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.7075` n `188` status `ready` deltaP `16.799` edge `0.2729` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.1813` n `188` status `ready` deltaP `14.7734` edge `0.4898` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1668` n `223` status `ready` deltaP `10.3877` edge `0.1266` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.9144` n `223` status `ready` deltaP `8.4403` edge `0.1313` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.7828` n `223` status `ready` deltaP `8.7383` edge `0.0772` maxDD `-1.9508`
- `market_context_high->fx_24h` score `0.6011` n `188` status `ready` deltaP `14.9446` edge `0.0279` maxDD `-1.1952`
- `market_context_high->crypto_major_24h` score `0.5629` n `188` status `ready` deltaP `20.2784` edge `0.7703` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.1675` n `188` status `ready` deltaP `3.0749` edge `0.1163` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1577` n `223` status `ready` deltaP `4.2447` edge `0.0374` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.599` n `223` status `ready` deltaP `-2.0199` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7117` n `223` status `ready` deltaP `-0.686` edge `0.0074` maxDD `-1.6378`
- `market_context_high->metal_1h` score `-0.9682` n `223` status `ready` deltaP `1.5675` edge `-0.001` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.975` n `223` status `ready` deltaP `2.0119` edge `-0.0227` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-1.1503` n `223` status `ready` deltaP `-8.4203` edge `-0.0032` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8817` n `223` status `ready` deltaP `2.0186` edge `0.0011` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
