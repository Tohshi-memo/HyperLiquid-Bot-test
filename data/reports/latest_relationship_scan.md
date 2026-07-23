# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T18:52:50.419404+00:00`
- Price records: `672`
- Market context records: `7696`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6063` n `132` status `ready` deltaP `19.396` edge `0.3054` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.309` n `133` status `ready` deltaP `15.7184` edge `0.1761` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1149` n `133` status `ready` deltaP `13.3076` edge `0.0483` maxDD `-1.5286`
- `market_context_high->equity_4h` score `0.8905` n `133` status `ready` deltaP `3.8042` edge `0.2801` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.8255` n `133` status `ready` deltaP `8.6569` edge `0.1228` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6987` n `133` status `ready` deltaP `8.7968` edge `0.0855` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.407` n `133` status `ready` deltaP `9.0949` edge `0.0163` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1833` n `133` status `ready` deltaP `3.8292` edge `0.033` maxDD `-1.4603`
- `market_context_high->index_4h` score `-0.0844` n `133` status `ready` deltaP `13.005` edge `0.0483` maxDD `-1.3325`
- `market_context_high->fx_24h` score `-0.1268` n `132` status `ready` deltaP `10.7249` edge `0.021` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2841` n `133` status `ready` deltaP `2.644` edge `0.0046` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.4124` n `133` status `ready` deltaP `2.1878` edge `0.0104` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5059` n `133` status `ready` deltaP `-0.377` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.7152` n `133` status `ready` deltaP `2.6812` edge `0.1316` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.7848` n `133` status `ready` deltaP `2.1656` edge `0.0205` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2386` n `133` status `ready` deltaP `-0.0765` edge `-0.0437` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4077` n `133` status `ready` deltaP `1.7479` edge `0.0765` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5202` n `133` status `ready` deltaP `-4.3147` edge `-0.0033` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7261` n `132` status `ready` deltaP `5.6858` edge `-0.0234` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2591` n `133` status `ready` deltaP `15.3023` edge `-0.1646` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
