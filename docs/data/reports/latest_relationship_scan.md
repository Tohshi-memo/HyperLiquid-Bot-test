# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T02:37:17.713995+00:00`
- Price records: `672`
- Market context records: `2100`
- Flow alert records: `7939`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.6386` n `181` status `ready` deltaP `31.0824` edge `0.7938` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4645` n `181` status `ready` deltaP `37.4452` edge `0.6754` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.8027` n `181` status `ready` deltaP `23.8613` edge `0.3994` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1231` n `181` status `ready` deltaP `22.507` edge `0.303` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.654` n `180` status `ready` deltaP `22.8162` edge `0.6011` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5305` n `181` status `ready` deltaP `18.83` edge `0.1537` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2642` n `181` status `ready` deltaP `16.0345` edge `0.1804` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.2586` n `180` status `ready` deltaP `11.5879` edge `0.2338` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0564` n `181` status `ready` deltaP `12.8908` edge `0.1968` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6243` n `180` status `ready` deltaP `22.7701` edge `0.4734` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8682` n `181` status `ready` deltaP `11.0233` edge `0.0777` maxDD `-2.6402`
- `market_context_high->metal_4h` score `0.5198` n `181` status `ready` deltaP `14.6417` edge `0.1679` maxDD `-10.4422`
- `market_context_high->unknown_1h` score `0.2516` n `181` status `ready` deltaP `5.5695` edge `0.0558` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1935` n `181` status `ready` deltaP `6.4893` edge `0.0319` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0449` n `180` status `ready` deltaP `21.0188` edge `0.7222` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1165` n `180` status `ready` deltaP `14.9097` edge `0.0302` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.1659` n `181` status `ready` deltaP `7.1021` edge `0.0409` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8662` n `181` status `ready` deltaP `-1.5772` edge `0.0011` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0149` n `181` status `ready` deltaP `-6.0116` edge `-0.0019` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.0909` n `180` status `ready` deltaP `10.3364` edge `0.2303` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
