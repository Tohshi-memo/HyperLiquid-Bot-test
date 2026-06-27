# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T18:37:25.599610+00:00`
- Price records: `672`
- Market context records: `4960`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_1h` score `19.4638` n `95` status `ready` deltaP `9.261` edge `1.602` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.0959` n `94` status `ready` deltaP `28.5612` edge `0.869` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2347` n `94` status `ready` deltaP `21.4355` edge `0.5824` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.9826` n `94` status `ready` deltaP `21.8864` edge `0.5712` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.766` n `91` status `ready` deltaP `26.7991` edge `0.3361` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.6815` n `94` status `ready` deltaP `13.8265` edge `0.1861` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5107` n `94` status `ready` deltaP `12.0232` edge `0.1203` maxDD `-1.9651`
- `market_context_high->equity_1h` score `1.0359` n `95` status `ready` deltaP `9.5509` edge `0.08` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9696` n `95` status `ready` deltaP `9.532` edge `0.1646` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.9094` n `94` status `ready` deltaP `11.7086` edge `0.0439` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.7529` n `95` status `ready` deltaP `10.2994` edge `0.1301` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.2397` n `95` status `ready` deltaP `6.0699` edge `0.0375` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.301` n `95` status `ready` deltaP `3.5392` edge `0.0133` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3646` n `95` status `ready` deltaP `1.7145` edge `0.0078` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0427` n `94` status `ready` deltaP `6.5613` edge `-0.0061` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1239` n `94` status `ready` deltaP `-6.383` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4908` n `91` status `ready` deltaP `-1.6502` edge `-0.0122` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5125` n `95` status `ready` deltaP `-9.2657` edge `-0.0043` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9995` n `91` status `ready` deltaP `19.6485` edge `0.0466` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9271` n `91` status `ready` deltaP `-9.3407` edge `0.0305` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
