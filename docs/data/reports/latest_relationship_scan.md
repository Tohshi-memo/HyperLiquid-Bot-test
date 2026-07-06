# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T02:22:24.966461+00:00`
- Price records: `672`
- Market context records: `5835`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.6153` n `268` status `ready` deltaP `7.6129` edge `0.1463` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.3057` n `268` status `ready` deltaP `1.4166` edge `-0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4223` n `268` status `ready` deltaP `4.1559` edge `0.0378` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5186` n `268` status `ready` deltaP `-0.6636` edge `-0.0018` maxDD `-2.1545`
- `market_context_high->equity_24h` score `-0.5532` n `240` status `ready` deltaP `15.6598` edge `0.3574` maxDD `-31.6316`
- `market_context_high->index_1h` score `-0.5582` n `268` status `ready` deltaP `1.1864` edge `0.0053` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6265` n `268` status `ready` deltaP `2.2321` edge `0.0` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-1.0084` n `268` status `ready` deltaP `2.6052` edge `0.0307` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1692` n `268` status `ready` deltaP `1.1127` edge `0.0286` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1732` n `268` status `ready` deltaP `0.6029` edge `0.0143` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.6295` n `240` status `ready` deltaP `7.7083` edge `0.0215` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.6327` n `268` status `ready` deltaP `-1.9817` edge `-0.0012` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2053` n `268` status `ready` deltaP `-5.1465` edge `-0.0453` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.5391` n `268` status `ready` deltaP `-0.744` edge `-0.0143` maxDD `-8.0531`
- `market_context_high->index_24h` score `-2.8955` n `240` status `ready` deltaP `2.9167` edge `0.0238` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.1446` n `268` status `ready` deltaP `6.2682` edge `0.1334` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8966` n `268` status `ready` deltaP `3.8246` edge `0.0673` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.3054` n `240` status `ready` deltaP `-0.1736` edge `-0.2082` maxDD `-9.9543`
- `market_context_high->commodity_24h` score `-8.7275` n `240` status `ready` deltaP `-11.0764` edge `-0.0575` maxDD `-30.3426`
- `market_context_high->crypto_alt_24h` score `-12.7906` n `240` status `ready` deltaP `-11.8403` edge `-0.5302` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
