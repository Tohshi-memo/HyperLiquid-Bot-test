# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T17:22:33.427594+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.5908` n `91` status `ready` deltaP `9.9587` edge `0.2703` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7006` n `91` status `ready` deltaP `19.3727` edge `0.2722` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1489` n `96` status `ready` deltaP `9.6121` edge `0.0618` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7535` n `96` status `ready` deltaP `14.126` edge `0.0262` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6312` n `96` status `ready` deltaP `12.4688` edge `0.0082` maxDD `-0.0982`
- `market_context_high->equity_4h` score `0.4999` n `96` status `ready` deltaP `4.1412` edge `0.1029` maxDD `-2.4411`
- `market_context_high->crypto_major_4h` score `0.4346` n `96` status `ready` deltaP `7.9522` edge `0.0853` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4135` n `96` status `ready` deltaP `8.9072` edge `-0.0022` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `-0.024` n `96` status `ready` deltaP `8.3841` edge `0.0691` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0309` n `96` status `ready` deltaP `4.0232` edge `0.0093` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.2007` n `91` status `ready` deltaP `12.5183` edge `-0.0788` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.2179` n `96` status `ready` deltaP `3.379` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.3742` n `96` status `ready` deltaP `3.938` edge `0.0108` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4639` n `96` status `ready` deltaP `-3.7176` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4922` n `96` status `ready` deltaP `1.1789` edge `0.0092` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5606` n `96` status `ready` deltaP `0.5863` edge `0.0087` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5863` n `96` status `ready` deltaP `0.6351` edge `0.0124` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8471` n `96` status `ready` deltaP `-6.9923` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.3183` n `91` status `ready` deltaP `-7.0447` edge `0.0268` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.4674` n `91` status `ready` deltaP `-29.0304` edge `-0.0288` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
