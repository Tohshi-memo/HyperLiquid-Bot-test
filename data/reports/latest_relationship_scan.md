# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T00:52:28.000874+00:00`
- Price records: `672`
- Market context records: `3022`
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

- `market_context_high->crypto_alt_24h` score `21.6403` n `99` status `ready` deltaP `9.7695` edge `2.1299` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5777` n `99` status `ready` deltaP `42.3769` edge `0.7897` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `12.5407` n `99` status `ready` deltaP `21.5436` edge `0.9479` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.9947` n `99` status `ready` deltaP `20.423` edge `1.0358` maxDD `-18.3486`
- `market_context_high->index_24h` score `6.8553` n `99` status `ready` deltaP `20.0127` edge `0.5634` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5839` n `113` status `ready` deltaP `18.7257` edge `0.1552` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6242` n `113` status `ready` deltaP `14.3603` edge `0.1752` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.4714` n `113` status `ready` deltaP `24.8152` edge `0.4498` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.2107` n `113` status `ready` deltaP `16.8884` edge `0.1042` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.0798` n `125` status `ready` deltaP `2.8515` edge `0.0299` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3233` n `125` status `ready` deltaP `3.9557` edge `0.0418` maxDD `-5.7692`
- `market_context_high->fx_1h` score `-0.4929` n `125` status `ready` deltaP `-4.0491` edge `0.0004` maxDD `-0.2615`
- `market_context_high->index_1h` score `-0.511` n `125` status `ready` deltaP `4.8491` edge `0.0265` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5395` n `125` status `ready` deltaP `6.5988` edge `0.0998` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.7485` n `125` status `ready` deltaP `4.4563` edge `-0.019` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-0.9165` n `113` status `ready` deltaP `-0.5612` edge `0.0327` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-0.9994` n `125` status `ready` deltaP `4.4934` edge `0.0682` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.2028` n `125` status `ready` deltaP `-2.6084` edge `-0.005` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.5384` n `113` status `ready` deltaP `-7.247` edge `-0.0009` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.7076` n `99` status `ready` deltaP `-4.577` edge `-0.0246` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
