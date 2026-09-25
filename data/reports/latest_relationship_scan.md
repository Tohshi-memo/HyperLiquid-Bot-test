# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T06:07:28.344451+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11162`

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

- `market_context_high->unknown_1h` score `85.0665` n `47` status `ready` deltaP `8.7687` edge `7.0375` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.3236` n `47` status `ready` deltaP `30.5962` edge `3.9456` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.1136` n `47` status `ready` deltaP `24.782` edge `2.5489` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0866` n `47` status `ready` deltaP `34.7628` edge `1.9777` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2151` n `47` status `ready` deltaP `38.4087` edge `0.4415` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.0336` n `116` status `ready` deltaP `2.6792` edge `0.4155` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7677` n `47` status `ready` deltaP `40.2667` edge `0.1527` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7623` n `54` status `ready` deltaP `30.3819` edge `0.1458` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9485` n `47` status `ready` deltaP `33.7215` edge `0.0363` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5679` n `47` status `ready` deltaP `17.1445` edge `0.1415` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.1782` n `116` status `ready` deltaP `10.8817` edge `0.1167` maxDD `-4.2849`
- `market_context_high->crypto_alt_4h` score `1.1366` n `47` status `ready` deltaP `9.688` edge `0.0969` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.981` n `47` status `ready` deltaP `11.7658` edge `0.0436` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_major_1h` score `0.382` n `116` status `ready` deltaP `7.2786` edge `0.058` maxDD `-3.3083`
- `market_context_high->fx_1h` score `0.3655` n `47` status `ready` deltaP `8.9119` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0609` n `47` status `ready` deltaP `4.026` edge `0.0126` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.037` n `116` status `ready` deltaP `8.5381` edge `0.0091` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.1014` n `47` status `ready` deltaP `2.6564` edge `0.0556` maxDD `-4.5405`
- `market_context_high->metal_4h` score `-0.2155` n `47` status `ready` deltaP `-2.2574` edge `0.0258` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
