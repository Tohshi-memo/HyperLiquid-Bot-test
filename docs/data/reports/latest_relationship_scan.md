# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T10:07:17.924850+00:00`
- Price records: `672`
- Market context records: `1107`
- Flow alert records: `5091`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `17.5475` n `150` status `ready` deltaP `38.0764` edge `1.2548` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.0626` n `150` status `ready` deltaP `14.4375` edge `0.6157` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.2219` n `150` status `ready` deltaP `15.6527` edge `0.4638` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.3689` n `150` status `ready` deltaP `-2.7569` edge `0.6325` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.9629` n `150` status `ready` deltaP `15.1319` edge `0.3435` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.771` n `168` status `ready` deltaP `10.3368` edge `0.145` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9469` n `168` status `ready` deltaP `8.747` edge `0.0889` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4654` n `168` status `ready` deltaP `7.4957` edge `0.0205` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2752` n `168` status `ready` deltaP `2.7302` edge `0.0425` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1364` n `168` status `ready` deltaP `8.3155` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1161` n `168` status `ready` deltaP `7.4316` edge `0.0367` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0527` n `168` status `ready` deltaP `8.4567` edge `0.1425` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1968` n `168` status `ready` deltaP `6.9504` edge `-0.0017` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2166` n `168` status `ready` deltaP `3.2435` edge `0.0446` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6708` n `168` status `ready` deltaP `1.851` edge `0.0013` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.717` n `168` status `ready` deltaP `-1.4756` edge `-0.0013` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0396` n `168` status `ready` deltaP `5.3862` edge `0.1273` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3293` n `168` status `ready` deltaP `7.0049` edge `-0.0454` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1305` n `168` status `ready` deltaP `-10.6635` edge `-0.0135` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3028` n `150` status `ready` deltaP `1.6944` edge `-0.0271` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
