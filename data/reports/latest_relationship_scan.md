# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T01:07:17.692007+00:00`
- Price records: `672`
- Market context records: `1581`
- Flow alert records: `6464`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.4845` n `182` status `ready` deltaP `27.9838` edge `1.0372` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7954` n `182` status `ready` deltaP `26.9974` edge `1.0046` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.1973` n `182` status `ready` deltaP `26.7399` edge `0.7847` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.2539` n `182` status `ready` deltaP `18.5821` edge `0.4633` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.0983` n `182` status `ready` deltaP `21.4744` edge `0.307` maxDD `-5.3574`
- `market_context_high->equity_4h` score `0.9474` n `199` status `ready` deltaP `8.4447` edge `0.1321` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2481` n `199` status `ready` deltaP `13.2545` edge `0.2754` maxDD `-19.5565`
- `market_context_high->fx_24h` score `0.1357` n `182` status `ready` deltaP `11.1473` edge `0.0419` maxDD `-1.3925`
- `market_context_high->crypto_major_4h` score `0.0607` n `199` status `ready` deltaP `9.2796` edge `0.2168` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2903` n `199` status `ready` deltaP `1.1171` edge `0.0577` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5575` n `199` status `ready` deltaP `0.7636` edge `0.0293` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5931` n `199` status `ready` deltaP `1.5226` edge `0.0036` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6963` n `199` status `ready` deltaP `5.7466` edge `0.006` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7905` n `199` status `ready` deltaP `-1.096` edge `-0.0019` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8358` n `199` status `ready` deltaP `-0.1444` edge `0.0295` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1662` n `199` status `ready` deltaP `-2.4582` edge `0.0281` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2994` n `199` status `ready` deltaP `10.516` edge `0.0908` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.387` n `199` status `ready` deltaP `-10.5497` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2276` n `199` status `ready` deltaP `-14.7001` edge `-0.1095` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
