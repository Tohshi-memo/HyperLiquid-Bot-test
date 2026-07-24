# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T12:37:30.051242+00:00`
- Price records: `672`
- Market context records: `7775`
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

- `market_context_high->equity_24h` score `6.7265` n `132` status `ready` deltaP `26.5389` edge `0.5178` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.2909` n `133` status `ready` deltaP `12.577` edge `0.2328` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9458` n `133` status `ready` deltaP `12.7088` edge `0.0382` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.6571` n `132` status `ready` deltaP `22.92` edge `0.0402` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4695` n `133` status `ready` deltaP `12.3647` edge `0.1285` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.419` n `133` status `ready` deltaP `7.5955` edge `0.0702` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3767` n `133` status `ready` deltaP `1.6636` edge `0.2285` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.2978` n `133` status `ready` deltaP `8.0438` edge `0.0142` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2508` n `133` status `ready` deltaP `6.8276` edge `0.0871` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.2111` n `133` status `ready` deltaP `6.622` edge `0.0328` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1052` n `133` status `ready` deltaP `4.1286` edge `0.0245` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0571` n `133` status `ready` deltaP `4.7461` edge `0.0095` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.3083` n `133` status `ready` deltaP `9.794` edge `0.041` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.387` n `133` status `ready` deltaP `0.9743` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.9117` n `132` status `ready` deltaP `8.9959` edge `0.0224` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9525` n `133` status `ready` deltaP `0.5189` edge `0.0175` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.4198` n `133` status `ready` deltaP `-2.9385` edge `0.0004` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.7158` n `133` status `ready` deltaP `-0.8436` edge `0.0681` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.9019` n `132` status `ready` deltaP `-12.3562` edge `0.0488` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2321` n `133` status `ready` deltaP `-1.1244` edge `-0.1195` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
