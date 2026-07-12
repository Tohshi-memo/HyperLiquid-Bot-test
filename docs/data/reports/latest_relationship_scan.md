# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T20:52:23.172104+00:00`
- Price records: `672`
- Market context records: `6538`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.7167` n `31` status `ready` deltaP `37.3959` edge `0.9085` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6355` n `31` status `ready` deltaP `54.9393` edge `0.1867` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3535` n `144` status `ready` deltaP `11.8934` edge `0.7802` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8469` n `31` status `ready` deltaP `21.1885` edge `0.5581` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7282` n `37` status `ready` deltaP `39.3416` edge `0.053` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.2732` n `31` status `ready` deltaP `24.1852` edge `0.0426` maxDD `-0.1518`
- `market_context_high->unknown_1h` score `1.962` n `196` status `ready` deltaP `-6.599` edge `0.2976` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.9575` n `37` status `ready` deltaP `24.4619` edge `0.0181` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.4475` n `144` status `ready` deltaP `13.4773` edge `0.2176` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.7074` n `37` status `ready` deltaP `7.214` edge `0.0963` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.6551` n `185` status `ready` deltaP `14.0895` edge `0.0283` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.338` n `185` status `ready` deltaP `9.8756` edge `0.1177` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0317` n `37` status `ready` deltaP `0.9023` edge `0.049` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2573` n `31` status `ready` deltaP `7.525` edge `0.004` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3071` n `185` status `ready` deltaP `10.4573` edge `0.0608` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.3855` n `185` status `ready` deltaP `12.7999` edge `0.0943` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4297` n `196` status `ready` deltaP `-0.4002` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4435` n `196` status `ready` deltaP `1.8972` edge `-0.0012` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5481` n `196` status `ready` deltaP `6.1836` edge `0.0198` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5658` n `196` status `ready` deltaP `5.9178` edge `0.0146` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
