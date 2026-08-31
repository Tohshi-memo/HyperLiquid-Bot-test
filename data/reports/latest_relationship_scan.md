# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T21:07:34.093288+00:00`
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

- `risk_on_high->unknown_4h` score `7.832` n `107` status `ready` deltaP `23.5739` edge `0.5572` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.832` n `107` status `ready` deltaP `23.5739` edge `0.5572` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.2848` n `159` status `ready` deltaP `20.2705` edge `0.458` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.2436` n `107` status `ready` deltaP `5.9167` edge `0.2052` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.2436` n `107` status `ready` deltaP `5.9167` edge `0.2052` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.0197` n `159` status `ready` deltaP `5.2584` edge `0.1963` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.9403` n `88` status `ready` deltaP `13.8889` edge `0.1679` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.9403` n `88` status `ready` deltaP `13.8889` edge `0.1679` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.3379` n `61` status `ready` deltaP `3.021` edge `0.126` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.039` n `88` status `ready` deltaP `42.8819` edge `0.0248` maxDD `-3.1977`
- `risk_on_and_context->fx_24h` score `1.039` n `88` status `ready` deltaP `42.8819` edge `0.0248` maxDD `-3.1977`
- `risk_on_high->crypto_alt_24h` score `0.8948` n `88` status `ready` deltaP `14.394` edge `0.6933` maxDD `-42.2971`
- `risk_on_and_context->crypto_alt_24h` score `0.8948` n `88` status `ready` deltaP `14.394` edge `0.6933` maxDD `-42.2971`
- `news_risk_high->commodity_4h` score `0.1988` n `61` status `ready` deltaP `6.5774` edge `0.0233` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1743` n `159` status `ready` deltaP `9.3304` edge `0.0173` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1208` n `61` status `ready` deltaP `10.3484` edge `0.0004` maxDD `-0.7461`
- `market_context_high->fx_24h` score `0.0466` n `133` status `ready` deltaP `28.5022` edge `0.0187` maxDD `-4.0532`
- `risk_on_high->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0524` n `107` status `ready` deltaP `5.6984` edge `-0.0002` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
