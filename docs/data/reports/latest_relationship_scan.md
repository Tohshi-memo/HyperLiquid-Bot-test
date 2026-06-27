# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T17:51:51.663200+00:00`
- Price records: `672`
- Market context records: `4957`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_1h` score `19.8839` n `94` status `ready` deltaP `9.772` edge `1.6336` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.2909` n `93` status `ready` deltaP `28.8241` edge `0.8835` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3044` n `93` status `ready` deltaP `21.7218` edge `0.5863` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0649` n `93` status `ready` deltaP `22.1954` edge `0.576` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8154` n `91` status `ready` deltaP `27.1463` edge `0.3379` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7188` n `93` status `ready` deltaP `14.067` edge `0.1876` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5834` n `93` status `ready` deltaP `12.1721` edge `0.1212` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.0223` n `94` status `ready` deltaP `9.9758` edge `0.1684` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0079` n `94` status `ready` deltaP `9.1254` edge `0.0805` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.9277` n `93` status `ready` deltaP `11.8919` edge `0.0442` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.8032` n `94` status `ready` deltaP `10.788` edge `0.1333` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1997` n `94` status `ready` deltaP `5.5548` edge `0.0376` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3338` n `94` status `ready` deltaP `2.908` edge `0.0133` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.337` n `94` status `ready` deltaP `2.2296` edge `0.0079` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.9646` n `93` status `ready` deltaP `7.0761` edge `-0.0053` maxDD `-4.7807`
- `market_context_high->fx_4h` score `-1.1483` n `93` status `ready` deltaP `-6.8368` edge `-0.0046` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4395` n `91` status `ready` deltaP `-1.1294` edge `-0.0114` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5316` n `94` status `ready` deltaP `-9.4885` edge `-0.0044` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9959` n `91` status `ready` deltaP `19.6485` edge `0.0469` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.877` n `91` status `ready` deltaP `-8.8199` edge `0.0312` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
