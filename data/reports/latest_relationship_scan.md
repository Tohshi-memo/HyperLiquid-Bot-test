# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T00:07:17.393066+00:00`
- Price records: `672`
- Market context records: `1269`
- Flow alert records: `5561`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9821` n `128` status `ready` deltaP `41.5798` edge `1.3345` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.0196` n `128` status `ready` deltaP `5.3819` edge `0.9658` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.5044` n `128` status `ready` deltaP `24.7395` edge `0.7454` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.2868` n `128` status `ready` deltaP `6.2881` edge `0.7703` maxDD `-6.7322`
- `market_context_high->index_24h` score `4.9535` n `128` status `ready` deltaP `26.3889` edge `0.3455` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.8084` n `128` status `ready` deltaP `19.3788` edge `0.2545` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.7503` n `128` status `ready` deltaP `24.4792` edge `0.5503` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.3178` n `128` status `ready` deltaP `1.5625` edge `0.4557` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `2.0758` n `128` status `ready` deltaP `-11.6319` edge `0.3987` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.9256` n `128` status `ready` deltaP `15.4153` edge `0.126` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.841` n `128` status `ready` deltaP `17.8926` edge `0.0939` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.7049` n `139` status `ready` deltaP `9.7252` edge `0.0256` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6875` n `139` status `ready` deltaP `6.4898` edge `0.0509` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.5104` n `139` status `ready` deltaP `12.4155` edge `0.0208` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.3862` n `128` status `ready` deltaP `8.8987` edge `0.1823` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.0547` n `128` status `ready` deltaP `3.2119` edge `0.0296` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.2121` n `128` status `ready` deltaP `10.08` edge `0.2021` maxDD `-16.7194`
- `market_context_high->crypto_alt_1h` score `-0.2897` n `139` status `ready` deltaP `1.6823` edge `0.0387` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.4063` n `139` status `ready` deltaP `2.1314` edge `-0.0025` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.5709` n `139` status `ready` deltaP `1.2288` edge `0.0096` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
