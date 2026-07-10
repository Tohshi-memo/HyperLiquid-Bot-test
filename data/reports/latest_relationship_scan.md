# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T10:22:26.420374+00:00`
- Price records: `672`
- Market context records: `6274`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11084`

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

- `news_risk_high->crypto_alt_24h` score `15.1489` n `32` status `ready` deltaP `43.058` edge `0.9901` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9471` n `32` status `ready` deltaP `50.519` edge `0.1588` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2073` n `32` status `ready` deltaP `44.1311` edge `0.061` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0098` n `32` status `ready` deltaP `16.4901` edge `0.4821` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.5044` n `32` status `ready` deltaP `25.5515` edge `0.0589` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3092` n `32` status `ready` deltaP `27.8443` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8398` n `204` status `ready` deltaP `2.36` edge `0.2384` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3151` n `32` status `ready` deltaP `13.5292` edge `0.1251` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2725` n `192` status `ready` deltaP `-1.3847` edge `0.3685` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7873` n `32` status `ready` deltaP `10.5726` edge `0.0766` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0323` n `192` status `ready` deltaP `5.7165` edge `0.0563` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1902` n `32` status `ready` deltaP `8.8452` edge `0.0038` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.308` n `204` status `ready` deltaP `0.8835` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3915` n `192` status `ready` deltaP `16.4775` edge `0.0968` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4275` n `192` status `ready` deltaP `5.1957` edge `0.0293` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.569` n `204` status `ready` deltaP `-0.5988` edge `0.0026` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.6686` n `32` status `ready` deltaP `-1.9461` edge `-0.023` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7001` n `204` status `ready` deltaP `7.08` edge `0.0383` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8152` n `204` status `ready` deltaP `5.2571` edge `0.0372` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.8196` n `204` status `ready` deltaP `1.9755` edge `-0.0016` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
