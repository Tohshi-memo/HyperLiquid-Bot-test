# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T23:07:29.045279+00:00`
- Price records: `672`
- Market context records: `7078`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7539` n `174` status `ready` deltaP `17.944` edge `0.0132` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0333` n `174` status `ready` deltaP `1.0479` edge `0.0461` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.0437` n `174` status `ready` deltaP `5.7712` edge `0.003` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3907` n `174` status `ready` deltaP `0.9516` edge `0.03` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4965` n `174` status `ready` deltaP `0.3906` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6085` n `174` status `ready` deltaP `3.4242` edge `0.0344` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8891` n `174` status `ready` deltaP `-4.8678` edge `-0.0199` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3584` n `174` status `ready` deltaP `-4.9075` edge `-0.0037` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.499` n `174` status `ready` deltaP `-6.6408` edge `0.0828` maxDD `-4.742`
- `market_context_high->commodity_4h` score `-1.5877` n `174` status `ready` deltaP `-7.9969` edge `-0.0467` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8945` n `174` status `ready` deltaP `4.5151` edge `-0.0307` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1863` n `174` status `ready` deltaP `3.6462` edge `-0.0347` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4878` n `174` status `ready` deltaP `-3.0052` edge `-0.0564` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0199` n `174` status `ready` deltaP `-0.3645` edge `-0.0062` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0807` n `174` status `ready` deltaP `2.6387` edge `0.0159` maxDD `-24.6094`
- `market_context_high->metal_4h` score `-3.7327` n `174` status `ready` deltaP `-1.1301` edge `-0.0052` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.7744` n `174` status `ready` deltaP `-2.658` edge `-0.0141` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-4.8955` n `174` status `ready` deltaP `-18.4268` edge `0.0099` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9738` n `174` status `ready` deltaP `4.1035` edge `-0.1626` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.5191` n `174` status `ready` deltaP `-22.6173` edge `-0.1106` maxDD `-44.2166`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
