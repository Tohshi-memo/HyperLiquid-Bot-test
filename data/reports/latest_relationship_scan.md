# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T18:37:43.296070+00:00`
- Price records: `672`
- Market context records: `5274`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.1581` n `153` status `ready` deltaP `29.0747` edge `1.995` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.6736` n `153` status `ready` deltaP `25.7353` edge `0.8829` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2746` n `169` status `ready` deltaP `15.6904` edge `0.4157` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7203` n `169` status `ready` deltaP `14.4709` edge `0.4428` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.6926` n `153` status `ready` deltaP `19.9653` edge `0.7375` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.0466` n `169` status `ready` deltaP `15.2755` edge `0.0876` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8154` n `169` status `ready` deltaP `9.1076` edge `0.1711` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5781` n `153` status `ready` deltaP `13.3068` edge `0.049` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4799` n `178` status `ready` deltaP `4.7921` edge `0.1042` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2686` n `153` status `ready` deltaP `21.1703` edge `0.0568` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.247` n `178` status `ready` deltaP `5.6146` edge `0.1077` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.0335` n `178` status `ready` deltaP `6.4826` edge `0.0561` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.009` n `178` status `ready` deltaP `5.9578` edge `0.0114` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2961` n `178` status `ready` deltaP `3.4818` edge `0.0113` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3348` n `178` status `ready` deltaP `0.2641` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5185` n `169` status `ready` deltaP `6.4096` edge `0.0258` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6741` n `169` status `ready` deltaP `2.0692` edge `0.0027` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4455` n `178` status `ready` deltaP `-3.2211` edge `-0.0072` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6087` n `169` status `ready` deltaP `-2.2496` edge `0.0091` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.1099` n `178` status `ready` deltaP `6.4086` edge `-0.1544` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
