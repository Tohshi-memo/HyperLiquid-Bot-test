# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T14:52:25.531907+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9959`

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

- `risk_on_high->unknown_24h` score `103.3694` n `110` status `ready` deltaP `23.9267` edge `8.4656` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `103.3694` n `110` status `ready` deltaP `23.9267` edge `8.4656` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `10.1121` n `110` status `ready` deltaP `23.1471` edge `1.1436` maxDD `-29.0855`
- `risk_on_and_context->crypto_major_24h` score `10.1121` n `110` status `ready` deltaP `23.1471` edge `1.1436` maxDD `-29.0855`
- `market_context_high->equity_24h` score `2.9078` n `196` status `ready` deltaP `15.6852` edge `0.3548` maxDD `-10.031`
- `risk_on_high->crypto_alt_24h` score `1.7868` n `110` status `ready` deltaP `11.433` edge `0.4961` maxDD `-25.5404`
- `risk_on_and_context->crypto_alt_24h` score `1.7868` n `110` status `ready` deltaP `11.433` edge `0.4961` maxDD `-25.5404`
- `market_context_high->crypto_alt_24h` score `0.6011` n `196` status `ready` deltaP `14.151` edge `0.4045` maxDD `-26.8998`
- `risk_on_high->equity_24h` score `0.2881` n `110` status `ready` deltaP `6.9097` edge `0.195` maxDD `-10.031`
- `risk_on_and_context->equity_24h` score `0.2881` n `110` status `ready` deltaP `6.9097` edge `0.195` maxDD `-10.031`
- `risk_on_high->index_1h` score `-0.0681` n `135` status `ready` deltaP `5.8317` edge `-0.0029` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0681` n `135` status `ready` deltaP `5.8317` edge `-0.0029` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1755` n `135` status `ready` deltaP `2.9796` edge `0.0672` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1755` n `135` status `ready` deltaP `2.9796` edge `0.0672` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.2068` n `135` status `ready` deltaP `6.9184` edge `-0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2068` n `135` status `ready` deltaP `6.9184` edge `-0.0014` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.3894` n `135` status `ready` deltaP `7.4008` edge `-0.0118` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.3894` n `135` status `ready` deltaP `7.4008` edge `-0.0118` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.476` n `135` status `ready` deltaP `1.4826` edge `0.0008` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.476` n `135` status `ready` deltaP `1.4826` edge `0.0008` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
