# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T05:22:27.825243+00:00`
- Price records: `672`
- Market context records: `5218`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `19.5358` n `112` status `ready` deltaP `33.2342` edge `1.4254` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.1188` n `112` status `ready` deltaP `31.9693` edge `1.3296` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.9484` n `112` status `ready` deltaP `27.5546` edge `0.9007` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.1669` n `155` status `ready` deltaP `13.3891` edge `0.4179` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1238` n `155` status `ready` deltaP `14.0696` edge `0.4791` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.7757` n `155` status `ready` deltaP `18.3546` edge `0.2945` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8669` n `155` status `ready` deltaP `8.6884` edge `0.1618` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5876` n `112` status `ready` deltaP `13.8145` edge `0.0464` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.53` n `155` status `ready` deltaP `4.5036` edge `0.1103` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5105` n `155` status `ready` deltaP `6.4033` edge `0.1244` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1147` n `155` status `ready` deltaP `6.483` edge `0.1302` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1714` n `155` status `ready` deltaP `3.5126` edge `0.0138` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2433` n `155` status `ready` deltaP `2.1084` edge `0.0` maxDD `-0.6194`
- `market_context_high->equity_1h` score `-0.2534` n `155` status `ready` deltaP `4.6214` edge `0.0446` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2793` n `155` status `ready` deltaP `2.7893` edge `0.0085` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.4118` n `112` status `ready` deltaP `13.8145` edge `0.0186` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6081` n `155` status `ready` deltaP `3.034` edge `0.0052` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6172` n `155` status `ready` deltaP `0.4259` edge `-0.0011` maxDD `-2.4692`
- `market_context_high->equity_24h` score `-0.7878` n `112` status `ready` deltaP `15.8978` edge `0.3559` maxDD `-40.0306`
- `market_context_high->index_4h` score `-0.8291` n `155` status `ready` deltaP `3.7716` edge `0.0175` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
