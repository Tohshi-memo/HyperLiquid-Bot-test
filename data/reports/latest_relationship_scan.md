# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T08:37:30.260875+00:00`
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

- `market_context_high->index_1h` score `0.3215` n `105` status `ready` deltaP `10.4078` edge `0.0061` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3197` n `105` status `ready` deltaP `8.57` edge `0.051` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.1051` n `105` status `ready` deltaP `4.7402` edge `0.1401` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0637` n `105` status `ready` deltaP `7.6379` edge `0.0075` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2499` n `105` status `ready` deltaP `6.5302` edge `-0.018` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.2918` n `103` status `ready` deltaP `5.596` edge `0.1217` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3216` n `105` status `ready` deltaP `2.1899` edge `-0.0027` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4565` n `105` status `ready` deltaP `7.1814` edge `-0.0632` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.7088` n `105` status `ready` deltaP `-2.1951` edge `0.0088` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7635` n `105` status `ready` deltaP `-6.0279` edge `-0.0011` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.9257` n `105` status `ready` deltaP `-2.3424` edge `-0.0229` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.0217` n `105` status `ready` deltaP `-1.3074` edge `-0.0378` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-3.009` n `105` status `ready` deltaP `-0.4442` edge `-0.1208` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.3136` n `103` status `ready` deltaP `-15.4851` edge `-0.0138` maxDD `-2.0613`
- `market_context_high->crypto_major_4h` score `-3.3166` n `105` status `ready` deltaP `1.6521` edge `-0.1853` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.9931` n `103` status `ready` deltaP `-2.6716` edge `-0.0439` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.2052` n `103` status `ready` deltaP `11.4145` edge `-0.3759` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4428` n `103` status `ready` deltaP `-17.6088` edge `-0.1214` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
