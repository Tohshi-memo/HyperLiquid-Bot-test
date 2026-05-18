# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T16:00:08.439447+00:00`
- Price records: `672`
- Market context records: `1132`
- Flow alert records: `5162`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8733`

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

- `market_context_high->crypto_major_24h` score `19.838` n `150` status `ready` deltaP `42.2431` edge `1.4179` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `9.6687` n `150` status `ready` deltaP `18.6041` edge `0.8051` maxDD `-9.5387`
- `market_context_high->equity_24h` score `7.5395` n `150` status `ready` deltaP `18.0833` edge `0.5574` maxDD `-3.6396`
- `market_context_high->index_24h` score `5.8391` n `150` status `ready` deltaP `16.6944` edge `0.4061` maxDD `-2.1308`
- `market_context_high->metal_24h` score `5.6315` n `150` status `ready` deltaP `-1.8889` edge `0.6486` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.8814` n `168` status `ready` deltaP `10.3368` edge `0.1542` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8316` n `168` status `ready` deltaP `7.68` edge `0.0864` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4666` n `168` status `ready` deltaP `7.1963` edge `0.0226` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3784` n `168` status `ready` deltaP `3.0296` edge `0.0491` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1484` n `168` status `ready` deltaP `8.4652` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0761` n `168` status `ready` deltaP `8.4567` edge `0.1455` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.0754` n `168` status `ready` deltaP `6.9825` edge `0.0363` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2376` n `168` status `ready` deltaP `6.8007` edge `-0.0041` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2586` n `168` status `ready` deltaP `2.9441` edge `0.0431` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7199` n `168` status `ready` deltaP `0.9364` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7653` n `168` status `ready` deltaP `-2.0744` edge `-0.0035` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0175` n `168` status `ready` deltaP `5.6911` edge `0.1281` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4828` n `168` status `ready` deltaP `6.0903` edge `-0.0521` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-3.0308` n `150` status `ready` deltaP `2.7153` edge `0.0023` maxDD `-10.1706`
- `market_context_high->commodity_4h` score `-3.1469` n `168` status `ready` deltaP `-11.5781` edge `-0.0095` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
