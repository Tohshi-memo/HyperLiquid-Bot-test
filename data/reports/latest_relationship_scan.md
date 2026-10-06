# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T06:52:35.504977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9400`

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

- `news_risk_high->crypto_major_4h` score `9.623` n `64` status `ready` deltaP `33.6509` edge `0.5979` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0752` n `64` status `ready` deltaP `20.846` edge `0.5017` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `4.4385` n `101` status `ready` deltaP `12.975` edge `0.4191` maxDD `-6.8577`
- `news_risk_high->equity_24h` score `3.6975` n `64` status `ready` deltaP `10.9321` edge `0.2452` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.258` n `64` status `ready` deltaP `22.6804` edge `0.1203` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6071` n `64` status `ready` deltaP `29.154` edge `0.0491` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.6036` n `117` status `ready` deltaP `13.2583` edge `0.225` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.369` n `64` status `ready` deltaP `9.1879` edge `0.1717` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `1.9369` n `64` status `ready` deltaP `17.4162` edge `0.1051` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.862` n `64` status `ready` deltaP `23.3346` edge `0.0146` maxDD `-0.1997`
- `market_context_high->fx_4h` score `1.2963` n `117` status `ready` deltaP `23.9238` edge `0.0242` maxDD `-0.3868`
- `news_risk_high->metal_4h` score `1.2122` n `64` status `ready` deltaP `17.6829` edge `0.0791` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.2053` n `117` status `ready` deltaP `16.2967` edge `0.0618` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1212` n `64` status `ready` deltaP `3.7706` edge `0.1202` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9312` n `117` status `ready` deltaP `14.9381` edge `0.0064` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7873` n `117` status `ready` deltaP `12.5045` edge `0.0219` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2523` n `117` status `ready` deltaP `-0.7218` edge `0.1982` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.251` n `101` status `ready` deltaP `16.6309` edge `0.0588` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.1799` n `64` status `ready` deltaP `24.6402` edge `0.0467` maxDD `-10.0322`
- `news_risk_high->metal_1h` score `0.0454` n `64` status `ready` deltaP `5.567` edge `0.0085` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
