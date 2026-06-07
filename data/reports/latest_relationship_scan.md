# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T14:52:27.405868+00:00`
- Price records: `672`
- Market context records: `3188`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.7725` n `106` status `ready` deltaP `47.5104` edge `0.8738` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.7417` n `106` status `ready` deltaP `15.1434` edge `2.402` maxDD `-71.142`
- `market_context_high->unknown_24h` score `10.8047` n `106` status `ready` deltaP `19.2675` edge `0.8978` maxDD `-8.0685`
- `market_context_high->index_24h` score `6.2976` n `106` status `ready` deltaP `30.5293` edge `0.8593` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6671` n `106` status `ready` deltaP `13.1944` edge `1.352` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.2074` n `139` status `ready` deltaP `20.8326` edge `0.1742` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6327` n `106` status `ready` deltaP `11.0981` edge `0.0015` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5592` n `139` status `ready` deltaP `11.9429` edge `0.1892` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3876` n `140` status `ready` deltaP `6.4286` edge `0.0317` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3408` n `140` status `ready` deltaP `6.4628` edge `0.0195` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5336` n `140` status `ready` deltaP `5.633` edge `0.107` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.6756` n `139` status `ready` deltaP `17.9976` edge `0.0843` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0953` n `140` status `ready` deltaP `3.1309` edge `0.065` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2957` n `140` status `ready` deltaP `4.1702` edge `0.0128` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3012` n `139` status `ready` deltaP `-10.7606` edge `-0.0066` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6359` n `140` status `ready` deltaP `-9.367` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1265` n `140` status `ready` deltaP `-4.4012` edge `-0.0085` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3614` n `139` status `ready` deltaP `16.7003` edge `0.3904` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1279` n `140` status `ready` deltaP `2.5022` edge `-0.0747` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7576` n `139` status `ready` deltaP `9.3481` edge `0.2483` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
