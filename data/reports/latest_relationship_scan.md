# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T07:37:33.655762+00:00`
- Price records: `672`
- Market context records: `5227`
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

- `market_context_high->unknown_24h` score `21.1573` n `118` status `ready` deltaP `32.5477` edge `1.5651` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.618` n `118` status `ready` deltaP `31.9503` edge `1.288` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.1485` n `118` status `ready` deltaP `25.6709` edge `0.8466` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `3.9479` n `155` status `ready` deltaP `12.9318` edge `0.4027` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9198` n `155` status `ready` deltaP `14.0696` edge `0.4621` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2644` n `155` status `ready` deltaP `16.9827` edge `0.1777` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8609` n `155` status `ready` deltaP `8.389` edge `0.1633` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5485` n `118` status `ready` deltaP `13.3416` edge `0.0463` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4349` n `155` status `ready` deltaP `6.553` edge `0.1171` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4221` n `155` status `ready` deltaP `4.3539` edge `0.1023` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.0074` n `118` status `ready` deltaP `16.6696` edge `0.4527` maxDD `-40.0306`
- `market_context_high->equity_4h` score `-0.0439` n `155` status `ready` deltaP `5.416` edge `0.1241` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.2321` n `155` status `ready` deltaP `3.0635` edge `0.009` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.2391` n `155` status `ready` deltaP `4.9208` edge `0.0438` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2589` n `155` status `ready` deltaP `3.0887` edge `0.0082` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2939` n `155` status `ready` deltaP `1.2102` edge `-0.0005` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.3024` n `118` status `ready` deltaP `15.0188` edge `0.0246` maxDD `-7.413`
- `market_context_high->commodity_1h` score `-0.6187` n `155` status `ready` deltaP `0.4259` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6643` n `155` status `ready` deltaP `2.1194` edge `0.0041` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.9397` n `155` status `ready` deltaP `2.7046` edge `0.0154` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
