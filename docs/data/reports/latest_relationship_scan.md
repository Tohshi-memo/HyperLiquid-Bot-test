# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T05:07:27.075247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.7035` n `98` status `ready` deltaP `30.1411` edge `0.964` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7035` n `98` status `ready` deltaP `30.1411` edge `0.964` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.6956` n `220` status `ready` deltaP `22.5158` edge `0.7406` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.3015` n `98` status `ready` deltaP `37.4285` edge `0.3961` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.3015` n `98` status `ready` deltaP `37.4285` edge `0.3961` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.1728` n `98` status `ready` deltaP `26.2848` edge `0.3417` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1728` n `98` status `ready` deltaP `26.2848` edge `0.3417` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.0713` n `98` status `ready` deltaP `21.1876` edge `0.9157` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0713` n `98` status `ready` deltaP `21.1876` edge `0.9157` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9635` n `98` status `ready` deltaP `30.793` edge `0.0459` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9635` n `98` status `ready` deltaP `30.793` edge `0.0459` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6854` n `220` status `ready` deltaP `14.7569` edge `0.1254` maxDD `0.0`
- `market_context_high->index_24h` score `2.3591` n `220` status `ready` deltaP `25.6724` edge `0.0648` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.3004` n `98` status `ready` deltaP `5.8353` edge `0.1047` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.3004` n `98` status `ready` deltaP `5.8353` edge `0.1047` maxDD `-1.1521`
- `risk_on_high->commodity_24h` score `1.2315` n `98` status `ready` deltaP `12.624` edge `0.0379` maxDD `-0.2216`
- `risk_on_and_context->commodity_24h` score `1.2315` n `98` status `ready` deltaP `12.624` edge `0.0379` maxDD `-0.2216`
- `risk_on_high->equity_4h` score `1.2268` n `98` status `ready` deltaP `22.1596` edge `-0.0114` maxDD `-1.0611`
- `risk_on_and_context->equity_4h` score `1.2268` n `98` status `ready` deltaP `22.1596` edge `-0.0114` maxDD `-1.0611`
- `risk_on_high->equity_1h` score `1.1188` n `98` status `ready` deltaP `16.9773` edge `0.0079` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
