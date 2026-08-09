# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T17:37:26.340950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10842`

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

- `market_context_high->equity_24h` score `2.5731` n `109` status `ready` deltaP `3.4515` edge `0.4974` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.9546` n `109` status `ready` deltaP `8.4862` edge `0.1639` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3186` n `143` status `ready` deltaP `16.2716` edge `0.0687` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8792` n `143` status `ready` deltaP `11.7395` edge `0.0293` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6166` n `109` status `ready` deltaP `20.2217` edge `0.0309` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.2551` n `109` status `ready` deltaP `6.0827` edge `0.1453` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4067` n `143` status `ready` deltaP `2.948` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4486` n `143` status `ready` deltaP `-1.9921` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.6368` n `143` status `ready` deltaP `3.9986` edge `-0.0044` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6986` n `143` status `ready` deltaP `-5.0374` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9622` n `143` status `ready` deltaP `-1.5254` edge `-0.0095` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.978` n `143` status `ready` deltaP `-0.7862` edge `0.0066` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0279` n `143` status `ready` deltaP `-1.9657` edge `-0.0178` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0667` n `143` status `ready` deltaP `-11.3312` edge `-0.0325` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.625` n `143` status `ready` deltaP `-2.0286` edge `-0.0715` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.358` n `143` status `ready` deltaP `-12.4838` edge `-0.0644` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-4.0077` n `143` status `ready` deltaP `-8.7338` edge `-0.1101` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.2575` n `109` status `ready` deltaP `1.5195` edge `-0.1155` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.2357` n `109` status `ready` deltaP `-17.6` edge `-0.258` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8292` n `143` status `ready` deltaP `-6.2435` edge `-0.5661` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
