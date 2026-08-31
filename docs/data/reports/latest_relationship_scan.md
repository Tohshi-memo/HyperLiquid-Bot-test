# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T17:07:25.324510+00:00`
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

- `risk_on_high->unknown_4h` score `7.9906` n `107` status `ready` deltaP `24.3361` edge `0.5653` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `7.9906` n `107` status `ready` deltaP `24.3361` edge `0.5653` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.4446` n `159` status `ready` deltaP `21.0327` edge `0.4662` maxDD `-2.5493`
- `risk_on_high->crypto_alt_24h` score `5.0813` n `74` status `ready` deltaP `25.7883` edge `0.9289` maxDD `-28.9501`
- `risk_on_and_context->crypto_alt_24h` score `5.0813` n `74` status `ready` deltaP `25.7883` edge `0.9289` maxDD `-28.9501`
- `risk_on_high->unknown_1h` score `2.4957` n `107` status `ready` deltaP `7.1143` edge `0.2182` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4957` n `107` status `ready` deltaP `7.1143` edge `0.2182` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2731` n `159` status `ready` deltaP `6.456` edge `0.2094` maxDD `-2.041`
- `risk_on_high->fx_24h` score `2.1718` n `74` status `ready` deltaP `51.9285` edge `0.0346` maxDD `-1.8547`
- `risk_on_and_context->fx_24h` score `2.1718` n `74` status `ready` deltaP `51.9285` edge `0.0346` maxDD `-1.8547`
- `market_context_high->crypto_alt_24h` score `1.8594` n `117` status `ready` deltaP `12.2864` edge `0.5566` maxDD `-31.0182`
- `risk_on_high->commodity_24h` score `1.711` n `74` status `ready` deltaP `11.937` edge `0.1618` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.711` n `74` status `ready` deltaP `11.937` edge `0.1618` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.5922` n `61` status `ready` deltaP `4.2186` edge `0.1392` maxDD `-1.1043`
- `market_context_high->fx_24h` score `0.993` n `117` status `ready` deltaP `32.3051` edge `0.0239` maxDD `-2.5211`
- `market_context_high->metal_24h` score `0.3514` n `117` status `ready` deltaP `22.7564` edge `0.1436` maxDD `-10.0208`
- `news_risk_high->commodity_4h` score `0.3181` n `61` status `ready` deltaP `8.4066` edge `0.0264` maxDD `-1.3325`
- `news_risk_high->commodity_24h` score `0.252` n `44` status `ready` deltaP `5.3031` edge `0.0285` maxDD `-1.1904`
- `market_context_high->commodity_1h` score `0.2222` n `159` status `ready` deltaP `9.7795` edge `0.0183` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.2085` n `61` status `ready` deltaP `11.4155` edge `0.0006` maxDD `-0.7461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
