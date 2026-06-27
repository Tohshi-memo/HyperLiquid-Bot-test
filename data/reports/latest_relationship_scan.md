# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T21:43:23.705292+00:00`
- Price records: `672`
- Market context records: `4975`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `18.2902` n `97` status `ready` deltaP `5.7859` edge `1.5357` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.8075` n `88` status `ready` deltaP `28.4645` edge `0.9301` maxDD `-1.8723`
- `market_context_high->crypto_major_4h` score `7.315` n `88` status `ready` deltaP `20.025` edge `0.5985` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.8597` n `88` status `ready` deltaP `20.6208` edge `0.5694` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8775` n `84` status `ready` deltaP `27.8026` edge `0.3387` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.6838` n `88` status `ready` deltaP `12.8049` edge `0.1931` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6637` n `88` status `ready` deltaP `13.5255` edge `0.1272` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8191` n `88` status `ready` deltaP `10.3243` edge `0.0456` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.4901` n `97` status `ready` deltaP `6.8507` edge `0.0745` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.3491` n `97` status `ready` deltaP `4.2749` edge `0.1201` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.2882` n `97` status `ready` deltaP `6.4186` edge `0.0964` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.1` n `97` status `ready` deltaP `2.2131` edge `0.0349` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.38` n `97` status `ready` deltaP `1.4476` edge `0.0076` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.449` n `97` status `ready` deltaP `0.7979` edge `0.0126` maxDD `-0.7054`
- `market_context_high->fx_24h` score `-0.8968` n `84` status `ready` deltaP `1.0913` edge `-0.0056` maxDD `-1.7793`
- `market_context_high->fx_4h` score `-1.1262` n `88` status `ready` deltaP `-6.6658` edge `-0.0029` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.3078` n `88` status `ready` deltaP `4.2267` edge `-0.0119` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.6438` n `97` status `ready` deltaP `-10.9066` edge `-0.0043` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.0949` n `84` status `ready` deltaP `15.6002` edge `0.0101` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9744` n `84` status `ready` deltaP `-7.8621` edge `0.0167` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
