# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T08:22:26.211408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3863`

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

- `news_risk_high->unknown_4h` score `3257.7835` n `31` status `ready` deltaP `3.4815` edge `271.4644` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3228.5689` n `31` status `ready` deltaP `1.6322` edge `269.0541` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `98.277` n `31` status `ready` deltaP `1.6322` edge `8.1883` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `39.4358` n `31` status `ready` deltaP `46.0069` edge `2.9796` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.1192` n `31` status `ready` deltaP `46.875` edge `2.8641` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.4932` n `31` status `ready` deltaP `46.1806` edge `2.3999` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.018` n `31` status `ready` deltaP `27.675` edge `0.8207` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6786` n `31` status `ready` deltaP `38.9015` edge `0.6786` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.4734` n `31` status `ready` deltaP `32.5549` edge `0.5999` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9336` n `31` status `ready` deltaP `18.6074` edge `0.9066` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4989` n `31` status `ready` deltaP `47.3958` edge `0.2256` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2829` n `31` status `ready` deltaP `45.0101` edge `0.153` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.777` n `31` status `ready` deltaP `20.5862` edge `0.1962` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5222` n `31` status `ready` deltaP `37.8344` edge `0.0673` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7453` n `31` status `ready` deltaP `32.4416` edge `0.021` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5016` n `31` status `ready` deltaP `10.1603` edge `0.2991` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.3087` n `31` status `ready` deltaP `13.4537` edge `0.242` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1238` n `31` status `ready` deltaP `26.9621` edge `0.0257` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5173` n `31` status `ready` deltaP `29.5827` edge `0.0252` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1093` n `31` status `ready` deltaP `16.7781` edge `0.0861` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
