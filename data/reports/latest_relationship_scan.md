# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T11:07:20.225027+00:00`
- Price records: `672`
- Market context records: `1836`
- Flow alert records: `7185`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9374` n `195` status `ready` deltaP `23.1121` edge `0.5385` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.5113` n `178` status `ready` deltaP `25.6808` edge `0.614` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4168` n `195` status `ready` deltaP `26.4806` edge `0.4828` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3306` n `195` status `ready` deltaP `16.9169` edge `0.4505` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.4551` n `178` status `ready` deltaP `17.6947` edge `0.2928` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.8994` n `195` status `ready` deltaP `16.4048` edge `0.2417` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7291` n `178` status `ready` deltaP `14.56` edge `0.6624` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.7805` n `178` status `ready` deltaP `14.673` edge `0.5404` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8361` n `195` status `ready` deltaP `12.371` edge `0.0961` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3906` n `196` status `ready` deltaP `5.8903` edge `0.0919` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2103` n `196` status `ready` deltaP `5.7742` edge `0.0904` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.1788` n `178` status `ready` deltaP `19.0329` edge `0.7466` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0593` n `178` status `ready` deltaP `12.1294` edge `0.0191` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.155` n `196` status `ready` deltaP `3.8342` edge `0.0409` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5283` n `196` status `ready` deltaP `3.0399` edge `0.0309` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.578` n `195` status `ready` deltaP `12.9933` edge `0.1344` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.6299` n `196` status `ready` deltaP `5.0745` edge `0.019` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6777` n `196` status `ready` deltaP `-0.6752` edge `0.0112` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7402` n `196` status `ready` deltaP `-4.5857` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0502` n `195` status `ready` deltaP `-5.6887` edge `-0.0079` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
