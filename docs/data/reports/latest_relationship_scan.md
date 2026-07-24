# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T14:22:35.107137+00:00`
- Price records: `672`
- Market context records: `7782`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.2417` n `132` status `ready` deltaP `27.7584` edge `0.5526` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4577` n `133` status `ready` deltaP `13.7923` edge `0.2386` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0118` n `133` status `ready` deltaP `13.0082` edge `0.0417` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.7587` n `133` status `ready` deltaP `13.2794` edge `0.1465` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.7376` n `132` status `ready` deltaP `24.1395` edge `0.0424` maxDD `-3.0343`
- `market_context_high->equity_4h` score `0.6943` n `133` status `ready` deltaP `2.581` edge `0.2631` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.5702` n `133` status `ready` deltaP `7.7457` edge `0.0818` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.5688` n `133` status `ready` deltaP `7.7423` edge `0.1075` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.3242` n `133` status `ready` deltaP `8.194` edge `0.0154` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2123` n `133` status `ready` deltaP `6.622` edge `0.0329` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1676` n `133` status `ready` deltaP `4.2783` edge `0.0287` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0307` n `133` status `ready` deltaP `4.8963` edge `0.0107` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2263` n `133` status `ready` deltaP `10.7114` edge `0.0454` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.363` n `133` status `ready` deltaP `1.2746` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.6953` n `132` status `ready` deltaP `10.2154` edge `0.0323` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9393` n `133` status `ready` deltaP `0.5189` edge `0.0186` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3556` n `133` status `ready` deltaP `-1.8682` edge `0.0015` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5862` n `133` status `ready` deltaP `0.071` edge `0.0728` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.7886` n `132` status `ready` deltaP `-11.1366` edge `0.0552` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.1122` n `133` status `ready` deltaP `-0.0765` edge `-0.1165` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
