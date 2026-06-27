# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T13:52:30.556171+00:00`
- Price records: `672`
- Market context records: `4939`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9408`

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

- `market_context_high->unknown_1h` score `19.7221` n `95` status `ready` deltaP `11.8153` edge `1.6065` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1239` n `95` status `ready` deltaP `28.4611` edge `0.872` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3514` n `95` status `ready` deltaP `21.4699` edge `0.5919` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1529` n `95` status `ready` deltaP `22.0507` edge `0.5843` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9604` n `86` status `ready` deltaP `26.5141` edge `0.3542` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8265` n `95` status `ready` deltaP `15.2487` edge `0.1887` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6404` n `95` status `ready` deltaP `12.6493` edge `0.1186` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.2464` n `95` status `ready` deltaP `7.7261` edge `0.1562` maxDD `-5.6406`
- `market_context_high->index_4h` score `1.0045` n `95` status `ready` deltaP `12.8819` edge `0.044` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8663` n `95` status `ready` deltaP `7.5953` edge `0.0789` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.6246` n `95` status `ready` deltaP `8.6432` edge `0.1247` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0952` n `95` status `ready` deltaP `4.4138` edge `0.0365` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4012` n `95` status `ready` deltaP `1.2654` edge `0.0061` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4175` n `95` status `ready` deltaP `1.434` edge `0.0124` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9568` n `95` status `ready` deltaP `6.5147` edge `-0.0045` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1019` n `95` status `ready` deltaP `-6.0799` edge `-0.0037` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5304` n `95` status `ready` deltaP `-9.116` edge `-0.0055` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.6394` n `86` status `ready` deltaP `-3.0725` edge `-0.0151` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.7486` n `86` status `ready` deltaP `15.94` edge `0.0089` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.1885` n `86` status `ready` deltaP `-10.239` edge `0.0147` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
