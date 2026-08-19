# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T11:11:48.265638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->crypto_major_24h` score `2.0543` n `96` status `ready` deltaP `6.5972` edge `0.248` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7893` n `96` status `ready` deltaP `10.2388` edge `0.1697` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6893` n `96` status `ready` deltaP `14.2528` edge `0.0759` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3236` n `96` status `ready` deltaP `18.8516` edge `0.0422` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.0231` n `96` status `ready` deltaP `11.1534` edge `0.113` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.9162` n `96` status `ready` deltaP `15.7622` edge `0.01` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.8875` n `96` status `ready` deltaP `11.8056` edge `0.2184` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.2156` n `96` status `ready` deltaP `8.3084` edge `-0.0147` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1847` n `96` status `ready` deltaP `6.2687` edge `0.0123` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `0.1454` n `96` status `ready` deltaP `9.4512` edge `0.0761` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1283` n `96` status `ready` deltaP `17.0139` edge `-0.0521` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.1135` n `96` status `ready` deltaP `8.8668` edge `0.0057` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0875` n `96` status `ready` deltaP `7.6473` edge `0.0218` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.3183` n `96` status `ready` deltaP `-1.1727` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3409` n `96` status `ready` deltaP `3.4306` edge `0.0179` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4416` n `96` status `ready` deltaP `1.7777` edge `0.0117` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5576` n `96` status `ready` deltaP `1.0417` edge `0.0066` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9024` n `96` status `ready` deltaP `-7.8905` edge `-0.0065` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2113` n `96` status `ready` deltaP `-3.6458` edge `0.0716` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.0085` n `96` status `ready` deltaP `-23.0902` edge `-0.0218` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
