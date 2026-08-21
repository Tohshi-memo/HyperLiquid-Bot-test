# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T05:52:31.106031+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->index_1h` score `0.3215` n `105` status `ready` deltaP `10.4078` edge `0.0061` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3125` n `105` status `ready` deltaP `8.4203` edge `0.0514` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.0755` n `105` status `ready` deltaP `7.7903` edge `0.008` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0301` n `105` status `ready` deltaP `4.2828` edge `0.1369` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1683` n `96` status `ready` deltaP `4.6875` edge `0.1305` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2154` n `105` status `ready` deltaP `0.6259` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2468` n `105` status `ready` deltaP `6.5302` edge `-0.0176` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.288` n `105` status `ready` deltaP `2.4893` edge `-0.0019` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3051` n `105` status `ready` deltaP `5.4283` edge `0.0171` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4158` n `105` status `ready` deltaP `7.6305` edge `-0.0628` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6583` n `105` status `ready` deltaP `-1.5854` edge `0.0112` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7471` n `105` status `ready` deltaP `-5.7285` edge `-0.001` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7495` n `105` status `ready` deltaP `-1.1448` edge `-0.0083` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8939` n `105` status `ready` deltaP `-0.4092` edge `-0.0274` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.4611` n `105` status `ready` deltaP `1.0802` edge `-0.0853` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.8608` n `105` status `ready` deltaP `3.329` edge `-0.1585` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.553` n `96` status `ready` deltaP `-18.0555` edge `-0.0174` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.585` n `96` status `ready` deltaP `1.0416` edge `-0.0498` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.9619` n `96` status `ready` deltaP `-21.0069` edge `-0.1653` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.4675` n `96` status `ready` deltaP `11.8055` edge `-0.4837` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
