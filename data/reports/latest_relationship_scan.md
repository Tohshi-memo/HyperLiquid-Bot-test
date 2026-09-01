# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T04:37:25.989093+00:00`
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

- `risk_on_high->unknown_4h` score `7.474` n `107` status `ready` deltaP `22.3544` edge `0.5356` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.474` n `107` status `ready` deltaP `22.3544` edge `0.5356` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0206` n `151` status `ready` deltaP `18.647` edge `0.4469` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1645` n `107` status `ready` deltaP `5.3179` edge `0.2026` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1645` n `107` status `ready` deltaP `5.3179` edge `0.2026` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0337` n `151` status `ready` deltaP `4.6804` edge `0.2013` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.4096` n `107` status `ready` deltaP `13.1199` edge `0.1288` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.4096` n `107` status `ready` deltaP `13.1199` edge `0.1288` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.2585` n `61` status `ready` deltaP `2.4222` edge `0.1234` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `0.9765` n `107` status `ready` deltaP `14.1388` edge `0.7213` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.9765` n `107` status `ready` deltaP `14.1388` edge `0.7213` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.8136` n `151` status `ready` deltaP `12.4885` edge `0.1041` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1232` n `61` status `ready` deltaP `10.3484` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0981` n `151` status `ready` deltaP `8.5726` edge `0.016` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.0663` n `61` status `ready` deltaP `4.7481` edge `0.0185` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.0068` n `151` status `ready` deltaP `5.9966` edge `0.0492` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `-0.0095` n `107` status `ready` deltaP `5.4718` edge `0.0145` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0095` n `107` status `ready` deltaP `5.4718` edge `0.0145` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0275` n `107` status `ready` deltaP `6.1475` edge `0.0` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0275` n `107` status `ready` deltaP `6.1475` edge `0.0` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
