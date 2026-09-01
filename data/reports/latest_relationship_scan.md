# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T05:07:27.964666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.4316` n `107` status `ready` deltaP `22.0496` edge `0.5341` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4316` n `107` status `ready` deltaP `22.0496` edge `0.5341` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.9782` n `151` status `ready` deltaP `18.3422` edge `0.4454` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2101` n `107` status `ready` deltaP `5.3179` edge `0.2064` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2101` n `107` status `ready` deltaP `5.3179` edge `0.2064` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0793` n `151` status `ready` deltaP `4.6804` edge `0.2051` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.3266` n `107` status `ready` deltaP `12.7726` edge `0.1242` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.3266` n `107` status `ready` deltaP `12.7726` edge `0.1242` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.3041` n `61` status `ready` deltaP `2.4222` edge `0.1272` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `0.8337` n `107` status `ready` deltaP `13.7916` edge `0.7053` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.8337` n `107` status `ready` deltaP `13.7916` edge `0.7053` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.7306` n `151` status `ready` deltaP `12.1412` edge `0.0995` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1244` n `61` status `ready` deltaP `10.3484` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0681` n `151` status `ready` deltaP `8.2732` edge `0.0155` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.0442` n `61` status `ready` deltaP `4.4432` edge `0.0177` maxDD `-1.3325`
- `risk_on_high->index_1h` score `-0.0189` n `107` status `ready` deltaP `6.2972` edge `0.0001` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0189` n `107` status `ready` deltaP `6.2972` edge `0.0001` maxDD `-0.5605`
- `risk_on_high->commodity_1h` score `-0.029` n `107` status `ready` deltaP `5.1724` edge `0.014` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.029` n `107` status `ready` deltaP `5.1724` edge `0.014` maxDD `-0.8428`
- `risk_on_high->fx_24h` score `-0.0367` n `107` status `ready` deltaP `36.1241` edge `0.0242` maxDD `-4.2453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
