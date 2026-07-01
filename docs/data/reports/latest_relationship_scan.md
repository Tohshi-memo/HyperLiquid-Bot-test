# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T20:07:33.643444+00:00`
- Price records: `672`
- Market context records: `5383`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `6.7129` n `186` status `ready` deltaP `16.8795` edge `0.4599` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.473` n `186` status `ready` deltaP `22.9671` edge `0.757` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.4382` n `205` status `ready` deltaP `14.6341` edge `0.4182` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9289` n `205` status `ready` deltaP `11.7683` edge `0.3297` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1861` n `205` status `ready` deltaP `10.6708` edge `0.2749` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.9654` n `186` status `ready` deltaP `11.4248` edge `0.6505` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.3374` n `205` status `ready` deltaP `7.0111` edge `0.0779` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `0.03` n `205` status `ready` deltaP `2.2287` edge `0.0838` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.0298` n `205` status `ready` deltaP `4.3245` edge `0.0982` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0007` n `205` status `ready` deltaP `5.1271` edge `0.0151` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1672` n `186` status `ready` deltaP `6.8101` edge `0.0302` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `-0.3231` n `205` status `ready` deltaP `8.5975` edge `0.0342` maxDD `-6.1421`
- `market_context_high->index_24h` score `-0.3662` n `186` status `ready` deltaP `15.6026` edge `0.0875` maxDD `-9.0959`
- `market_context_high->fx_1h` score `-0.4485` n `205` status `ready` deltaP `-1.1034` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5047` n `205` status `ready` deltaP `1.7796` edge `0.0136` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.0745` n `205` status `ready` deltaP `5.4878` edge `0.0348` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2059` n `205` status `ready` deltaP `0.2439` edge `0.0008` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5202` n `205` status `ready` deltaP `-3.7695` edge `-0.0071` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4644` n `205` status `ready` deltaP `-5.6098` edge `-0.0261` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1542` n `186` status `ready` deltaP `13.7433` edge `0.3737` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
