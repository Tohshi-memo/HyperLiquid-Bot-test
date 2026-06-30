# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T06:07:30.580230+00:00`
- Price records: `672`
- Market context records: `5221`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5600`

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

- `market_context_high->unknown_24h` score `20.3235` n `114` status `ready` deltaP `32.7759` edge `1.4941` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.9805` n `114` status `ready` deltaP `31.981` edge `1.318` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.7534` n `114` status `ready` deltaP `27.787` edge `0.8829` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0455` n `155` status `ready` deltaP `13.2367` edge `0.4088` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0242` n `155` status `ready` deltaP `14.0696` edge `0.4708` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.2159` n `155` status `ready` deltaP `17.8973` edge `0.2509` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8777` n `155` status `ready` deltaP `8.6884` edge `0.1627` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5724` n `114` status `ready` deltaP `13.6696` edge `0.0461` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4745` n `155` status `ready` deltaP `6.4033` edge `0.1214` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4605` n `155` status `ready` deltaP `4.3539` edge `0.1055` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.0495` n `155` status `ready` deltaP `6.1782` edge `0.1268` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1714` n `155` status `ready` deltaP `3.5126` edge `0.0138` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.2414` n `155` status `ready` deltaP `4.7711` edge `0.0446` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2417` n `155` status `ready` deltaP `2.1084` edge `0.0002` maxDD `-0.6194`
- `market_context_high->index_1h` score `-0.2841` n `155` status `ready` deltaP `2.7893` edge `0.0081` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.39` n `114` status `ready` deltaP `13.8889` edge `0.0209` maxDD `-7.413`
- `market_context_high->equity_24h` score `-0.4908` n `114` status `ready` deltaP `16.1641` edge `0.3922` maxDD `-40.0306`
- `market_context_high->fx_4h` score `-0.6081` n `155` status `ready` deltaP `3.034` edge `0.0052` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6187` n `155` status `ready` deltaP `0.4259` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.8801` n `155` status `ready` deltaP `3.3143` edge `0.0163` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
