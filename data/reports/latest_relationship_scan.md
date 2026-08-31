# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T16:52:27.669667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `risk_on_high->unknown_4h` score `8.0052` n `107` status `ready` deltaP `24.4886` edge `0.5655` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0052` n `107` status `ready` deltaP `24.4886` edge `0.5655` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.4592` n `159` status `ready` deltaP `21.1852` edge `0.4664` maxDD `-2.5493`
- `risk_on_high->crypto_alt_24h` score `5.5439` n `73` status `ready` deltaP `26.7694` edge `0.9579` maxDD `-27.3814`
- `risk_on_and_context->crypto_alt_24h` score `5.5439` n `73` status `ready` deltaP `26.7694` edge `0.9579` maxDD `-27.3814`
- `risk_on_high->unknown_1h` score `2.4718` n `107` status `ready` deltaP `6.9646` edge `0.2172` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4718` n `107` status `ready` deltaP `6.9646` edge `0.2172` maxDD `-1.9453`
- `market_context_high->crypto_alt_24h` score `2.3648` n `116` status `ready` deltaP `12.7874` edge `0.5716` maxDD `-29.4495`
- `risk_on_high->fx_24h` score `2.2688` n `73` status `ready` deltaP `52.7731` edge `0.0358` maxDD `-1.7403`
- `risk_on_and_context->fx_24h` score `2.2688` n `73` status `ready` deltaP `52.7731` edge `0.0358` maxDD `-1.7403`
- `market_context_high->unknown_1h` score `2.2492` n `159` status `ready` deltaP `6.3063` edge `0.2084` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5683` n `61` status `ready` deltaP `4.0689` edge `0.1382` maxDD `-1.1043`
- `risk_on_high->commodity_24h` score `1.0781` n `73` status `ready` deltaP `11.7033` edge `0.159` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.0781` n `73` status `ready` deltaP `11.7033` edge `0.159` maxDD `-0.5706`
- `market_context_high->fx_24h` score `1.04` n `116` status `ready` deltaP `32.603` edge `0.0244` maxDD `-2.4067`
- `market_context_high->metal_24h` score `0.5061` n `116` status `ready` deltaP `23.3237` edge `0.1483` maxDD `-9.4462`
- `news_risk_high->commodity_4h` score `0.3292` n `61` status `ready` deltaP `8.5591` edge `0.0268` maxDD `-1.3325`
- `news_risk_high->commodity_24h` score `0.2774` n `44` status `ready` deltaP `5.4767` edge `0.0306` maxDD `-1.1904`
- `market_context_high->commodity_1h` score `0.2366` n `159` status `ready` deltaP `9.9292` edge `0.0185` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.2207` n `61` status `ready` deltaP `11.5679` edge `0.0006` maxDD `-0.7461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
