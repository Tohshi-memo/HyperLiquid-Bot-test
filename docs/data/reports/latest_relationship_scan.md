# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T00:52:16.220407+00:00`
- Price records: `599`
- Market context records: `702`
- Flow alert records: `1984`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.6833` n `146` status `ready` deltaP `25.9756` edge `0.7505` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5805` n `146` status `ready` deltaP `8.2614` edge `0.4981` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2057` n `149` status `ready` deltaP `7.2863` edge `0.0122` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2736` n `149` status `ready` deltaP `3.065` edge `0.0023` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5147` n `149` status `ready` deltaP `2.1236` edge `0.0404` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.613` n `149` status `ready` deltaP `0.5042` edge `0.0034` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-1.1641` n `149` status `ready` deltaP `15.9243` edge `0.1152` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.17` n `149` status `ready` deltaP `-1.6898` edge `-0.0052` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1792` n `149` status `ready` deltaP `-4.1149` edge `-0.0105` maxDD `-2.1602`
- `market_context_high->index_24h` score `-1.1928` n `146` status `ready` deltaP `-3.4329` edge `0.123` maxDD `-5.9609`
- `market_context_high->crypto_alt_1h` score `-1.4201` n `149` status `ready` deltaP `4.2637` edge `-0.0153` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6556` n `149` status `ready` deltaP `2.4458` edge `-0.002` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6589` n `149` status `ready` deltaP `5.7843` edge `-0.0045` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.973` n `149` status `ready` deltaP `4.074` edge `0.0654` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.3328` n `146` status `ready` deltaP `-5.419` edge `0.1022` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5503` n `149` status `ready` deltaP `-0.663` edge `0.0071` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.33` n `149` status `ready` deltaP `-4.9608` edge `-0.0485` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8898` n `149` status `ready` deltaP `-6.7438` edge `0.0709` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.3189` n `149` status `ready` deltaP `2.8964` edge `-0.1914` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0056` n `146` status `ready` deltaP `-11.5135` edge `-0.0478` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
