# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T11:52:26.347625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11019`

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

- `risk_on_high->unknown_4h` score `22.1133` n `142` status `ready` deltaP `7.096` edge `1.8573` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.1133` n `142` status `ready` deltaP `7.096` edge `1.8573` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.9172` n `228` status `ready` deltaP `7.5284` edge `0.9326` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.5023` n `37` status `ready` deltaP `25.1783` edge `0.4843` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.0343` n `37` status `ready` deltaP `22.0486` edge `0.1892` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6234` n `37` status `ready` deltaP `17.1803` edge `0.2287` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.2188` n `37` status `ready` deltaP `22.322` edge `0.0582` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `2.008` n `37` status `ready` deltaP `12.6483` edge `0.1031` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6099` n `37` status `ready` deltaP `13.3841` edge `0.084` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.1847` n `37` status `ready` deltaP `6.1661` edge `0.0759` maxDD `-0.4628`
- `news_risk_high->metal_1h` score `1.1843` n `37` status `ready` deltaP `14.1164` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1742` n `37` status `ready` deltaP `14.7233` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `0.953` n `37` status `ready` deltaP `16.2303` edge `0.2916` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.8974` n `37` status `ready` deltaP `8.7272` edge `0.0431` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.5939` n `37` status `ready` deltaP `6.3983` edge `0.0397` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.4561` n `37` status `ready` deltaP `14.5739` edge `0.0424` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.3004` n `124` status `ready` deltaP `21.2869` edge `0.771` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.3004` n `124` status `ready` deltaP `21.2869` edge `0.771` maxDD `-56.9519`
- `market_context_high->equity_24h` score `0.1666` n `192` status `ready` deltaP `15.7986` edge `0.3506` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1363` n `152` status `ready` deltaP `13.0673` edge `0.0016` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
