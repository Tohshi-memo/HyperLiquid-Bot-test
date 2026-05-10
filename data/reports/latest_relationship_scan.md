# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T02:07:16.837614+00:00`
- Price records: `672`
- Market context records: `930`
- Flow alert records: `2603`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.3918` n `32` status `ready` deltaP `31.5972` edge `1.572` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.3918` n `32` status `ready` deltaP `31.5972` edge `1.572` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.5184` n `169` status `ready` deltaP `28.6386` edge `0.969` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.7916` n `32` status `ready` deltaP `25.0` edge `0.8993` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.7916` n `32` status `ready` deltaP `25.0` edge `0.8993` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.4801` n `32` status `ready` deltaP `4.8611` edge `1.0076` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.4801` n `32` status `ready` deltaP `4.8611` edge `1.0076` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.4249` n `169` status `ready` deltaP `4.8611` edge `0.503` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9912` n `32` status `ready` deltaP `26.9097` edge `0.1532` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9912` n `32` status `ready` deltaP `26.9097` edge `0.1532` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2123` n `32` status `ready` deltaP `5.7165` edge `0.2661` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.2123` n `32` status `ready` deltaP `5.7165` edge `0.2661` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.1743` n `32` status `ready` deltaP `23.3994` edge `0.129` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.1743` n `32` status `ready` deltaP `23.3994` edge `0.129` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.772` n `32` status `ready` deltaP `20.5793` edge `0.131` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.772` n `32` status `ready` deltaP `20.5793` edge `0.131` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.2165` n `32` status `ready` deltaP `10.4421` edge `0.1239` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.2165` n `32` status `ready` deltaP `10.4421` edge `0.1239` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.0047` n `32` status `ready` deltaP `-13.0208` edge `0.2902` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.0047` n `32` status `ready` deltaP `-13.0208` edge `0.2902` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
