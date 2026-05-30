# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T01:22:19.361764+00:00`
- Price records: `672`
- Market context records: `2300`
- Flow alert records: `8512`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9289`

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

- `news_risk_high->crypto_alt_24h` score `20.6149` n `43` status `ready` deltaP `50.0363` edge `1.4432` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6597` n `43` status `ready` deltaP `40.73` edge `1.0774` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5787` n `43` status `ready` deltaP `29.7925` edge `0.9644` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3574` n `43` status `ready` deltaP `19.7674` edge `0.7894` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.5455` n `159` status `ready` deltaP `24.6136` edge `0.7326` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.5329` n `159` status `ready` deltaP `29.436` edge `0.6125` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.2992` n `115` status `ready` deltaP `23.9432` edge `0.4898` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.8627` n `43` status `ready` deltaP `27.9877` edge `0.4079` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6046` n `159` status `ready` deltaP `22.3079` edge `0.3793` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0107` n `115` status `ready` deltaP `13.4783` edge `0.9418` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8969` n `43` status `ready` deltaP `32.6148` edge `0.3493` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.731` n `43` status `ready` deltaP `11.5351` edge `0.2759` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4287` n `43` status `ready` deltaP `36.0142` edge `0.0641` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3413` n `115` status `ready` deltaP `13.3349` edge `0.2413` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.1842` n `43` status `ready` deltaP `4.4614` edge `0.3173` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2431` n `159` status `ready` deltaP `21.8716` edge `0.1237` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2318` n `43` status `ready` deltaP `28.3465` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.0198` n `159` status `ready` deltaP `12.9232` edge `0.2009` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7992` n `159` status `ready` deltaP `13.2226` edge `0.1812` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.7701` n `159` status `ready` deltaP `16.403` edge `0.1786` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
