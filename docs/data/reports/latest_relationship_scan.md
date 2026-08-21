# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T10:22:26.927406+00:00`
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

- `market_context_high->equity_1h` score `0.5221` n `110` status `ready` deltaP `10.0653` edge `0.0579` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3639` n `110` status `ready` deltaP `10.92` edge `0.0063` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.0977` n `105` status `ready` deltaP `8.2476` edge `0.0078` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0305` n `105` status `ready` deltaP `4.5877` edge `0.1349` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.0905` n `110` status `ready` deltaP `2.877` edge `0.0051` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2585` n `105` status `ready` deltaP `6.5302` edge `-0.0191` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3019` n `105` status `ready` deltaP `5.4283` edge `0.0175` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3039` n `110` status `ready` deltaP `0.9309` edge `-0.0062` maxDD `-0.4509`
- `market_context_high->commodity_24h` score `-0.4035` n `105` status `ready` deltaP `4.9355` edge `0.1168` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5298` n `110` status `ready` deltaP `8.4404` edge `-0.0777` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6955` n `110` status `ready` deltaP `-5.1116` edge `0.0015` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7892` n `105` status `ready` deltaP `-3.2622` edge `0.0056` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.0231` n `110` status `ready` deltaP `-1.6031` edge `-0.036` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-1.4674` n `110` status `ready` deltaP `-3.0784` edge `-0.0216` maxDD `-2.413`
- `market_context_high->fx_24h` score `-3.2532` n `105` status `ready` deltaP `-14.7322` edge `-0.0119` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.4072` n `105` status `ready` deltaP `-1.2064` edge `-0.1489` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.7415` n `105` status `ready` deltaP `0.5851` edge `-0.2136` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0365` n `105` status `ready` deltaP `-3.6855` edge `-0.0427` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.1483` n `105` status `ready` deltaP `10.5506` edge `-0.3654` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.3436` n `105` status `ready` deltaP `-16.7212` edge `-0.1146` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
