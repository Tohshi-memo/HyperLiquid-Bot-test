# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T21:52:26.841102+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12010`

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

- `news_risk_high->unknown_24h` score `817.2875` n `76` status `ready` deltaP `-0.9686` edge `68.1182` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.383` n `47` status `ready` deltaP `8.3196` edge `5.9002` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4399` n `47` status `ready` deltaP `30.0753` edge `4.0421` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9108` n `47` status `ready` deltaP `24.782` edge `2.532` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2641` n `47` status `ready` deltaP `33.7212` edge `1.9161` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6413` n `47` status `ready` deltaP `34.4156` edge `0.4203` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9067` n `47` status `ready` deltaP `33.1487` edge `0.1284` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7763` n `47` status `ready` deltaP `17.7542` edge `0.1548` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.614` n `47` status `ready` deltaP `30.2154` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3749` n `47` status `ready` deltaP `11.2124` edge `0.1066` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1188` n `47` status `ready` deltaP `12.8137` edge `0.0481` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9759` n `111` status `ready` deltaP `9.4784` edge `0.1092` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8409` n `47` status `ready` deltaP `13.2628` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.4991` n `76` status `ready` deltaP `21.8385` edge `0.0845` maxDD `-6.9545`
- `market_context_high->crypto_major_4h` score `0.3696` n `47` status `ready` deltaP `4.5375` edge `0.091` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3303` n `47` status `ready` deltaP `5.0516` edge `0.0756` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.1095` n `111` status `ready` deltaP `4.3616` edge `0.0556` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0721` n `111` status `ready` deltaP `3.6131` edge `0.0359` maxDD `-2.0595`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
