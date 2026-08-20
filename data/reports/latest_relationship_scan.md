# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T17:51:30.037168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11818`

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

- `market_context_high->equity_4h` score `0.6732` n `105` status `ready` deltaP `7.9414` edge `0.1661` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5295` n `105` status `ready` deltaP `9.7676` edge `0.0605` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.355` n `105` status `ready` deltaP `10.7072` edge `0.0069` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.0214` n `105` status `ready` deltaP `10.1887` edge `-0.0076` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0123` n `105` status `ready` deltaP `6.8757` edge `0.006` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.0801` n `96` status `ready` deltaP `4.6875` edge `0.1418` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1682` n `105` status `ready` deltaP `3.5372` edge `0.0011` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2185` n `105` status `ready` deltaP `0.6259` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2467` n `105` status `ready` deltaP `6.1905` edge `0.0195` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.5033` n `105` status `ready` deltaP `6.882` edge `-0.0651` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5633` n `105` status `ready` deltaP `0.951` edge `0.0016` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7158` n `105` status `ready` deltaP `-2.1951` edge `0.0079` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7708` n `105` status `ready` deltaP `1.2375` edge `-0.0226` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8039` n `105` status `ready` deltaP `-6.7764` edge `-0.0013` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5414` n `105` status `ready` deltaP `4.2814` edge `-0.03` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.8939` n `105` status `ready` deltaP `6.8351` edge `-0.1013` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.1304` n `96` status `ready` deltaP `17.5347` edge `-0.2438` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5999` n `96` status `ready` deltaP `1.0416` edge `-0.0517` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8042` n `96` status `ready` deltaP `-21.1805` edge `-0.0175` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9611` n `96` status `ready` deltaP `-21.0069` edge `-0.1652` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
