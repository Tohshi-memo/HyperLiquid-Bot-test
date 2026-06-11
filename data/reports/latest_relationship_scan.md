# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T18:37:51.782866+00:00`
- Price records: `672`
- Market context records: `3610`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `44.6003` n `32` status `ready` deltaP `48.2639` edge `3.3992` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `44.6003` n `32` status `ready` deltaP `48.2639` edge `3.3992` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `41.4114` n `32` status `ready` deltaP `50.3472` edge `3.1153` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `41.4114` n `32` status `ready` deltaP `50.3472` edge `3.1153` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `37.5652` n `32` status `ready` deltaP `47.3958` edge `2.8296` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `37.5652` n `32` status `ready` deltaP `47.3958` edge `2.8296` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.147` n `32` status `ready` deltaP `50.3472` edge `1.6766` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.147` n `32` status `ready` deltaP `50.3472` edge `1.6766` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.0898` n `32` status `ready` deltaP `35.9375` edge `1.2107` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.0898` n `32` status `ready` deltaP `35.9375` edge `1.2107` maxDD `-0.7574`
- `market_context_high->equity_24h` score `15.6814` n `158` status `ready` deltaP `26.9295` edge `1.7685` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.1373` n `32` status `ready` deltaP `24.3902` edge `1.0444` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1373` n `32` status `ready` deltaP `24.3902` edge `1.0444` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.7971` n `158` status `ready` deltaP `35.1573` edge `1.0537` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `9.2777` n `158` status `ready` deltaP `14.0471` edge `1.4526` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.6328` n `158` status `ready` deltaP `29.8457` edge `1.1054` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.8289` n `32` status `ready` deltaP `4.9543` edge `0.5538` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.8289` n `32` status `ready` deltaP `4.9543` edge `0.5538` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `3.6919` n `158` status `ready` deltaP `8.1157` edge `1.0578` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.5168` n `32` status `ready` deltaP `14.253` edge `0.4693` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
