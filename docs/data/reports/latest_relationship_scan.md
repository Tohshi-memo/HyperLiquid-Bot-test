# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T01:37:23.538446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `56.6631` n `50` status `ready` deltaP `18.5442` edge `4.5983` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6475` n `50` status `ready` deltaP `46.6066` edge `2.6207` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.4902` n `50` status `ready` deltaP `26.9809` edge `0.6603` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.8001` n `71` status `ready` deltaP `17.7387` edge `0.6461` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.8791` n `50` status `ready` deltaP `30.1005` edge `0.4654` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.9718` n `120` status `ready` deltaP `11.8775` edge `0.4917` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4862` n `50` status `ready` deltaP `43.4073` edge `0.0887` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3034` n `120` status `ready` deltaP `28.7406` edge `0.1856` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.9442` n `76` status `ready` deltaP `7.1619` edge `0.2333` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4538` n `50` status `ready` deltaP `26.9948` edge `0.0396` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2427` n `120` status `ready` deltaP `17.3984` edge `0.1116` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2223` n `71` status `ready` deltaP `32.6112` edge `0.0227` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9671` n `120` status `ready` deltaP `9.0918` edge `0.065` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5295` n `76` status `ready` deltaP `11.6057` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4198` n `76` status `ready` deltaP `12.1415` edge `0.0049` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.019` n `120` status `ready` deltaP `11.4735` edge `0.0128` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3639` n `120` status `ready` deltaP `4.0619` edge `-0.0005` maxDD `-0.8587`
- `market_context_high->crypto_major_4h` score `-0.4563` n `120` status `ready` deltaP `13.9431` edge `0.2141` maxDD `-20.9394`
- `market_context_high->crypto_alt_4h` score `-0.4717` n `120` status `ready` deltaP `15.7723` edge `0.319` maxDD `-31.4361`
- `news_risk_high->index_1h` score `-0.4764` n `76` status `ready` deltaP `-1.2291` edge `-0.0092` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
