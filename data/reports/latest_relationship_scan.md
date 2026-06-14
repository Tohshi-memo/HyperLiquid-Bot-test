# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T16:37:32.178138+00:00`
- Price records: `672`
- Market context records: `3909`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `48.8938` n `70` status `ready` deltaP `4.4555` edge `6.4529` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.8938` n `70` status `ready` deltaP `4.4555` edge `6.4529` maxDD `-13.467`
- `risk_on_high->equity_24h` score `21.7259` n `40` status `ready` deltaP `42.0139` edge `1.5304` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `21.7259` n `40` status `ready` deltaP `42.0139` edge `1.5304` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `20.8736` n `40` status `ready` deltaP `12.4306` edge `1.7982` maxDD `-7.6614`
- `risk_on_and_context->crypto_major_24h` score `20.8736` n `40` status `ready` deltaP `12.4306` edge `1.7982` maxDD `-7.6614`
- `risk_on_high->index_24h` score `8.8372` n `40` status `ready` deltaP `30.0347` edge `0.5362` maxDD `0.0`
- `risk_on_and_context->index_24h` score `8.8372` n `40` status `ready` deltaP `30.0347` edge `0.5362` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.9104` n `206` status `ready` deltaP `-1.6887` edge `1.4381` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `6.4414` n `70` status `ready` deltaP `22.5522` edge `0.4832` maxDD `-5.0747`
- `risk_on_and_context->crypto_major_4h` score `6.4414` n `70` status `ready` deltaP `22.5522` edge `0.4832` maxDD `-5.0747`
- `market_context_high->equity_24h` score `6.0648` n `165` status `ready` deltaP `20.8018` edge `0.6697` maxDD `-14.5715`
- `risk_on_high->crypto_alt_24h` score `5.8987` n `40` status `ready` deltaP `10.3472` edge `0.9168` maxDD `-14.6959`
- `risk_on_and_context->crypto_alt_24h` score `5.8987` n `40` status `ready` deltaP `10.3472` edge `0.9168` maxDD `-14.6959`
- `market_context_high->index_24h` score `4.5804` n `165` status `ready` deltaP `25.7923` edge `0.3237` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.3347` n `70` status `ready` deltaP `27.3302` edge `0.1852` maxDD `-4.4942`
- `risk_on_and_context->equity_4h` score `3.3347` n `70` status `ready` deltaP `27.3302` edge `0.1852` maxDD `-4.4942`
- `market_context_high->crypto_major_4h` score `2.9408` n `206` status `ready` deltaP `17.6563` edge `0.3038` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.7483` n `165` status `ready` deltaP `18.4596` edge `0.2533` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.3166` n `206` status `ready` deltaP `14.4314` edge `0.1839` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
