# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T01:37:27.884912+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11538`

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

- `risk_on_high->unknown_4h` score `22.8611` n `133` status `ready` deltaP `10.218` edge `1.8988` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.8611` n `133` status `ready` deltaP `10.218` edge `1.8988` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.0961` n `167` status `ready` deltaP `11.8163` edge `1.3321` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.0035` n `133` status `ready` deltaP `-0.3051` edge `1.2267` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.0035` n `133` status `ready` deltaP `-0.3051` edge `1.2267` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.5237` n `167` status `ready` deltaP `0.1497` edge `0.8557` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.6338` n `134` status `ready` deltaP `15.8971` edge `0.3814` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3208` n `67` status `ready` deltaP `5.9474` edge `0.0374` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0579` n `133` status `ready` deltaP `11.6643` edge `0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0579` n `133` status `ready` deltaP `11.6643` edge `0.0009` maxDD `-1.699`
- `risk_on_high->equity_24h` score `0.0443` n `112` status `ready` deltaP `11.0863` edge `0.3443` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.0443` n `112` status `ready` deltaP `11.0863` edge `0.3443` maxDD `-19.828`
- `news_risk_high->index_1h` score `-0.0562` n `67` status `ready` deltaP `4.6251` edge `-0.0027` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0944` n `133` status `ready` deltaP `5.0403` edge `-0.0012` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0944` n `133` status `ready` deltaP `5.0403` edge `-0.0012` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.149` n `133` status `ready` deltaP `4.9007` edge `0.0566` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.149` n `133` status `ready` deltaP `4.9007` edge `0.0566` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.181` n `67` status `ready` deltaP `4.4517` edge `-0.0255` maxDD `-0.2074`
- `news_risk_high->fx_4h` score `-0.1928` n `67` status `ready` deltaP `7.06` edge `0.0025` maxDD `-1.2507`
- `news_risk_high->commodity_1h` score `-0.2125` n `67` status `ready` deltaP `4.0084` edge `0.0002` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
