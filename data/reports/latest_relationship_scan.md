# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T09:37:28.050288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.3234` n `50` status `ready` deltaP `10.855` edge `30.4595` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2492` n `50` status `ready` deltaP `12.0244` edge `24.4406` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.815` n `50` status `ready` deltaP `26.513` edge `1.0615` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.3627` n `69` status `ready` deltaP `30.1258` edge `0.7112` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.2114` n `50` status `ready` deltaP `34.1664` edge `0.7648` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.1704` n `72` status `ready` deltaP `38.8128` edge `0.6091` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.7766` n `72` status `ready` deltaP `29.8896` edge `0.5832` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4178` n `50` status `ready` deltaP `17.9239` edge `0.569` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2606` n `50` status `ready` deltaP `17.9452` edge `0.531` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2739` n `69` status `ready` deltaP `32.9139` edge `0.1526` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9803` n `72` status `ready` deltaP `29.3189` edge `0.1975` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3394` n `50` status `ready` deltaP `15.3274` edge `0.2424` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.217` n `72` status `ready` deltaP `16.293` edge `0.195` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9929` n `50` status `ready` deltaP `13.6263` edge `0.2036` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.975` n `50` status `ready` deltaP `33.3607` edge `0.039` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.6991` n `72` status `ready` deltaP `29.7945` edge `0.0525` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.3121` n `72` status `ready` deltaP `19.9582` edge `0.1012` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.9124` n `72` status `ready` deltaP `7.6607` edge `0.1602` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.4925` n `72` status `ready` deltaP `14.2439` edge `0.0656` maxDD `-0.8948`
- `market_context_high->fx_1h` score `1.4419` n `50` status `ready` deltaP `20.2601` edge `0.0115` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
