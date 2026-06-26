# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T16:52:27.165992+00:00`
- Price records: `672`
- Market context records: `4846`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.4302` n `110` status `ready` deltaP `9.7115` edge `1.0962` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.1185` n `99` status `ready` deltaP `26.9586` edge `0.8156` maxDD `-2.5027`
- `market_context_high->unknown_24h` score `5.0491` n `90` status `ready` deltaP `24.1667` edge `0.2939` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `4.5863` n `99` status `ready` deltaP `18.0771` edge `0.3969` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `4.5563` n `99` status `ready` deltaP `14.551` edge `0.4051` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.5133` n `99` status `ready` deltaP `11.9011` edge `0.113` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.4305` n `110` status `ready` deltaP `6.1704` edge `0.1179` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4027` n `110` status `ready` deltaP `8.1709` edge `0.0994` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.3561` n `99` status `ready` deltaP `8.8523` edge `0.0329` maxDD `-0.7006`
- `market_context_high->equity_4h` score `0.3311` n `99` status `ready` deltaP `10.8155` edge `0.1085` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.1747` n `110` status `ready` deltaP `4.2352` edge `0.0539` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.1916` n `99` status `ready` deltaP `6.3178` edge `0.0101` maxDD `-0.788`
- `market_context_high->metal_1h` score `-0.198` n `110` status `ready` deltaP `0.4055` edge `0.0299` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2215` n `110` status `ready` deltaP `3.2825` edge `0.0157` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.4926` n `99` status `ready` deltaP `9.8039` edge `0.0108` maxDD `-4.377`
- `market_context_high->index_1h` score `-0.532` n `110` status `ready` deltaP `-0.2885` edge `0.0092` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.331` n `110` status `ready` deltaP `-6.8672` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8515` n `90` status `ready` deltaP `-6.3542` edge `-0.0109` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.7566` n `90` status `ready` deltaP `-8.2292` edge `-0.1539` maxDD `-24.085`
- `market_context_high->commodity_24h` score `-5.3476` n `90` status `ready` deltaP `10.9722` edge `-0.0079` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
