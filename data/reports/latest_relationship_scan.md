# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T21:07:22.895433+00:00`
- Price records: `672`
- Market context records: `3216`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11250`

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

- `market_context_high->commodity_24h` score `13.6899` n `102` status `ready` deltaP `47.9473` edge `0.864` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0864` n `102` status `ready` deltaP `15.0225` edge `2.447` maxDD `-71.142`
- `market_context_high->index_24h` score `9.3542` n `102` status `ready` deltaP `29.3198` edge `0.8395` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.429` n `102` status `ready` deltaP `14.2872` edge `1.4424` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.446` n `128` status `ready` deltaP `22.8849` edge `0.1804` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.3384` n `140` status `ready` deltaP `5.9795` edge `0.0306` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.5817` n `102` status `ready` deltaP `4.7079` edge `-0.0097` maxDD `-1.2796`
- `market_context_high->unknown_4h` score `-0.6403` n `128` status `ready` deltaP `8.2317` edge `0.0896` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.9437` n `140` status `ready` deltaP `2.8101` edge `0.0089` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-1.0155` n `140` status `ready` deltaP `4.5594` edge `0.0657` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0408` n `128` status `ready` deltaP `-5.9641` edge `-0.0052` maxDD `-1.4115`
- `market_context_high->crypto_alt_1h` score `-1.3848` n `140` status `ready` deltaP `4.3884` edge `0.0808` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.6895` n `140` status `ready` deltaP `-10.0813` edge `-0.0049` maxDD `-0.8278`
- `market_context_high->equity_1h` score `-1.7216` n `140` status `ready` deltaP `2.0616` edge `-0.0003` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.888` n `128` status `ready` deltaP `12.1761` edge `0.0524` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.275` n `140` status `ready` deltaP `-4.5509` edge `-0.0112` maxDD `-8.177`
- `market_context_high->unknown_1h` score `-2.7771` n `140` status `ready` deltaP `1.5227` edge `-0.1183` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-3.3231` n `102` status `ready` deltaP `14.1953` edge `1.7644` maxDD `-165.4723`
- `market_context_high->crypto_major_4h` score `-4.934` n `128` status `ready` deltaP `3.5251` edge `0.1363` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-5.2359` n `128` status `ready` deltaP `10.8804` edge `0.0217` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
