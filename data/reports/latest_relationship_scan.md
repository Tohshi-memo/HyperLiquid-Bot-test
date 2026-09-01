# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T04:52:26.053479+00:00`
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

- `risk_on_high->unknown_4h` score `7.4558` n `107` status `ready` deltaP `22.202` edge `0.5351` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4558` n `107` status `ready` deltaP `22.202` edge `0.5351` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0024` n `151` status `ready` deltaP `18.4946` edge `0.4464` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2017` n `107` status `ready` deltaP `5.3179` edge `0.2057` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2017` n `107` status `ready` deltaP `5.3179` edge `0.2057` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0709` n `151` status `ready` deltaP `4.6804` edge `0.2044` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.3681` n `107` status `ready` deltaP `12.9462` edge `0.1265` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.3681` n `107` status `ready` deltaP `12.9462` edge `0.1265` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.2957` n `61` status `ready` deltaP `2.4222` edge `0.1265` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `0.9035` n `107` status `ready` deltaP `13.9652` edge `0.7131` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.9035` n `107` status `ready` deltaP `13.9652` edge `0.7131` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.7721` n `151` status `ready` deltaP `12.3148` edge `0.1018` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1232` n `61` status `ready` deltaP `10.3484` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0837` n `151` status `ready` deltaP `8.4229` edge `0.0158` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.0552` n `61` status `ready` deltaP `4.5957` edge `0.0181` maxDD `-1.3325`
- `risk_on_high->commodity_1h` score `-0.0189` n `107` status `ready` deltaP `5.3221` edge `0.0143` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0189` n `107` status `ready` deltaP `5.3221` edge `0.0143` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.0238` n `151` status `ready` deltaP `5.8442` edge `0.0488` maxDD `-2.1795`
- `risk_on_high->index_1h` score `-0.0275` n `107` status `ready` deltaP `6.1475` edge `0.0` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0275` n `107` status `ready` deltaP `6.1475` edge `0.0` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
