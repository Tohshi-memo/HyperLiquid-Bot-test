# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T21:52:24.333913+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10593`

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

- `risk_on_high->unknown_24h` score `315.827` n `105` status `ready` deltaP `27.2569` edge `26.1372` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `315.827` n `105` status `ready` deltaP `27.2569` edge `26.1372` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.9653` n `105` status `ready` deltaP `33.7897` edge `1.4902` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.9653` n `105` status `ready` deltaP `33.7897` edge `1.4902` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.8433` n `105` status `ready` deltaP `29.4295` edge `0.9657` maxDD `-0.3296`
- `risk_on_and_context->crypto_alt_24h` score `13.8433` n `105` status `ready` deltaP `29.4295` edge `0.9657` maxDD `-0.3296`
- `market_context_high->crypto_alt_24h` score `8.5324` n `196` status `ready` deltaP `23.239` edge `0.6136` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `7.9951` n `250` status `ready` deltaP `-4.109` edge `0.7661` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.814` n `196` status `ready` deltaP `23.0903` edge `0.4139` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.1526` n `119` status `ready` deltaP `29.8704` edge `0.3446` maxDD `-2.1484`
- `risk_on_and_context->crypto_alt_4h` score `6.1526` n `119` status `ready` deltaP `29.8704` edge `0.3446` maxDD `-2.1484`
- `risk_on_high->equity_24h` score `6.034` n `105` status `ready` deltaP `23.0903` edge `0.3489` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.034` n `105` status `ready` deltaP `23.0903` edge `0.3489` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.2951` n `119` status `ready` deltaP `24.0431` edge `0.2835` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2951` n `119` status `ready` deltaP `24.0431` edge `0.2835` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7954` n `105` status `ready` deltaP `23.1846` edge `0.0832` maxDD `-0.0516`
- `risk_on_and_context->index_24h` score `2.7954` n `105` status `ready` deltaP `23.1846` edge `0.0832` maxDD `-0.0516`
- `market_context_high->index_24h` score `2.6079` n `196` status `ready` deltaP `21.9601` edge `0.0953` maxDD `-0.2837`
- `risk_on_high->crypto_alt_1h` score `1.2097` n `128` status `ready` deltaP `5.7635` edge `0.0946` maxDD `-0.9103`
- `risk_on_and_context->crypto_alt_1h` score `1.2097` n `128` status `ready` deltaP `5.7635` edge `0.0946` maxDD `-0.9103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
