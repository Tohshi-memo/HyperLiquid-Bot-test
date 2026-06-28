# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T16:52:35.073205+00:00`
- Price records: `672`
- Market context records: `5059`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `12.8009` n `98` status `ready` deltaP `3.3056` edge `1.0948` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0117` n `98` status `ready` deltaP `20.9837` edge `0.7133` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.9327` n `98` status `ready` deltaP `17.9442` edge `0.5015` maxDD `-6.8054`
- `market_context_high->crypto_major_4h` score `5.3248` n `98` status `ready` deltaP `16.3608` edge `0.4931` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `0.9752` n `98` status `ready` deltaP `7.8516` edge `0.1158` maxDD `-4.2834`
- `market_context_high->metal_4h` score `0.9162` n `98` status `ready` deltaP `10.0267` edge `0.1174` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8239` n `98` status `ready` deltaP `8.1908` edge `0.0714` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6329` n `98` status `ready` deltaP `5.7584` edge `0.1684` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.415` n `98` status `ready` deltaP `7.1306` edge `0.0367` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2759` n `98` status `ready` deltaP `5.878` edge `0.0948` maxDD `-5.2229`
- `market_context_high->index_4h` score `-0.0247` n `98` status `ready` deltaP `5.2887` edge `0.0388` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0569` n `74` status `ready` deltaP `9.0747` edge `0.0084` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.3376` n `98` status `ready` deltaP `1.4695` edge `0.0124` maxDD `-0.5714`
- `market_context_high->commodity_1h` score `-0.5496` n `98` status `ready` deltaP `0.9257` edge `0.014` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8737` n `98` status `ready` deltaP `6.9531` edge `0.0061` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9736` n `98` status `ready` deltaP `-3.7176` edge `-0.0011` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4442` n `98` status `ready` deltaP `-8.258` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.6641` n `74` status `ready` deltaP `5.4945` edge `0.0391` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.2416` n `74` status `ready` deltaP `0.8211` edge `-0.0806` maxDD `-25.1598`
- `market_context_high->unknown_24h` score `-4.457` n `74` status `ready` deltaP `27.0364` edge `-0.5174` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
