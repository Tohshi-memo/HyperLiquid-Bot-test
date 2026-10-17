# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T18:07:29.018992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `risk_on_high->commodity_24h` score `6.9497` n `54` status `ready` deltaP `38.676` edge `0.3213` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9497` n `54` status `ready` deltaP `38.676` edge `0.3213` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.4976` n `172` status `ready` deltaP `13.8081` edge `0.3475` maxDD `-14.1804`
- `risk_on_high->crypto_major_4h` score `0.5761` n `90` status `ready` deltaP `16.25` edge `0.2025` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5761` n `90` status `ready` deltaP `16.25` edge `0.2025` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4933` n `174` status `ready` deltaP `5.3703` edge `0.0942` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0806` n `174` status `ready` deltaP `7.5917` edge `0.1061` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0519` n `90` status `ready` deltaP `5.5556` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0519` n `90` status `ready` deltaP `5.5556` edge `0.0057` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.196` n `174` status `ready` deltaP `6.705` edge `0.005` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2514` n `90` status `ready` deltaP `1.3213` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2514` n `90` status `ready` deltaP `1.3213` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3159` n `174` status `ready` deltaP `5.766` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3705` n `174` status `ready` deltaP `10.1584` edge `0.0385` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4158` n `90` status `ready` deltaP `10.1201` edge `0.0275` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4158` n `90` status `ready` deltaP `10.1201` edge `0.0275` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.504` n `90` status `ready` deltaP `0.7086` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.504` n `90` status `ready` deltaP `0.7086` edge `0.0038` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5051` n `172` status `ready` deltaP `5.7466` edge `0.0408` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.7048` n `90` status `ready` deltaP `0.2362` edge `0.0` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
