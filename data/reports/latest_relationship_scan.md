# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T01:07:38.340441+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `15.5105` n `88` status `ready` deltaP `16.7455` edge `1.1852` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5729` n `90` status `ready` deltaP `1.7479` edge `0.5523` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6186` n `90` status `ready` deltaP `17.5373` edge `0.1026` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.4626` n `88` status `ready` deltaP `3.488` edge `0.2811` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0789` n `88` status `ready` deltaP `25.9943` edge `0.0856` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3097` n `90` status `ready` deltaP `5.9414` edge `0.0278` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1159` n `90` status `ready` deltaP `7.1557` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0585` n `90` status `ready` deltaP `13.0048` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5418` n `90` status `ready` deltaP `-1.6068` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5993` n `90` status `ready` deltaP `-0.6054` edge `-0.0194` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-0.6008` n `88` status `ready` deltaP `7.2128` edge `0.0192` maxDD `-4.5445`
- `market_context_high->metal_4h` score `-0.6966` n `90` status `ready` deltaP `3.4891` edge `0.0109` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7258` n `90` status `ready` deltaP `-2.159` edge `-0.0076` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.1247` n `90` status `ready` deltaP `3.0284` edge `-0.0254` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.5956` n `88` status `ready` deltaP `-4.7664` edge `0.0467` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.7328` n `90` status `ready` deltaP `3.9022` edge `-0.0946` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1165` n `90` status `ready` deltaP `-12.4356` edge `-0.063` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3337` n `90` status `ready` deltaP `-10.9614` edge `-0.0674` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4024` n `90` status `ready` deltaP `2.0492` edge `-0.2525` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-7.2932` n `88` status `ready` deltaP `3.709` edge `-0.1636` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
