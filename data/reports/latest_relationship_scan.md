# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T10:37:17.363962+00:00`
- Price records: `672`
- Market context records: `1211`
- Flow alert records: `5393`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.7643` n `129` status `ready` deltaP `44.0528` edge `1.3832` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.3136` n `129` status `ready` deltaP `2.8526` edge `0.7121` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.0752` n `129` status `ready` deltaP `21.98` edge `0.6447` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.873` n `129` status `ready` deltaP `-2.7777` edge `0.6561` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.3676` n `129` status `ready` deltaP `-3.452` edge `0.5537` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8714` n `129` status `ready` deltaP `14.8965` edge `0.2063` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1463` n `129` status `ready` deltaP `18.314` edge `0.1654` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.8435` n `129` status `ready` deltaP `18.4997` edge `0.3457` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9911` n `129` status `ready` deltaP `10.029` edge `0.0635` maxDD `-0.4881`
- `market_context_high->index_4h` score `0.9837` n `129` status `ready` deltaP `10.6766` edge `0.0791` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5819` n `129` status `ready` deltaP `9.1921` edge `0.0189` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5292` n `129` status `ready` deltaP `4.947` edge `0.048` maxDD `-1.2834`
- `market_context_high->metal_1h` score `-0.0829` n `129` status `ready` deltaP `9.4544` edge `-0.0089` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1795` n `129` status `ready` deltaP `4.5467` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.214` n `129` status `ready` deltaP `5.4571` edge `0.1283` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3964` n `129` status `ready` deltaP `0.2484` edge `0.0318` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4111` n `129` status `ready` deltaP `2.7399` edge `0.0056` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.4233` n `129` status `ready` deltaP `-0.1817` edge `0.2389` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.7823` n `129` status `ready` deltaP `-2.5368` edge `0.0132` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.1337` n `129` status `ready` deltaP `10.9389` edge `-0.0243` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
