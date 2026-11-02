# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T02:37:01.609903+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7518.0823` n `50` status `ready` deltaP `1.3889` edge `626.4976` maxDD `0.0`
- `market_context_high->unknown_4h` score `385.9612` n `50` status `ready` deltaP `7.2988` edge `32.1191` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `34.9736` n `54` status `ready` deltaP `4.3081` edge `2.8968` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.5263` n `50` status `ready` deltaP `42.6181` edge `1.45` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.6673` n `94` status `ready` deltaP `33.2188` edge `1.0531` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.5186` n `50` status `ready` deltaP `45.4653` edge `0.2712` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.2382` n `50` status `ready` deltaP `49.1319` edge `0.1923` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1621` n `50` status `ready` deltaP `25.4451` edge `0.3733` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3814` n `50` status `ready` deltaP `30.3415` edge `0.2798` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.8804` n `50` status `ready` deltaP `36.7805` edge `0.0949` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.9695` n `50` status `ready` deltaP `2.7988` edge `0.299` maxDD `-2.283`
- `market_context_high->equity_1h` score `2.3488` n `54` status `ready` deltaP `8.8102` edge `0.1895` maxDD `-1.5336`
- `news_risk_high->crypto_alt_4h` score `2.287` n `126` status `ready` deltaP `9.3181` edge `0.2671` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `1.8968` n `50` status `ready` deltaP `7.2222` edge `0.2627` maxDD `-3.0799`
- `market_context_high->crypto_major_1h` score `1.7477` n `54` status `ready` deltaP `8.6605` edge `0.1388` maxDD `-1.4048`
- `market_context_high->crypto_alt_24h` score `1.6284` n `50` status `ready` deltaP `-6.9514` edge `0.4069` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.5235` n `54` status `ready` deltaP `4.0031` edge `0.1615` maxDD `-2.2314`
- `market_context_high->fx_1h` score `1.4379` n `54` status `ready` deltaP `19.4722` edge `0.0076` maxDD `-0.0736`
- `market_context_high->metal_4h` score `1.4012` n `50` status `ready` deltaP `17.1829` edge `0.0447` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.7145` n `54` status `ready` deltaP `9.4478` edge `0.0214` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
