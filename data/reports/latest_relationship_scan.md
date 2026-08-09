# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T02:52:28.141393+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.354` n `103` status `ready` deltaP `4.5729` edge `0.555` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6503` n `103` status `ready` deltaP `13.2535` edge `0.1901` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4345` n `125` status `ready` deltaP `14.5707` edge `0.0897` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9001` n `137` status `ready` deltaP `11.1456` edge `0.035` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8384` n `103` status `ready` deltaP `21.9222` edge `0.048` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5041` n `103` status `ready` deltaP `9.1002` edge `0.1571` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3535` n `137` status `ready` deltaP `3.5841` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3946` n `125` status `ready` deltaP `6.8012` edge `-0.0029` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.5849` n `125` status `ready` deltaP `-0.2512` edge `-0.0128` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6658` n `137` status `ready` deltaP `-4.3315` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.8117` n `137` status `ready` deltaP `-3.3021` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9007` n `137` status `ready` deltaP `0.4796` edge `0.0046` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9996` n `125` status `ready` deltaP `-1.5098` edge `-0.0172` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0583` n `137` status `ready` deltaP `-11.3313` edge `-0.0318` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4589` n `125` status `ready` deltaP `-0.1768` edge `-0.07` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.188` n `137` status `ready` deltaP `-10.7894` edge `-0.0648` maxDD `-6.9815`
- `market_context_high->crypto_major_24h` score `-3.5635` n `103` status `ready` deltaP `6.2197` edge `-0.089` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4926` n `103` status `ready` deltaP `-12.4461` edge `-0.1471` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.5245` n `125` status `ready` deltaP `-11.5646` edge `-0.1343` maxDD `-6.585`
- `market_context_high->unknown_1h` score `-8.2852` n `137` status `ready` deltaP `-5.3433` edge `-0.6101` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
