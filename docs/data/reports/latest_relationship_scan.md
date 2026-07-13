# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T19:52:42.893040+00:00`
- Price records: `672`
- Market context records: `6636`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.3423` n `203` status `ready` deltaP `-5.491` edge `0.3219` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.4618` n `189` status `ready` deltaP `-1.4958` edge `0.4481` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5715` n `189` status `ready` deltaP `10.1326` edge `0.1669` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1103` n `203` status `ready` deltaP `8.8139` edge `0.0497` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.105` n `203` status `ready` deltaP `6.2011` edge `0.043` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4758` n `203` status `ready` deltaP `0.8208` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6724` n `203` status `ready` deltaP `-1.4387` edge `-0.0083` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7237` n `203` status `ready` deltaP `-15.5766` edge `0.2841` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-0.8011` n `203` status `ready` deltaP `3.5014` edge `0.0126` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8059` n `203` status `ready` deltaP `10.7788` edge `0.0128` maxDD `-5.7046`
- `market_context_high->crypto_major_4h` score `-1.0632` n `203` status `ready` deltaP `10.5671` edge `0.1247` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1125` n `203` status `ready` deltaP `-2.9077` edge `0.0008` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.3971` n `203` status `ready` deltaP `-1.3119` edge `-0.0209` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.456` n `203` status `ready` deltaP `7.4124` edge `0.1041` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4895` n `203` status `ready` deltaP `4.5371` edge `0.0` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9141` n `203` status `ready` deltaP `1.5221` edge `0.0305` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3455` n `203` status `ready` deltaP `8.9834` edge `0.0049` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.5483` n `189` status `ready` deltaP `-2.8561` edge `0.0259` maxDD `-22.4543`
- `market_context_high->fx_24h` score `-6.1522` n `189` status `ready` deltaP `-10.1124` edge `-0.006` maxDD `-10.475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
