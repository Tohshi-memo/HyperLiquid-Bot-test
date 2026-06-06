# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T02:22:20.432317+00:00`
- Price records: `672`
- Market context records: `3029`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.5336` n `99` status `ready` deltaP `10.8112` edge `2.1974` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.84` n `99` status `ready` deltaP `22.5852` edge `0.9659` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.6953` n `99` status `ready` deltaP `42.3769` edge `0.7995` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.6113` n `99` status `ready` deltaP `21.4647` edge `1.1079` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.4186` n `99` status `ready` deltaP `21.0543` edge `0.6034` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7894` n `119` status `ready` deltaP `19.1497` edge `0.1695` maxDD `-2.8438`
- `market_context_high->index_4h` score `0.0783` n `119` status `ready` deltaP `15.6167` edge `0.0957` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.0553` n `129` status `ready` deltaP `2.5902` edge `0.0296` maxDD `-1.7142`
- `market_context_high->crypto_alt_4h` score `-0.0338` n `119` status `ready` deltaP `22.0152` edge `0.4037` maxDD `-38.7172`
- `market_context_high->equity_4h` score `-0.3023` n `119` status `ready` deltaP `12.5718` edge `0.1355` maxDD `-18.3126`
- `market_context_high->index_1h` score `-0.4154` n `129` status `ready` deltaP `3.7878` edge `0.0229` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.491` n `129` status `ready` deltaP `3.7182` edge `0.0338` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5408` n `129` status `ready` deltaP `-4.8891` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5716` n `129` status `ready` deltaP `6.3861` edge `0.0971` maxDD `-14.7034`
- `market_context_high->unknown_4h` score `-0.5834` n `119` status `ready` deltaP `0.9633` edge `0.0503` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-0.8273` n `129` status `ready` deltaP `3.9212` edge `-0.022` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0028` n `129` status `ready` deltaP `4.2798` edge `0.0692` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0225` n `119` status `ready` deltaP `-7.4478` edge `-0.0018` maxDD `-0.7044`
- `market_context_high->metal_1h` score `-1.1466` n `129` status `ready` deltaP `-1.7987` edge `-0.0032` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.5943` n `99` status `ready` deltaP `-3.5353` edge `-0.0221` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
