# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T07:37:30.155496+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.2951` n `105` status `ready` deltaP `10.1084` edge `0.0059` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.2945` n `105` status `ready` deltaP `8.4203` edge `0.0499` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.1063` n `105` status `ready` deltaP `4.7402` edge `0.1402` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0478` n `105` status `ready` deltaP `7.333` edge `0.0075` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->commodity_24h` score `-0.2428` n `101` status `ready` deltaP `5.7137` edge `0.125` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.2453` n `105` status `ready` deltaP `6.5302` edge `-0.0174` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3019` n `105` status `ready` deltaP `5.4283` edge `0.0175` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3024` n `105` status `ready` deltaP `2.3396` edge `-0.0021` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4098` n `105` status `ready` deltaP `7.6305` edge `-0.0623` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6622` n `105` status `ready` deltaP `-1.5854` edge `0.0107` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.744` n `105` status `ready` deltaP `-5.7285` edge `-0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8625` n `105` status `ready` deltaP `-2.1927` edge `-0.0158` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.975` n `105` status `ready` deltaP `-1.1577` edge `-0.0328` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.7756` n `105` status `ready` deltaP `0.0131` edge `-0.1044` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.1214` n `105` status `ready` deltaP `2.2619` edge `-0.1731` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3284` n `101` status `ready` deltaP `-15.6989` edge `-0.0144` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8816` n `101` status `ready` deltaP `-1.5367` edge `-0.0458` maxDD `-18.6608`
- `market_context_high->unknown_24h` score `-4.5264` n `101` status `ready` deltaP `11.57` edge `-0.4037` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.5781` n `101` status `ready` deltaP `-18.5317` edge `-0.1326` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
