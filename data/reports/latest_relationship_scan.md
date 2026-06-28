# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T22:37:27.668132+00:00`
- Price records: `672`
- Market context records: `5084`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.1248` n `73` status `ready` deltaP `26.8883` edge `0.8654` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `10.4929` n `105` status `ready` deltaP `1.4828` edge `0.9283` maxDD `-2.769`
- `market_context_high->unknown_4h` score `9.1605` n `93` status `ready` deltaP `21.4496` edge `0.7226` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.9783` n `93` status `ready` deltaP `16.9388` edge `0.5072` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.0499` n `93` status `ready` deltaP `15.398` edge `0.5014` maxDD `-10.3251`
- `market_context_high->equity_4h` score `2.4305` n `93` status `ready` deltaP `13.2885` edge `0.2271` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.3283` n `105` status `ready` deltaP `11.9048` edge `0.0845` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.8544` n `105` status `ready` deltaP `6.3815` edge `0.1116` maxDD `-3.9688`
- `market_context_high->crypto_major_1h` score `0.5385` n `105` status `ready` deltaP `7.6205` edge `0.1264` maxDD `-5.6537`
- `market_context_high->index_1h` score `0.5379` n `105` status `ready` deltaP `8.4488` edge `0.0183` maxDD `-0.3843`
- `market_context_high->metal_1h` score `0.4841` n `105` status `ready` deltaP `11.688` edge `0.0338` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.4467` n `93` status `ready` deltaP `8.3284` edge `0.0896` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.3452` n `93` status `ready` deltaP `8.8021` edge `0.0462` maxDD `-1.0893`
- `market_context_high->commodity_4h` score `-0.4424` n `93` status `ready` deltaP `8.9217` edge `0.0115` maxDD `-3.6276`
- `market_context_high->fx_24h` score `-0.7011` n `73` status `ready` deltaP `-1.1678` edge `-0.0059` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.7866` n `105` status `ready` deltaP `0.0142` edge `0.0027` maxDD `-1.4673`
- `market_context_high->commodity_24h` score `-1.2661` n `73` status `ready` deltaP `11.758` edge `0.0555` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.8768` n `105` status `ready` deltaP `-13.0197` edge `-0.0055` maxDD `-0.7951`
- `market_context_high->fx_4h` score `-2.0989` n `93` status `ready` deltaP `-9.1398` edge `-0.0103` maxDD `-1.6274`
- `market_context_high->metal_24h` score `-4.5706` n `73` status `ready` deltaP `-5.1441` edge `-0.0062` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
