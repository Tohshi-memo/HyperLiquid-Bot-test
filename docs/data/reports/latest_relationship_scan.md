# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T02:07:28.279428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.4349` n `158` status `ready` deltaP `15.925` edge `0.0807` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8779` n `170` status `ready` deltaP `11.423` edge `0.0313` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.513` n `137` status `ready` deltaP `18.9959` edge `0.0226` maxDD `-1.678`
- `market_context_high->fx_1h` score `-0.2056` n `170` status `ready` deltaP `3.658` edge `-0.0012` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2881` n `158` status `ready` deltaP `5.3913` edge `0.0024` maxDD `-1.6892`
- `market_context_high->index_1h` score `-0.5685` n `170` status `ready` deltaP `-3.0257` edge `-0.005` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.5763` n `137` status `ready` deltaP `2.2975` edge `0.0898` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.8223` n `170` status `ready` deltaP `-2.1151` edge `-0.0043` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.8513` n `170` status `ready` deltaP `-5.0898` edge `-0.0116` maxDD `-2.0884`
- `market_context_high->index_4h` score `-0.8804` n `158` status `ready` deltaP `-3.5891` edge `-0.0107` maxDD `-1.26`
- `market_context_high->metal_24h` score `-0.9524` n `137` status `ready` deltaP `-2.7689` edge `0.0375` maxDD `-2.2056`
- `market_context_high->equity_24h` score `-1.1879` n `137` status `ready` deltaP `-0.8554` edge `0.2127` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.541` n `170` status `ready` deltaP `-8.6615` edge `-0.0377` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.6104` n `158` status `ready` deltaP `-6.0647` edge `-0.0326` maxDD `-5.3415`
- `market_context_high->crypto_major_1h` score `-2.3672` n `170` status `ready` deltaP `-10.4702` edge `-0.0603` maxDD `-10.5372`
- `market_context_high->equity_4h` score `-3.5175` n `158` status `ready` deltaP `-6.0647` edge `-0.0898` maxDD `-7.6983`
- `market_context_high->crypto_alt_24h` score `-4.3769` n `137` status `ready` deltaP `-11.3152` edge `-0.145` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.6949` n `137` status `ready` deltaP `-1.143` edge `-0.1342` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-5.8855` n `158` status `ready` deltaP `-12.0524` edge `-0.1587` maxDD `-13.4458`
- `market_context_high->unknown_1h` score `-7.5801` n `170` status `ready` deltaP `-5.0053` edge `-0.5526` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
