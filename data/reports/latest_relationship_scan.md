# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T12:37:26.139647+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `99.5862` n `47` status `ready` deltaP `10.2657` edge `8.2375` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.6688` n `46` status `ready` deltaP `30.8953` edge `3.4487` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `29.5374` n `46` status `ready` deltaP `25.8681` edge `2.289` maxDD `0.0`
- `market_context_high->equity_24h` score `25.1586` n `46` status `ready` deltaP `28.2911` edge `1.918` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.9276` n `103` status `ready` deltaP `3.2043` edge `1.7102` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.2304` n `46` status `ready` deltaP `36.9716` edge `0.4481` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `7.2753` n `103` status `ready` deltaP `0.6254` edge `1.3034` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.6198` n `46` status `ready` deltaP `31.2953` edge `0.1164` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.076` n `47` status `ready` deltaP `34.941` edge `0.0388` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6841` n `47` status `ready` deltaP `17.9067` edge `0.1461` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.3283` n `118` status `ready` deltaP `12.6535` edge `0.1587` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.9994` n `118` status `ready` deltaP `14.7493` edge `0.1118` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6705` n `114` status `ready` deltaP `24.5561` edge `0.0391` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.334` n `103` status `ready` deltaP `30.532` edge `0.1306` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.3256` n `103` status `ready` deltaP `17.4976` edge `0.1117` maxDD `-2.431`
- `market_context_high->index_1h` score `1.029` n `47` status `ready` deltaP `15.3586` edge `0.0112` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `1.0197` n `103` status `ready` deltaP `23.1695` edge `0.1211` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.9523` n `47` status `ready` deltaP `11.167` edge `0.0452` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.8618` n `114` status `ready` deltaP `13.091` edge `0.1977` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.764` n `118` status `ready` deltaP `16.0053` edge `0.0163` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
