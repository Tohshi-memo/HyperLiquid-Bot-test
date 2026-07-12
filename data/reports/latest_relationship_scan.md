# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T23:52:23.698570+00:00`
- Price records: `672`
- Market context records: `6552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4099` n `144` status `ready` deltaP `11.8934` edge `0.7849` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.5563` n `30` status `ready` deltaP `38.6484` edge `0.0433` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2708` n `30` status `ready` deltaP `27.8243` edge `0.0218` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8117` n `205` status `ready` deltaP `-5.6433` edge `0.2787` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3141` n `144` status `ready` deltaP `12.784` edge `0.2111` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.359` n `196` status `ready` deltaP `11.3956` edge `0.0254` maxDD `-0.7164`
- `news_risk_high->crypto_major_1h` score `0.278` n `30` status `ready` deltaP `1.8363` edge `0.0771` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `-0.1653` n `196` status `ready` deltaP `8.5739` edge `0.1003` maxDD `-8.0324`
- `news_risk_high->crypto_alt_1h` score `-0.35` n `30` status `ready` deltaP `-3.1836` edge `0.0273` maxDD `-2.0756`
- `news_risk_high->unknown_1h` score `-0.3658` n `30` status `ready` deltaP `5.1697` edge `-0.0278` maxDD `-0.9718`
- `market_context_high->equity_4h` score `-0.3824` n `196` status `ready` deltaP `9.893` edge `0.0549` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4156` n `205` status `ready` deltaP `-0.1431` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.5561` n `196` status `ready` deltaP `11.0192` edge `0.0843` maxDD `-12.6576`
- `market_context_high->index_1h` score `-0.5834` n `205` status `ready` deltaP `-0.9201` edge `0.0033` maxDD `-0.7564`
- `news_risk_high->commodity_4h` score `-0.6027` n `30` status `ready` deltaP `-4.1362` edge `-0.0002` maxDD `-1.2929`
- `market_context_high->crypto_major_1h` score `-0.6089` n `205` status `ready` deltaP `6.064` edge `0.0081` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.9173` n `205` status `ready` deltaP `-0.4995` edge `-0.0048` maxDD `-2.1314`
- `news_risk_high->index_1h` score `-0.9397` n `30` status `ready` deltaP `-6.3673` edge `-0.0217` maxDD `-1.1725`
- `market_context_high->crypto_alt_1h` score `-0.9792` n `205` status `ready` deltaP `5.7595` edge `0.0113` maxDD `-5.8368`
- `news_risk_high->metal_1h` score `-0.9867` n `30` status `ready` deltaP `-5.8084` edge `-0.0254` maxDD `-1.6568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
