# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T10:07:28.075493+00:00`
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

- `market_context_high->equity_1h` score `0.4812` n `109` status `ready` deltaP `9.7484` edge `0.0566` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3359` n `109` status `ready` deltaP `10.5697` edge `0.0063` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.089` n `105` status `ready` deltaP `8.0952` edge `0.0077` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0413` n `105` status `ready` deltaP `4.5877` edge `0.1358` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.1139` n `109` status `ready` deltaP `2.4433` edge `0.005` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2585` n `105` status `ready` deltaP `6.5302` edge `-0.0191` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->commodity_24h` score `-0.3959` n `104` status `ready` deltaP `4.8344` edge `0.1181` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.41` n `109` status `ready` deltaP `1.4146` edge `-0.0049` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.531` n `109` status `ready` deltaP `8.1402` edge `-0.0758` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.7203` n `109` status `ready` deltaP `-5.4373` edge `0.0005` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7766` n `105` status `ready` deltaP `-3.1098` edge `0.0062` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.0593` n `109` status `ready` deltaP `-3.487` edge `-0.0324` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.085` n `109` status `ready` deltaP `-1.8788` edge `-0.0421` maxDD `-2.7581`
- `market_context_high->fx_24h` score `-3.2343` n `104` status `ready` deltaP `-14.6768` edge `-0.0117` maxDD `-2.1314`
- `market_context_high->crypto_alt_4h` score `-3.364` n `105` status `ready` deltaP `-1.2064` edge `-0.1453` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.6874` n `105` status `ready` deltaP `0.7375` edge `-0.2101` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0192` n `104` status `ready` deltaP `-3.2184` edge `-0.0436` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.3536` n `104` status `ready` deltaP `10.5502` edge `-0.3825` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4156` n `104` status `ready` deltaP `-17.1607` edge `-0.1209` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
