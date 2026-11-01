# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T00:22:26.835739+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6391`

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

- `market_context_high->unknown_24h` score `4060.9525` n `81` status `ready` deltaP `-9.9923` edge `338.5223` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `147.5505` n `81` status `ready` deltaP `0.5194` edge `12.3057` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.4848` n `108` status `ready` deltaP `-5.1951` edge `6.437` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `15.3008` n `91` status `ready` deltaP `36.0596` edge `1.1358` maxDD `-5.4237`
- `market_context_high->equity_24h` score `10.768` n `81` status `ready` deltaP `20.8719` edge `1.0339` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5924` n `108` status `ready` deltaP `21.3415` edge `0.4624` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.0386` n `81` status `ready` deltaP `44.0394` edge `0.1446` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.1966` n `81` status `ready` deltaP `22.337` edge `0.0717` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2895` n `81` status `ready` deltaP `15.9967` edge `0.0433` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.932` n `108` status `ready` deltaP `9.4755` edge `0.1099` maxDD `-3.9659`
- `market_context_high->fx_4h` score `0.7221` n `81` status `ready` deltaP `14.5475` edge `0.0023` maxDD `-0.1285`
- `market_context_high->metal_1h` score `0.7207` n `81` status `ready` deltaP `10.4199` edge `0.0196` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.549` n `81` status `ready` deltaP `13.3363` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.3437` n `81` status `ready` deltaP `1.3658` edge `0.1071` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.2758` n `81` status `ready` deltaP `-2.4766` edge `0.1912` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.0686` n `81` status `ready` deltaP `3.8349` edge `0.0684` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.4349` n `81` status `ready` deltaP `-0.2421` edge `0.0168` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4552` n `81` status `ready` deltaP `-0.6173` edge `0.0016` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.703` n `108` status `ready` deltaP `3.7037` edge `-0.0033` maxDD `-1.3981`
- `market_context_high->commodity_24h` score `-0.7637` n `81` status `ready` deltaP `21.1998` edge `0.0592` maxDD `-15.2087`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
