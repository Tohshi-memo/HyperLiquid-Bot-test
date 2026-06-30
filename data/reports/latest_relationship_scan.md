# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T10:52:30.999573+00:00`
- Price records: `672`
- Market context records: `5241`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5604`

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

- `market_context_high->unknown_24h` score `23.9987` n `131` status `ready` deltaP `31.4952` edge `1.8089` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.7722` n `131` status `ready` deltaP `32.7622` edge `1.2121` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `6.1301` n `131` status `ready` deltaP `20.9314` edge `0.735` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.2751` n `155` status `ready` deltaP `14.4562` edge `0.4198` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1062` n `155` status `ready` deltaP `15.2892` edge `0.4695` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2542` n `155` status `ready` deltaP `17.44` edge `0.1738` maxDD `-5.5109`
- `market_context_high->equity_24h` score `1.6558` n `131` status `ready` deltaP `18.0993` edge `0.5802` maxDD `-40.0306`
- `market_context_high->unknown_1h` score `1.4695` n `157` status `ready` deltaP `8.4166` edge `0.1305` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.592` n `131` status `ready` deltaP `13.4502` edge `0.0492` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4773` n `157` status `ready` deltaP `4.7742` edge `0.1041` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.42` n `157` status `ready` deltaP `6.6822` edge `0.115` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.2869` n `155` status `ready` deltaP `6.9404` edge `0.1415` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.0871` n `131` status `ready` deltaP `18.2146` edge `0.0309` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.1148` n `157` status `ready` deltaP `5.9041` edge `0.0476` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1638` n `157` status `ready` deltaP `3.9876` edge `0.0116` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.186` n `157` status `ready` deltaP `3.9552` edge `0.0085` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2934` n `157` status `ready` deltaP `1.2195` edge `-0.0005` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6839` n `157` status `ready` deltaP `-0.6179` edge `-0.0027` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7837` n `155` status `ready` deltaP `0.1377` edge `0.002` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8375` n `155` status `ready` deltaP `3.7716` edge `0.0168` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
