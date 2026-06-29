# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T02:37:29.177723+00:00`
- Price records: `672`
- Market context records: `5102`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `18.7727` n `79` status `ready` deltaP `27.547` edge `1.415` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.3136` n `109` status `ready` deltaP `22.4883` edge `0.6451` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.9835` n `121` status `ready` deltaP `4.3958` edge `0.6168` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.8941` n `109` status `ready` deltaP `13.8985` edge `0.4383` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.2144` n `109` status `ready` deltaP `12.2161` edge `0.4317` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.8208` n `109` status `ready` deltaP `9.4778` edge `0.1677` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.54` n `121` status `ready` deltaP `7.318` edge `0.1166` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4432` n `121` status `ready` deltaP `8.5997` edge `0.0588` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.4311` n `121` status `ready` deltaP `8.1321` edge `0.1256` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3128` n `121` status `ready` deltaP `9.1144` edge `0.029` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.059` n `121` status `ready` deltaP `4.6952` edge `0.0115` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.1117` n `109` status `ready` deltaP `5.9493` edge `0.0325` maxDD `-1.9189`
- `market_context_high->metal_4h` score `-0.4405` n `109` status `ready` deltaP `3.1887` edge `0.0633` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.858` n `121` status `ready` deltaP `-6.6598` edge `-0.0015` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.8648` n `121` status `ready` deltaP `0.5567` edge `0.0` maxDD `-2.062`
- `market_context_high->fx_24h` score `-1.6071` n `79` status `ready` deltaP `-3.6634` edge `-0.0083` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6745` n `79` status `ready` deltaP `7.7004` edge `0.0302` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.8772` n `109` status `ready` deltaP `-6.5758` edge `-0.0053` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1432` n `109` status `ready` deltaP `2.2684` edge `-0.0233` maxDD `-7.3003`
- `market_context_high->metal_24h` score `-4.5457` n `79` status `ready` deltaP `-6.5995` edge `0.0067` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
