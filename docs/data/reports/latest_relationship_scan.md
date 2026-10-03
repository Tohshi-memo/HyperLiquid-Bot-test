# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T09:52:25.775935+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.3246` n `50` status `ready` deltaP `10.855` edge `30.4596` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2672` n `50` status `ready` deltaP `12.0244` edge `24.4421` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.9092` n `50` status `ready` deltaP `26.6863` edge `1.0682` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `10.2949` n `50` status `ready` deltaP `34.3397` edge `0.7706` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.2504` n `71` status `ready` deltaP `38.8085` edge `0.6158` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.1874` n `69` status `ready` deltaP `28.8499` edge `0.7051` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7925` n `71` status `ready` deltaP `29.7875` edge `0.5852` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4348` n `50` status `ready` deltaP `18.0761` edge `0.5694` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2872` n `50` status `ready` deltaP `18.0974` edge `0.5322` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2871` n `69` status `ready` deltaP `32.9139` edge `0.1537` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9835` n `71` status `ready` deltaP `29.1037` edge `0.1992` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3454` n `50` status `ready` deltaP `15.3274` edge `0.2429` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.159` n `71` status `ready` deltaP `15.8235` edge `0.1933` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9977` n `50` status `ready` deltaP `13.6263` edge `0.204` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.975` n `50` status `ready` deltaP `33.3607` edge `0.039` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.8081` n `71` status `ready` deltaP `31.0073` edge `0.0535` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.2869` n `71` status `ready` deltaP `19.5082` edge `0.1021` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.7767` n `71` status `ready` deltaP `7.0739` edge `0.1528` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.4721` n `71` status `ready` deltaP `13.9434` edge `0.0659` maxDD `-0.8948`
- `market_context_high->fx_1h` score `1.4538` n `50` status `ready` deltaP `20.4096` edge `0.0115` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
