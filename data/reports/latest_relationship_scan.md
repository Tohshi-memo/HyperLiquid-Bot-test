# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T18:22:26.554756+00:00`
- Price records: `672`
- Market context records: `7694`
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

- `market_context_high->equity_24h` score `3.5727` n `132` status `ready` deltaP `19.396` edge `0.3026` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.2596` n `133` status `ready` deltaP `15.5659` edge `0.173` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1005` n `133` status `ready` deltaP `13.1579` edge `0.0481` maxDD `-1.5286`
- `market_context_high->equity_4h` score `0.8716` n `133` status `ready` deltaP `3.6513` edge `0.2787` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.7774` n `133` status `ready` deltaP `8.5045` edge `0.1198` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6746` n `133` status `ready` deltaP `8.6466` edge `0.0845` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.407` n `133` status `ready` deltaP `9.0949` edge `0.0163` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1641` n `133` status `ready` deltaP `3.6795` edge `0.0324` maxDD `-1.4603`
- `market_context_high->index_4h` score `-0.0931` n `133` status `ready` deltaP `12.8521` edge `0.0482` maxDD `-1.3325`
- `market_context_high->fx_24h` score `-0.1497` n `132` status `ready` deltaP `10.3764` edge `0.0204` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3153` n `133` status `ready` deltaP `2.3437` edge `0.004` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.4331` n `133` status `ready` deltaP `2.0349` edge `0.0097` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4819` n `133` status `ready` deltaP `-0.0767` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.7464` n `133` status `ready` deltaP `2.6812` edge `0.129` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.7836` n `133` status `ready` deltaP `2.1656` edge `0.0206` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2554` n `133` status `ready` deltaP `-0.2262` edge `-0.0441` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4113` n `133` status `ready` deltaP `1.7479` edge `0.0762` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5043` n `133` status `ready` deltaP `-4.0088` edge `-0.0033` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7261` n `132` status `ready` deltaP `5.6858` edge `-0.0234` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2711` n `133` status `ready` deltaP `15.3023` edge `-0.1656` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
