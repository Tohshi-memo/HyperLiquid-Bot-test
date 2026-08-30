# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T00:07:30.513287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_alt_4h` score `7.0122` n `51` status `ready` deltaP `24.2049` edge `0.454` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `7.0122` n `51` status `ready` deltaP `24.2049` edge `0.454` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `6.1069` n `51` status `ready` deltaP `33.2257` edge `0.315` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.1069` n `51` status `ready` deltaP `33.2257` edge `0.315` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.679` n `104` status `ready` deltaP `34.415` edge `0.2624` maxDD `-3.1535`
- `news_risk_high->crypto_alt_24h` score `4.4599` n `43` status `ready` deltaP `20.3933` edge `0.7734` maxDD `-22.3391`
- `news_risk_high->unknown_4h` score `4.3828` n `49` status `ready` deltaP `-2.859` edge `0.4433` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `3.4062` n `49` status `ready` deltaP `-7.5675` edge `0.37` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1344` n `51` status `ready` deltaP `35.4286` edge `0.0336` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1344` n `51` status `ready` deltaP `35.4286` edge `0.0336` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.4503` n `51` status `ready` deltaP `20.0891` edge `0.0952` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.4503` n `51` status `ready` deltaP `20.0891` edge `0.0952` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8355` n `153` status `ready` deltaP `17.6959` edge `0.082` maxDD `-1.0945`
- `risk_on_high->index_4h` score `1.5299` n `51` status `ready` deltaP `22.2023` edge `0.0104` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.5299` n `51` status `ready` deltaP `22.2023` edge `0.0104` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.3598` n `165` status `ready` deltaP `8.4622` edge `0.105` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.2839` n `63` status `ready` deltaP `18.1352` edge `0.0075` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2839` n `63` status `ready` deltaP `18.1352` edge `0.0075` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.0143` n `49` status `ready` deltaP `25.9177` edge `0.0122` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.5769` n `63` status `ready` deltaP `1.2761` edge `0.0835` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
