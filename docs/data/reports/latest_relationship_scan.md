# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T19:22:27.168579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9592` n `103` status `ready` deltaP `4.5729` edge `0.5221` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3978` n `103` status `ready` deltaP `12.2118` edge `0.176` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.542` n `104` status `ready` deltaP `14.7748` edge `0.0973` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0217` n `112` status `ready` deltaP `12.0509` edge `0.0391` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.9672` n `103` status `ready` deltaP `23.4847` edge `0.0541` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4081` n `103` status `ready` deltaP `9.1002` edge `0.1448` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5347` n `112` status `ready` deltaP `-3.4538` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.54` n `112` status `ready` deltaP `1.4917` edge `-0.0054` maxDD `-0.9639`
- `market_context_high->equity_1h` score `-0.6338` n `112` status `ready` deltaP `2.0157` edge `0.0166` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.6554` n `112` status `ready` deltaP `-4.2076` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.708` n `104` status `ready` deltaP `-2.8143` edge `-0.0115` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8508` n `104` status `ready` deltaP `1.4892` edge `-0.0055` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0287` n `104` status `ready` deltaP `-2.6853` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0749` n `112` status `ready` deltaP `-12.238` edge `-0.0284` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2042` n `104` status `ready` deltaP `0.3517` edge `-0.0523` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.6552` n `112` status `ready` deltaP `-8.6452` edge `-0.0571` maxDD `-5.189`
- `market_context_high->crypto_major_24h` score `-3.456` n `103` status `ready` deltaP `6.3933` edge `-0.0812` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.9046` n `103` status `ready` deltaP `-12.4461` edge `-0.0981` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.4548` n `104` status `ready` deltaP `-12.1716` edge `-0.1249` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0809` n `104` status `ready` deltaP `-14.9508` edge `-0.2346` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
