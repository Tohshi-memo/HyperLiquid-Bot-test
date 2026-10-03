# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T05:52:31.433325+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4858`

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

- `market_context_high->unknown_1h` score `366.217` n `50` status `ready` deltaP `11.024` edge `30.4495` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.5248` n `50` status `ready` deltaP `11.2805` edge `24.3852` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.6467` n `50` status `ready` deltaP `24.0` edge `0.9809` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.7198` n `70` status `ready` deltaP `33.7351` edge `0.7169` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.2231` n `50` status `ready` deltaP `31.6528` edge `0.6992` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `8.8193` n `86` status `ready` deltaP `34.6745` edge `0.5241` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.7467` n `86` status `ready` deltaP `31.2252` edge `0.5718` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2685` n `50` status `ready` deltaP `16.628` edge `0.5652` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8959` n `50` status `ready` deltaP `16.3415` edge `0.5113` maxDD `-7.6465`
- `news_risk_high->crypto_alt_24h` score `4.2061` n `70` status `ready` deltaP `12.8571` edge `0.7349` maxDD `-16.8426`
- `news_risk_high->index_24h` score `3.9336` n `70` status `ready` deltaP `33.0407` edge `0.1234` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.7894` n `86` status `ready` deltaP `30.502` edge `0.1737` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1714` n `50` status `ready` deltaP `14.2036` edge `0.2359` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.921` n `50` status `ready` deltaP `12.8024` edge `0.2031` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8043` n `50` status `ready` deltaP `31.3171` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.6251` n `86` status `ready` deltaP `13.9187` edge `0.1615` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.7801` n `86` status `ready` deltaP `7.5059` edge `0.1502` maxDD `-2.4854`
- `news_risk_high->metal_4h` score `1.6748` n `86` status `ready` deltaP `14.3718` edge `0.0895` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.3681` n `86` status `ready` deltaP `14.1137` edge `0.0561` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
