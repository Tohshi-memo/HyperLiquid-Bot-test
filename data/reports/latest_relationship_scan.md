# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T16:37:35.663969+00:00`
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

- `risk_on_high->unknown_4h` score `8.0282` n `107` status `ready` deltaP `24.641` edge `0.5664` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0282` n `107` status `ready` deltaP `24.641` edge `0.5664` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.4822` n `159` status `ready` deltaP `21.3376` edge `0.4673` maxDD `-2.5493`
- `risk_on_high->crypto_alt_24h` score `5.9854` n `72` status `ready` deltaP `27.7778` edge `0.9857` maxDD `-25.9491`
- `risk_on_and_context->crypto_alt_24h` score `5.9854` n `72` status `ready` deltaP `27.7778` edge `0.9857` maxDD `-25.9491`
- `market_context_high->crypto_alt_24h` score `2.8372` n `115` status `ready` deltaP `13.2971` edge `0.5855` maxDD `-28.0172`
- `risk_on_high->unknown_1h` score `2.4706` n `107` status `ready` deltaP `6.9646` edge `0.2171` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4706` n `107` status `ready` deltaP `6.9646` edge `0.2171` maxDD `-1.9453`
- `risk_on_high->fx_24h` score `2.3653` n `72` status `ready` deltaP `53.6458` edge `0.0369` maxDD `-1.637`
- `risk_on_and_context->fx_24h` score `2.3653` n `72` status `ready` deltaP `53.6458` edge `0.0369` maxDD `-1.637`
- `market_context_high->unknown_1h` score `2.248` n `159` status `ready` deltaP `6.3063` edge `0.2083` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5671` n `61` status `ready` deltaP `4.0689` edge `0.1381` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.086` n `115` status `ready` deltaP `32.9091` edge `0.0249` maxDD `-2.3033`
- `risk_on_high->commodity_24h` score `1.0498` n `72` status `ready` deltaP `11.4583` edge `0.157` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.0498` n `72` status `ready` deltaP `11.4583` edge `0.157` maxDD `-0.5706`
- `market_context_high->metal_24h` score `0.6593` n `115` status `ready` deltaP `23.9009` edge `0.153` maxDD `-8.8914`
- `news_risk_high->commodity_4h` score `0.33` n `61` status `ready` deltaP `8.5591` edge `0.0269` maxDD `-1.3325`
- `news_risk_high->commodity_24h` score `0.3028` n `44` status `ready` deltaP `5.6503` edge `0.0327` maxDD `-1.1904`
- `news_risk_high->fx_4h` score `0.2341` n `61` status `ready` deltaP `11.7204` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.2222` n `159` status `ready` deltaP `9.7795` edge `0.0183` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
