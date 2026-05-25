# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T12:07:18.004830+00:00`
- Price records: `672`
- Market context records: `1840`
- Flow alert records: `7197`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.8828` n `196` status `ready` deltaP `22.9249` edge `0.5352` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.4151` n `178` status `ready` deltaP `25.3336` edge `0.6083` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.3183` n `196` status `ready` deltaP `26.1044` edge `0.4771` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3941` n `196` status `ready` deltaP `17.3656` edge `0.4528` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.3372` n `178` status `ready` deltaP `17.0003` edge `0.2876` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.7628` n `196` status `ready` deltaP `15.9128` edge `0.2336` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7099` n `178` status `ready` deltaP `14.56` edge `0.6608` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.5546` n `178` status `ready` deltaP `13.9786` edge `0.5262` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.7735` n `196` status `ready` deltaP `11.9183` edge `0.0939` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3852` n `199` status `ready` deltaP `5.4472` edge `0.0944` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.3172` n `178` status `ready` deltaP `19.7273` edge `0.7535` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2042` n `199` status `ready` deltaP `5.4577` edge `0.092` maxDD `-4.9097`
- `market_context_high->fx_24h` score `-0.0449` n `178` status `ready` deltaP `12.1294` edge `0.0203` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0843` n `199` status `ready` deltaP `4.388` edge `0.0431` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5216` n `199` status `ready` deltaP `3.1377` edge `0.0308` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5326` n `196` status `ready` deltaP `13.2` edge `0.1368` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5959` n `199` status `ready` deltaP `5.3832` edge `0.0213` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6122` n `199` status `ready` deltaP `-0.006` edge `0.0122` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7298` n `199` status `ready` deltaP `-4.4` edge `-0.001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0608` n `196` status `ready` deltaP `-5.8922` edge `-0.0079` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
