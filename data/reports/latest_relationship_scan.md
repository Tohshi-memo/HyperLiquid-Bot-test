# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T16:07:52.234365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11627`

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

- `market_context_high->crypto_major_24h` score `2.4587` n `91` status `ready` deltaP `9.6121` edge `0.2616` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7326` n `91` status `ready` deltaP `19.3727` edge `0.2763` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1956` n `96` status `ready` deltaP `10.0612` edge `0.0627` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7271` n `96` status `ready` deltaP `14.126` edge `0.024` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6839` n `96` status `ready` deltaP `13.0676` edge `0.0086` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4891` n `96` status `ready` deltaP `9.3563` edge `0.0011` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.389` n `96` status `ready` deltaP `7.9522` edge `0.0815` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.2782` n `96` status `ready` deltaP `3.379` edge `0.0895` maxDD `-2.4411`
- `market_context_high->metal_1h` score `0.0086` n `96` status `ready` deltaP `4.4723` edge `0.0096` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0456` n `96` status `ready` deltaP `8.3841` edge `0.0673` maxDD `-5.4926`
- `market_context_high->fx_4h` score `-0.2091` n `96` status `ready` deltaP `3.5315` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.294` n `91` status `ready` deltaP `11.6518` edge `-0.0808` maxDD `-0.3771`
- `market_context_high->commodity_4h` score `-0.3719` n `96` status `ready` deltaP `3.938` edge `0.0111` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4717` n `96` status `ready` deltaP `-3.8673` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.5101` n `96` status `ready` deltaP `1.0292` edge `0.0079` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6019` n `96` status `ready` deltaP `0.1372` edge `0.0064` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6275` n `96` status `ready` deltaP `0.3303` edge `0.011` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8666` n `96` status `ready` deltaP `-7.2917` edge `-0.0059` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.425` n `91` status `ready` deltaP `-7.9113` edge `0.0189` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.5452` n `91` status `ready` deltaP `-29.897` edge `-0.0295` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
