# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T11:07:43.044091+00:00`
- Price records: `672`
- Market context records: `6080`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.0187` n `30` status `ready` deltaP `31.1805` edge `0.2251` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3455` n `32` status `ready` deltaP `45.1982` edge `0.0654` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.491` edge `0.0222` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.8372` n `205` status `ready` deltaP `9.5427` edge `0.1812` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1419` n `32` status `ready` deltaP `13.2298` edge `0.1049` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.8095` n `30` status `ready` deltaP `19.3056` edge `-0.0407` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6408` n `32` status `ready` deltaP `9.0756` edge `0.0678` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1008` n `30` status `ready` deltaP `9.2361` edge `0.0385` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.335` n `205` status `ready` deltaP `3.9631` edge `0.0105` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4824` n `205` status `ready` deltaP `0.8325` edge `-0.0005` maxDD `-0.6202`
- `market_context_high->equity_1h` score `-0.5285` n `205` status `ready` deltaP `1.9344` edge `0.0309` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.6105` n `205` status `ready` deltaP `5.3658` edge `0.0321` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7155` n `32` status `ready` deltaP `-1.6467` edge `-0.031` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7519` n `205` status `ready` deltaP `4.8226` edge `0.0467` maxDD `-9.3536`
- `market_context_high->commodity_1h` score `-0.7631` n `205` status `ready` deltaP `-2.079` edge `-0.0051` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8187` n `205` status `ready` deltaP `4.678` edge `0.0406` maxDD `-9.807`
- `market_context_high->index_4h` score `-0.8415` n `205` status `ready` deltaP `2.5305` edge `0.0261` maxDD `-1.7348`
- `news_risk_high->index_1h` score `-0.9598` n `32` status `ready` deltaP `-7.5786` edge `-0.0162` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1693` n `205` status `ready` deltaP `-1.8621` edge `0.0044` maxDD `-1.1543`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
