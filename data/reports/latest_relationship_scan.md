# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T05:07:29.484579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `8.6359` n `63` status `ready` deltaP `22.8465` edge `0.6102` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.6359` n `63` status `ready` deltaP `22.8465` edge `0.6102` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `4.9947` n `165` status `ready` deltaP `19.3256` edge `0.3344` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6446` n `101` status `ready` deltaP `33.6702` edge `0.2645` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.3616` n `63` status `ready` deltaP `23.9668` edge `0.232` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.3616` n `63` status `ready` deltaP `23.9668` edge `0.232` maxDD `-0.5985`
- `risk_on_high->equity_4h` score `3.0185` n `63` status `ready` deltaP `27.4197` edge `0.0874` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.0185` n `63` status `ready` deltaP `27.4197` edge `0.0874` maxDD `-0.1594`
- `risk_on_high->unknown_1h` score `2.8816` n `63` status `ready` deltaP `6.3374` edge `0.224` maxDD `-0.7562`
- `risk_on_and_context->unknown_1h` score `2.8816` n `63` status `ready` deltaP `6.3374` edge `0.224` maxDD `-0.7562`
- `risk_on_high->crypto_alt_4h` score `2.4753` n `63` status `ready` deltaP `14.1648` edge `0.2712` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.4753` n `63` status `ready` deltaP `14.1648` edge `0.2712` maxDD `-1.5298`
- `market_context_high->unknown_1h` score `2.2674` n `165` status `ready` deltaP `10.5798` edge `0.1593` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.1385` n `63` status `ready` deltaP `27.5092` edge `0.0123` maxDD `-0.0654`
- `risk_on_and_context->index_4h` score `2.1385` n `63` status `ready` deltaP `27.5092` edge `0.0123` maxDD `-0.0654`
- `risk_on_high->metal_4h` score `1.7586` n `63` status `ready` deltaP `22.2634` edge `0.0279` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7586` n `63` status `ready` deltaP `22.2634` edge `0.0279` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.4946` n `63` status `ready` deltaP `20.0219` edge `0.0081` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.4946` n `63` status `ready` deltaP `20.0219` edge `0.0081` maxDD `-0.0291`
- `news_risk_high->unknown_1h` score `1.2531` n `32` status `ready` deltaP `-13.4543` edge `0.2243` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
