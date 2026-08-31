# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T16:22:29.420137+00:00`
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

- `risk_on_high->unknown_4h` score `8.0476` n `107` status `ready` deltaP `24.7935` edge `0.567` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0476` n `107` status `ready` deltaP `24.7935` edge `0.567` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5016` n `159` status `ready` deltaP `21.4901` edge `0.4679` maxDD `-2.5493`
- `risk_on_high->crypto_alt_24h` score `6.4685` n `71` status `ready` deltaP `28.8146` edge `1.0171` maxDD `-24.3927`
- `risk_on_and_context->crypto_alt_24h` score `6.4685` n `71` status `ready` deltaP `28.8146` edge `1.0171` maxDD `-24.3927`
- `market_context_high->crypto_alt_24h` score `3.1993` n `114` status `ready` deltaP `13.8158` edge `0.6018` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.463` n `71` status `ready` deltaP `54.5481` edge `0.038` maxDD `-1.5373`
- `risk_on_and_context->fx_24h` score `2.463` n `71` status `ready` deltaP `54.5481` edge `0.038` maxDD `-1.5373`
- `risk_on_high->unknown_1h` score `2.4574` n `107` status `ready` deltaP `6.8149` edge `0.217` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4574` n `107` status `ready` deltaP `6.8149` edge `0.217` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2348` n `159` status `ready` deltaP `6.1566` edge `0.2082` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5539` n `61` status `ready` deltaP `3.9192` edge `0.138` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.1322` n `114` status `ready` deltaP `33.2237` edge `0.0254` maxDD `-2.2036`
- `risk_on_high->commodity_24h` score `1.013` n `71` status `ready` deltaP `11.2016` edge `0.154` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.013` n `71` status `ready` deltaP `11.2016` edge `0.154` maxDD `-0.5706`
- `market_context_high->metal_24h` score `0.8187` n `114` status `ready` deltaP `24.4883` edge `0.1582` maxDD `-8.3191`
- `news_risk_high->commodity_4h` score `0.33` n `61` status `ready` deltaP `8.5591` edge `0.0269` maxDD `-1.3325`
- `news_risk_high->commodity_24h` score `0.3282` n `44` status `ready` deltaP `5.8239` edge `0.0348` maxDD `-1.1904`
- `news_risk_high->fx_4h` score `0.2463` n `61` status `ready` deltaP `11.8728` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.2222` n `159` status `ready` deltaP `9.7795` edge `0.0183` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
