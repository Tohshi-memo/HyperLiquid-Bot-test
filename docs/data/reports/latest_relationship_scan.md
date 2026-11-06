# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T11:22:27.291268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4236`

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

- `news_risk_high->crypto_alt_4h` score `-0.4677` n `125` status `ready` deltaP `4.9329` edge `0.1708` maxDD `-14.0916`
- `news_risk_high->index_4h` score `-0.5157` n `125` status `ready` deltaP `6.6098` edge `0.0122` maxDD `-2.457`
- `news_risk_high->index_1h` score `-0.5375` n `125` status `ready` deltaP `4.3437` edge `0.0014` maxDD `-1.0123`
- `news_risk_high->fx_1h` score `-0.708` n `125` status `ready` deltaP `-4.1425` edge `-0.0025` maxDD `-0.5191`
- `news_risk_high->crypto_alt_1h` score `-0.79` n `125` status `ready` deltaP `-0.1054` edge `0.0222` maxDD `-5.8225`
- `news_risk_high->index_24h` score `-0.8953` n `125` status `ready` deltaP `-5.719` edge `0.111` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `-0.9476` n `125` status `ready` deltaP `-4.5549` edge `-0.0059` maxDD `-0.8182`
- `news_risk_high->equity_24h` score `-1.087` n `125` status `ready` deltaP `19.2983` edge `0.9394` maxDD `-86.0244`
- `news_risk_high->fx_24h` score `-1.5656` n `125` status `ready` deltaP `-18.2215` edge `-0.012` maxDD `-0.7131`
- `news_risk_high->metal_1h` score `-1.5712` n `125` status `ready` deltaP `-5.2515` edge `-0.016` maxDD `-2.0608`
- `news_risk_high->equity_1h` score `-1.737` n `125` status `ready` deltaP `-3.0012` edge `0.0095` maxDD `-11.9744`
- `news_risk_high->crypto_major_1h` score `-2.2078` n `125` status `ready` deltaP `-5.4575` edge `-0.0166` maxDD `-6.1465`
- `news_risk_high->crypto_major_4h` score `-2.2295` n `125` status `ready` deltaP `-4.4366` edge `0.0456` maxDD `-10.8117`
- `news_risk_high->commodity_1h` score `-2.9438` n `125` status `ready` deltaP `-15.0994` edge `-0.008` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.4824` n `125` status `ready` deltaP `-8.6683` edge `-0.0564` maxDD `-4.7473`
- `news_risk_high->commodity_4h` score `-4.591` n `125` status `ready` deltaP `-20.5134` edge `-0.0104` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-4.6177` n `125` status `ready` deltaP `7.0671` edge `0.0698` maxDD `-32.4714`
- `news_risk_high->metal_24h` score `-5.7646` n `125` status `ready` deltaP `-8.2311` edge `-0.2359` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.3765` n `125` status `ready` deltaP `-22.6007` edge `0.0251` maxDD `-41.1309`
- `news_risk_high->crypto_major_24h` score `-11.0982` n `125` status `ready` deltaP `-19.0588` edge `0.0712` maxDD `-52.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
