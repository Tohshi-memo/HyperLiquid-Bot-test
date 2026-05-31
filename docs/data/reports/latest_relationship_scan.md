# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T21:07:24.144581+00:00`
- Price records: `672`
- Market context records: `2495`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.4787` n `124` status `ready` deltaP `19.8869` edge `0.3568` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0789` n `144` status `ready` deltaP `20.9857` edge `0.4679` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5333` n `144` status `ready` deltaP `16.8361` edge `0.3632` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1312` n `124` status `ready` deltaP `12.4328` edge `0.5796` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.3416` n `144` status `ready` deltaP `9.5359` edge `0.1532` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4586` n `153` status `ready` deltaP `6.4283` edge `0.1141` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.376` n `153` status `ready` deltaP `6.7277` edge `0.1059` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.2946` n `124` status `ready` deltaP `2.4921` edge `0.7169` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.1072` n `124` status `ready` deltaP `4.3514` edge `0.078` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1425` n `124` status `ready` deltaP `18.4084` edge `0.0181` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1861` n `144` status `ready` deltaP `6.3516` edge `0.0263` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3404` n `153` status `ready` deltaP `0.8307` edge `0.0043` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5093` n `153` status `ready` deltaP `3.3502` edge `0.0002` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5622` n `153` status `ready` deltaP `-0.3375` edge `0.0048` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6071` n `144` status `ready` deltaP `-0.0846` edge `0.0087` maxDD `-0.8774`
- `market_context_high->unknown_1h` score `-0.6268` n `153` status `ready` deltaP `1.5939` edge `0.0091` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.8036` n `153` status `ready` deltaP `0.4618` edge `0.0059` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.877` n `153` status `ready` deltaP `-0.1839` edge `0.012` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9034` n `124` status `ready` deltaP `2.8506` edge `0.0037` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.123` n `144` status `ready` deltaP `1.3889` edge `0.0359` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
