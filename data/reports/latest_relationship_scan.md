# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T00:52:26.670897+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.6879` n `50` status `ready` deltaP `9.8263` edge `28.1634` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.3883` n `50` status `ready` deltaP `8.689` edge `23.8911` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2805` n `83` status `ready` deltaP `37.8682` edge `1.3752` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.853` n `50` status `ready` deltaP `35.6458` edge `0.8084` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2379` n `50` status `ready` deltaP `18.9146` edge `0.5474` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.8763` n `50` status `ready` deltaP `14.2778` edge `0.6488` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.962` n `50` status `ready` deltaP `16.189` edge `0.4349` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.6046` n `50` status `ready` deltaP `18.6944` edge `0.5237` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.4144` n `83` status `ready` deltaP `15.0916` edge `0.4993` maxDD `-15.8971`
- `market_context_high->crypto_major_1h` score `3.0323` n `50` status `ready` deltaP `14.7485` edge `0.1994` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9542` n `50` status `ready` deltaP `13.7545` edge `0.2208` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9336` n `50` status `ready` deltaP `32.9939` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.7513` n `96` status `ready` deltaP `24.4918` edge `0.1356` maxDD `-2.9013`
- `news_risk_high->crypto_alt_4h` score `2.6719` n `96` status `ready` deltaP `10.7723` edge `0.2852` maxDD `-6.4152`
- `news_risk_high->equity_24h` score `2.3775` n `83` status `ready` deltaP `15.7546` edge `0.4228` maxDD `-9.175`
- `news_risk_high->commodity_24h` score `1.7598` n `83` status `ready` deltaP `27.692` edge `0.1534` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.5399` n `83` status `ready` deltaP `16.4428` edge `0.2152` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->index_24h` score `1.4483` n `83` status `ready` deltaP `18.2857` edge `0.0466` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9198` n `50` status `ready` deltaP `14.7917` edge `0.0764` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
