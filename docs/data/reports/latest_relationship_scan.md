# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T22:07:25.821157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11577`

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

- `risk_on_high->unknown_4h` score `27.5277` n `133` status `ready` deltaP `10.9802` edge `2.2826` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `27.5277` n `133` status `ready` deltaP `10.9802` edge `2.2826` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `20.7626` n `167` status `ready` deltaP `12.5785` edge `1.7159` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `15.2142` n `133` status `ready` deltaP `0.4434` edge `1.3226` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `15.2142` n `133` status `ready` deltaP `0.4434` edge `1.3226` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.7344` n `167` status `ready` deltaP `0.8982` edge `0.9516` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.8217` n `127` status `ready` deltaP `16.4766` edge `0.3932` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3683` n `67` status `ready` deltaP `6.7096` edge `0.0384` maxDD `-0.8733`
- `risk_on_high->equity_24h` score `0.3388` n `107` status `ready` deltaP `11.7228` edge `0.3646` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.3388` n `107` status `ready` deltaP `11.7228` edge `0.3646` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `0.1128` n `67` status `ready` deltaP `16.0525` edge `0.2009` maxDD `-19.4761`
- `risk_on_high->metal_1h` score `0.0875` n `133` status `ready` deltaP `12.1134` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0875` n `133` status `ready` deltaP `12.1134` edge `0.0017` maxDD `-1.699`
- `news_risk_high->equity_24h` score `0.0189` n `67` status `ready` deltaP `4.1485` edge `0.2215` maxDD `-15.4056`
- `news_risk_high->fx_4h` score `-0.0321` n `67` status `ready` deltaP `8.8892` edge `0.0037` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.043` n `67` status `ready` deltaP `4.9245` edge `-0.003` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0812` n `133` status `ready` deltaP `5.3397` edge `-0.0015` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0812` n `133` status `ready` deltaP `5.3397` edge `-0.0015` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.1353` n `107` status `ready` deltaP `25.7075` edge `0.081` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.1353` n `107` status `ready` deltaP `25.7075` edge `0.081` maxDD `-4.2453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
