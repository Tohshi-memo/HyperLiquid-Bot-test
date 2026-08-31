# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T20:37:29.541078+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11568`

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

- `risk_on_high->unknown_4h` score `7.8514` n `107` status `ready` deltaP `23.7264` edge `0.5578` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8514` n `107` status `ready` deltaP `23.7264` edge `0.5578` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3041` n `159` status `ready` deltaP `20.423` edge `0.4586` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.2724` n `107` status `ready` deltaP `6.0664` edge `0.2066` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.2724` n `107` status `ready` deltaP `6.0664` edge `0.2066` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.0485` n `159` status `ready` deltaP `5.4081` edge `0.1977` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.9883` n `87` status `ready` deltaP `13.9487` edge `0.1715` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.9883` n `87` status `ready` deltaP `13.9487` edge `0.1715` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.3667` n `61` status `ready` deltaP `3.1707` edge `0.1274` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.102` n `87` status `ready` deltaP `43.2531` edge `0.0251` maxDD `-3.1066`
- `risk_on_and_context->fx_24h` score `1.102` n `87` status `ready` deltaP `43.2531` edge `0.0251` maxDD `-3.1066`
- `risk_on_high->crypto_alt_24h` score `1.0183` n `87` status `ready` deltaP `15.0862` edge `0.6997` maxDD `-42.2447`
- `risk_on_and_context->crypto_alt_24h` score `1.0183` n `87` status `ready` deltaP `15.0862` edge `0.6997` maxDD `-42.2447`
- `market_context_high->fx_24h` score `0.2118` n `131` status `ready` deltaP `28.8897` edge `0.0192` maxDD `-3.865`
- `news_risk_high->commodity_4h` score `0.2091` n `61` status `ready` deltaP `6.7298` edge `0.0236` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1887` n `159` status `ready` deltaP `9.4801` edge `0.0175` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1341` n `61` status `ready` deltaP `10.5008` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.0466` n `159` status `ready` deltaP `6.204` edge `0.0445` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
