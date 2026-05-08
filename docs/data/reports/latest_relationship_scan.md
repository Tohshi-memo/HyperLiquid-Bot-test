# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T06:37:13.723353+00:00`
- Price records: `622`
- Market context records: `728`
- Flow alert records: `2056`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `11.9347` n `146` status `ready` deltaP `28.853` edge `0.8356` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3704` n `146` status `ready` deltaP `7.8702` edge `0.4832` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.2948` n `146` status `ready` deltaP `-0.1129` edge `0.1757` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3353` n `149` status `ready` deltaP `5.3925` edge `0.0082` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4509` n `155` status `ready` deltaP `2.6899` edge `0.0023` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4913` n `155` status `ready` deltaP `2.2959` edge `0.0412` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9295` n `155` status `ready` deltaP `0.704` edge `0.0032` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9846` n `149` status `ready` deltaP `17.6645` edge `0.1266` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0585` n `155` status `ready` deltaP `-0.7618` edge `-0.0021` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.071` n `155` status `ready` deltaP `5.6395` edge `-0.0026` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.1074` n `146` status `ready` deltaP `-1.8606` edge `0.1806` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.4507` n `155` status `ready` deltaP `4.1664` edge `-0.0172` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5571` n `155` status `ready` deltaP `-4.5213` edge `-0.0226` maxDD `-3.4946`
- `market_context_high->index_4h` score `-1.8638` n `149` status `ready` deltaP `0.9677` edge `-0.0095` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0166` n `149` status `ready` deltaP `3.1541` edge `0.0679` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8283` n `149` status `ready` deltaP `-2.0223` edge `-0.007` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2767` n `155` status `ready` deltaP `-4.6998` edge `-0.0458` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5721` n `149` status `ready` deltaP `-5.1272` edge `0.0866` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.963` n `149` status `ready` deltaP `4.4953` edge `-0.1724` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2391` n `146` status `ready` deltaP `-14.1448` edge `-0.0602` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
