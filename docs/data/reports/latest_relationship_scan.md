# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T05:37:24.073640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.091` n `96` status `ready` deltaP `6.7708` edge `0.2499` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.6343` n `96` status `ready` deltaP `13.5043` edge `0.0763` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.6264` n `96` status `ready` deltaP `9.4766` edge `0.1612` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.2479` n `96` status `ready` deltaP `15.4514` edge `0.2403` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.2182` n `96` status `ready` deltaP `18.0894` edge `0.0385` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.0069` n `96` status `ready` deltaP `11.6107` edge `0.1086` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8863` n `96` status `ready` deltaP `15.3131` edge `0.0105` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2899` n `96` status `ready` deltaP `9.0569` edge `-0.0135` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.263` n `96` status `ready` deltaP `10.3659` edge `0.0798` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1512` n `96` status `ready` deltaP `5.9693` edge `0.0115` maxDD `-0.4291`
- `market_context_high->fx_4h` score `0.0574` n `96` status `ready` deltaP `7.9522` edge `0.0046` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0411` n `96` status `ready` deltaP `7.0376` edge `0.022` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.337` n `96` status `ready` deltaP `-1.4721` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.3567` n `96` status `ready` deltaP `2.9753` edge `0.0146` maxDD `-2.413`
- `market_context_high->unknown_24h` score `-0.3757` n `96` status `ready` deltaP `13.368` edge `-0.0698` maxDD `-1.0505`
- `market_context_high->crypto_major_1h` score `-0.3915` n `96` status `ready` deltaP `2.6821` edge `0.0164` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.5213` n `96` status `ready` deltaP `1.499` edge `0.0082` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8635` n `96` status `ready` deltaP `-7.2917` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2409` n `96` status `ready` deltaP `-3.6458` edge `0.0678` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.2906` n `96` status `ready` deltaP `-25.5208` edge `-0.0291` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
