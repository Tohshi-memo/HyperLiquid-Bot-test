# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T10:37:35.594524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->index_1h` score `-0.4222` n `128` status `ready` deltaP `3.1437` edge `0.001` maxDD `-1.0864`
- `news_risk_high->crypto_alt_4h` score `-0.5278` n `128` status `ready` deltaP `4.0777` edge `0.1688` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6328` n `128` status `ready` deltaP `1.1321` edge `0.0341` maxDD `-5.8225`
- `news_risk_high->index_4h` score `-0.6794` n `128` status `ready` deltaP `5.7546` edge `0.012` maxDD `-2.6641`
- `news_risk_high->fx_1h` score `-0.7881` n `128` status `ready` deltaP `-4.2243` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.072` n `128` status `ready` deltaP `-5.6212` edge `-0.0089` maxDD `-1.2853`
- `news_risk_high->index_24h` score `-1.0957` n `128` status `ready` deltaP `-6.769` edge `0.1048` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-1.1905` n `128` status `ready` deltaP `-6.133` edge `-0.017` maxDD `-2.2462`
- `news_risk_high->fx_24h` score `-1.7467` n `128` status `ready` deltaP `-19.3609` edge `-0.0154` maxDD `-1.0242`
- `news_risk_high->equity_1h` score `-1.8868` n `128` status `ready` deltaP `-3.939` edge `0.0055` maxDD `-12.691`
- `news_risk_high->equity_24h` score `-1.9009` n `128` status `ready` deltaP `17.7795` edge `0.8942` maxDD `-86.0244`
- `news_risk_high->crypto_major_1h` score `-1.9576` n `128` status `ready` deltaP `-4.07` edge `-0.005` maxDD `-6.1465`
- `news_risk_high->crypto_major_4h` score `-2.6918` n `128` status `ready` deltaP `-4.9543` edge `0.0372` maxDD `-12.9458`
- `news_risk_high->commodity_1h` score `-2.8464` n `128` status `ready` deltaP `-14.2122` edge `-0.0058` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.9457` n `128` status `ready` deltaP `-9.2798` edge `-0.0628` maxDD `-5.9979`
- `news_risk_high->commodity_4h` score `-4.5294` n `128` status `ready` deltaP `-19.8933` edge `-0.0094` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-5.2955` n `128` status `ready` deltaP `6.2119` edge `0.064` maxDD `-35.0694`
- `news_risk_high->metal_24h` score `-5.983` n `128` status `ready` deltaP `-9.6561` edge `-0.2446` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.5435` n `128` status `ready` deltaP `-22.2129` edge `0.0319` maxDD `-41.9948`
- `news_risk_high->crypto_major_24h` score `-11.8076` n `128` status `ready` deltaP `-19.715` edge `0.0413` maxDD `-54.1732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
