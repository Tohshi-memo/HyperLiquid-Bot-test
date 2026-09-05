# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T04:07:28.162460+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10466`

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

- `risk_on_high->unknown_4h` score `19.4978` n `133` status `ready` deltaP `7.6265` edge `1.6358` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.4978` n `133` status `ready` deltaP `7.6265` edge `1.6358` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.0002` n `217` status `ready` deltaP `8.0631` edge `0.7658` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.366` n `37` status `ready` deltaP `25.0047` edge `0.4741` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3877` n `37` status `ready` deltaP `25.5208` edge `0.1955` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.852` n `37` status `ready` deltaP `17.6376` edge `0.2447` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1798` n `37` status `ready` deltaP `21.8647` edge `0.058` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8277` n `37` status `ready` deltaP `10.5142` edge `0.1023` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6578` n `37` status `ready` deltaP `13.8332` edge `0.085` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.3633` n `37` status `ready` deltaP `7.3637` edge `0.0828` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2604` n `37` status `ready` deltaP `15.7712` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1843` n `37` status `ready` deltaP `14.1164` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_4h` score `1.1466` n `37` status `ready` deltaP `8.8374` edge `0.0695` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `1.0725` n `37` status `ready` deltaP `9.4757` edge `0.0527` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.1534` n `37` status `ready` deltaP `11.7961` edge `0.0357` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.001` n `37` status `ready` deltaP `6.1742` edge `0.0036` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1723` n `133` status `ready` deltaP `3.8427` edge `-0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1723` n `133` status `ready` deltaP `3.8427` edge `-0.0032` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
