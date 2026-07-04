# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T10:37:27.212077+00:00`
- Price records: `672`
- Market context records: `5654`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.4493` n `185` status `ready` deltaP `14.9549` edge `0.6123` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.7992` n `237` status `ready` deltaP `10.8521` edge `0.2235` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.6358` n `185` status `ready` deltaP `18.7631` edge `0.057` maxDD `-1.9947`
- `market_context_high->equity_4h` score `0.5001` n `237` status `ready` deltaP `7.6863` edge `0.1543` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.0145` n `237` status `ready` deltaP `6.6791` edge `0.1416` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2596` n `245` status `ready` deltaP `1.9864` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3628` n `245` status `ready` deltaP `5.6037` edge `0.0331` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5565` n `245` status `ready` deltaP `-0.5444` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.7184` n `245` status `ready` deltaP `0.8836` edge `0.0304` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8078` n `245` status `ready` deltaP `3.0203` edge `0.0371` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9327` n `245` status `ready` deltaP `0.5573` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9449` n `245` status `ready` deltaP `0.286` edge `-0.0041` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2598` n `237` status `ready` deltaP `2.2853` edge `0.0066` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0355` n `237` status `ready` deltaP `-1.689` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.349` n `185` status `ready` deltaP `9.2736` edge `0.0357` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7996` n `237` status `ready` deltaP `-2.1875` edge `-0.0345` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5304` n `185` status `ready` deltaP `4.0494` edge `0.0495` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4072` n `185` status `ready` deltaP `-13.3577` edge `-0.2527` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.8002` n `185` status `ready` deltaP `-14.9831` edge `-0.1059` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
