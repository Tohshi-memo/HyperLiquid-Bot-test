# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T18:07:37.957700+00:00`
- Price records: `672`
- Market context records: `5375`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11526`

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

- `market_context_high->unknown_24h` score `8.7811` n `179` status `ready` deltaP `17.0963` edge `0.6308` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.3183` n `179` status `ready` deltaP `22.2474` edge `0.7489` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.0932` n `205` status `ready` deltaP `14.1768` edge `0.3925` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.8354` n `179` status `ready` deltaP `13.5999` edge `0.7085` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.4607` n `205` status `ready` deltaP `10.7012` edge `0.2978` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6001` n `205` status `ready` deltaP `9.4513` edge `0.2342` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.202` n `179` status `ready` deltaP `17.01` edge `0.0963` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0675` n `205` status `ready` deltaP `6.1129` edge `0.0614` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0343` n `179` status `ready` deltaP `8.1267` edge `0.0325` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1026` n `205` status `ready` deltaP `4.3786` edge `0.0116` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.1873` n `205` status `ready` deltaP `3.576` edge `0.0851` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.199` n `205` status `ready` deltaP `1.4802` edge `0.0697` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4244` n `205` status `ready` deltaP `-0.6543` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6041` n `205` status `ready` deltaP `1.0311` edge `0.0103` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.8085` n `205` status `ready` deltaP `8.1402` edge `-0.0032` maxDD `-6.1421`
- `market_context_high->fx_4h` score `-1.1779` n `205` status `ready` deltaP `0.5488` edge `0.0011` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.2776` n `205` status `ready` deltaP `4.2683` edge `0.026` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5202` n `205` status `ready` deltaP `-3.7695` edge `-0.0071` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.591` n `205` status `ready` deltaP `-6.8293` edge `-0.0342` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.3407` n `179` status `ready` deltaP `13.0819` edge `0.3542` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
