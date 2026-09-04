# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T08:52:29.761443+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.5777` n `133` status `ready` deltaP `8.5412` edge `1.7197` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.5777` n `133` status `ready` deltaP `8.5412` edge `1.7197` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `14.0096` n `181` status `ready` deltaP `11.7606` edge `1.1586` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.2456` n `133` status `ready` deltaP `-1.0536` edge `1.0852` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.2456` n `133` status `ready` deltaP `-1.0536` edge `1.0852` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.1613` n `192` status `ready` deltaP `0.1996` edge `0.9085` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.7278` n `163` status `ready` deltaP `16.837` edge `0.4663` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.9186` n `64` status `ready` deltaP `8.1936` edge `0.0452` maxDD `-0.5286`
- `risk_on_high->equity_24h` score `0.7901` n `133` status `ready` deltaP `12.1136` edge `0.3996` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.7901` n `133` status `ready` deltaP `12.1136` edge `0.3996` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.1187` n `133` status `ready` deltaP `12.4128` edge `0.0037` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1187` n `133` status `ready` deltaP `12.4128` edge `0.0037` maxDD `-1.699`
- `news_risk_high->commodity_24h` score `0.0117` n `64` status `ready` deltaP `4.8611` edge `-0.0125` maxDD `-0.1812`
- `news_risk_high->commodity_1h` score `-0.0505` n `64` status `ready` deltaP `5.7635` edge `0.002` maxDD `-0.9036`
- `news_risk_high->index_1h` score `-0.0862` n `64` status `ready` deltaP `4.1542` edge `-0.0034` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.2923` n `192` status `ready` deltaP `6.8363` edge `0.0026` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.3253` n `133` status `ready` deltaP `4.1522` edge `0.0469` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3253` n `133` status `ready` deltaP `4.1522` edge `0.0469` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
