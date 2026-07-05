# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T19:52:25.526949+00:00`
- Price records: `672`
- Market context records: `5806`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.3077` n `248` status `ready` deltaP `15.3954` edge `0.4309` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.1236` n `294` status `ready` deltaP `5.5148` edge `0.1168` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.22` n `294` status `ready` deltaP `2.8708` edge `0.0012` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6382` n `294` status `ready` deltaP `2.2852` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6452` n `294` status `ready` deltaP `0.108` edge `0.0034` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6675` n `294` status `ready` deltaP `2.8006` edge `0.0264` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.6975` n `294` status `ready` deltaP `-1.7954` edge `-0.0044` maxDD `-3.1777`
- `market_context_high->crypto_major_1h` score `-0.9364` n `294` status `ready` deltaP `2.9655` edge `0.0343` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1384` n `294` status `ready` deltaP `1.1966` edge `0.0306` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2591` n `294` status `ready` deltaP `-0.2686` edge `0.0091` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.3177` n `248` status `ready` deltaP `11.2791` edge `0.0338` maxDD `-5.2348`
- `market_context_high->fx_4h` score `-1.4235` n `294` status `ready` deltaP `1.2319` edge `0.0042` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.33` n `294` status `ready` deltaP `-4.4674` edge `-0.0459` maxDD `-10.5095`
- `market_context_high->index_24h` score `-2.8057` n `248` status `ready` deltaP `3.7131` edge `0.03` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8082` n `294` status `ready` deltaP `7.848` edge `0.1509` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-3.0594` n `294` status `ready` deltaP `-2.4888` edge `-0.0205` maxDD `-10.0954`
- `market_context_high->crypto_alt_4h` score `-4.445` n `294` status `ready` deltaP `5.5843` edge `0.0932` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.0082` n `248` status `ready` deltaP `-5.4548` edge `-0.2412` maxDD `-22.0844`
- `market_context_high->commodity_24h` score `-9.6769` n `248` status `ready` deltaP `-13.1496` edge `-0.0706` maxDD `-34.5179`
- `market_context_high->crypto_major_24h` score `-10.5656` n `248` status `ready` deltaP `-1.5345` edge `-0.2339` maxDD `-34.2402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
