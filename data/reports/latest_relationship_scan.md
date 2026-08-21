# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T11:22:23.042292+00:00`
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

- `market_context_high->equity_1h` score `0.4883` n `114` status `ready` deltaP `9.8225` edge `0.0567` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4141` n `114` status `ready` deltaP `11.5322` edge `0.0064` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.1325` n `105` status `ready` deltaP `8.8574` edge `0.0082` maxDD `-0.3539`
- `market_context_high->equity_4h` score `-0.0396` n `105` status `ready` deltaP `4.1304` edge `0.1321` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.0413` n `114` status `ready` deltaP `3.8082` edge `0.0052` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2554` n `105` status `ready` deltaP `6.5302` edge `-0.0187` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3114` n `105` status `ready` deltaP `5.2759` edge `0.0173` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3983` n `114` status `ready` deltaP `9.5888` edge `-0.0744` maxDD `-0.4843`
- `market_context_high->commodity_24h` score `-0.4607` n `105` status `ready` deltaP `4.4147` edge `0.1155` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.4662` n `114` status `ready` deltaP `0.8352` edge `-0.0048` maxDD `-0.503`
- `market_context_high->commodity_1h` score `-0.6575` n `114` status `ready` deltaP `-4.47` edge `0.0021` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7931` n `105` status `ready` deltaP `-3.2622` edge `0.0051` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.1502` n `114` status `ready` deltaP `-2.7576` edge `-0.0446` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-1.2211` n `114` status `ready` deltaP `-1.9645` edge `-0.0085` maxDD `-2.413`
- `market_context_high->fx_24h` score `-3.1796` n `105` status `ready` deltaP `-14.0377` edge `-0.0104` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.6406` n `105` status `ready` deltaP `-1.6637` edge `-0.1653` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.9559` n `105` status `ready` deltaP `-0.0247` edge `-0.2274` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0631` n `105` status `ready` deltaP `-4.0328` edge `-0.0438` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.3771` n `105` status `ready` deltaP `-16.7212` edge `-0.1189` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.4199` n `105` status `ready` deltaP `9.8562` edge `-0.3834` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
