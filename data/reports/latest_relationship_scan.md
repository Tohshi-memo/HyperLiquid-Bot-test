# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T13:22:25.781031+00:00`
- Price records: `672`
- Market context records: `7778`
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

- `market_context_high->equity_24h` score `6.8511` n `132` status `ready` deltaP `27.0615` edge `0.5247` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3577` n `133` status `ready` deltaP `13.0979` edge `0.2349` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9386` n `133` status `ready` deltaP `12.7088` edge `0.0376` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.692` n `132` status `ready` deltaP `23.4426` edge `0.0412` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.5419` n `133` status `ready` deltaP `12.6696` edge `0.1325` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.4449` n `133` status `ready` deltaP `1.9694` edge `0.2352` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3866` n `133` status `ready` deltaP `7.4454` edge `0.0685` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.3436` n `133` status `ready` deltaP `7.1325` edge `0.0928` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.2834` n `133` status `ready` deltaP `7.8937` edge `0.014` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2111` n `133` status `ready` deltaP `6.622` edge `0.0328` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1076` n `133` status `ready` deltaP `4.1286` edge `0.0247` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0523` n `133` status `ready` deltaP `4.7461` edge `0.0099` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2846` n `133` status `ready` deltaP `10.0998` edge `0.042` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.363` n `133` status `ready` deltaP `1.2746` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.8147` n `132` status `ready` deltaP `9.5185` edge `0.027` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9645` n `133` status `ready` deltaP `0.3692` edge `0.0175` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3921` n `133` status `ready` deltaP `-2.4798` edge `0.0009` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6734` n `133` status `ready` deltaP `-0.5387` edge `0.0696` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.8592` n `132` status `ready` deltaP `-11.8335` edge `0.0508` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.1889` n `133` status `ready` deltaP `-0.6753` edge `-0.1189` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
