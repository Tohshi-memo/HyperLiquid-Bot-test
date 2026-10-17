# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T12:52:27.279954+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0293` n `54` status `ready` deltaP `38.5017` edge `0.3291` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0293` n `54` status `ready` deltaP `38.5017` edge `0.3291` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.1834` n `151` status `ready` deltaP `19.8312` edge `0.4319` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `4.2194` n `77` status `ready` deltaP `24.3982` edge `0.2909` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2194` n `77` status `ready` deltaP `24.3982` edge `0.2909` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `4.1302` n `151` status `ready` deltaP `11.9943` edge `0.5004` maxDD `-11.2277`
- `market_context_high->crypto_major_1h` score `0.5905` n `163` status `ready` deltaP `5.1853` edge `0.0952` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3245` n `151` status `ready` deltaP `12.6565` edge `0.0472` maxDD `-1.6961`
- `market_context_high->crypto_alt_1h` score `0.2641` n `163` status `ready` deltaP `6.7117` edge `0.1087` maxDD `-5.8485`
- `risk_on_high->index_1h` score `0.0681` n `89` status `ready` deltaP `5.8171` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0681` n `89` status `ready` deltaP `5.8171` edge `0.0053` maxDD `-0.7394`
- `risk_on_high->crypto_alt_4h` score `-0.1725` n `77` status `ready` deltaP `3.0152` edge `0.1931` maxDD `-11.1585`
- `risk_on_and_context->crypto_alt_4h` score `-0.1725` n `77` status `ready` deltaP `3.0152` edge `0.1931` maxDD `-11.1585`
- `market_context_high->index_1h` score `-0.1955` n `163` status `ready` deltaP `6.789` edge `0.0045` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.234` n `163` status `ready` deltaP `7.2811` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.3113` n `89` status `ready` deltaP `0.1839` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3113` n `89` status `ready` deltaP `0.1839` edge `-0.0031` maxDD `-0.376`
- `market_context_high->equity_4h` score `-0.3815` n `151` status `ready` deltaP `13.7847` edge `0.2018` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.3978` n `163` status `ready` deltaP `9.4917` edge `0.0367` maxDD `-7.0778`
- `risk_on_high->equity_1h` score `-0.4756` n `89` status `ready` deltaP `9.6434` edge `0.0257` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
