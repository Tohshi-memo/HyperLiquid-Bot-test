# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T18:37:18.362462+00:00`
- Price records: `672`
- Market context records: `1553`
- Flow alert records: `6382`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.407` n `182` status `ready` deltaP `23.4699` edge `0.9775` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.845` n `182` status `ready` deltaP `26.9974` edge `0.9254` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2877` n `182` status `ready` deltaP `26.7399` edge `0.7089` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.092` n `182` status `ready` deltaP `20.7799` edge `0.3111` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7144` n `182` status `ready` deltaP `14.0682` edge `0.3651` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.5976` n `182` status `ready` deltaP `15.6612` edge `0.0503` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3255` n `199` status `ready` deltaP `5.3959` edge `0.1006` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.1474` n `199` status `ready` deltaP `13.2545` edge `0.2247` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.246` n `199` status `ready` deltaP `9.1272` edge `0.1785` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4182` n `199` status `ready` deltaP `0.8177` edge `0.0433` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6327` n `199` status `ready` deltaP `-2.1439` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6939` n `199` status `ready` deltaP `-0.0481` edge `0.0035` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7431` n `199` status `ready` deltaP `5.1478` edge `0.004` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.8063` n `199` status `ready` deltaP `-0.5732` edge `-0.0002` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8092` n `199` status `ready` deltaP `-1.0328` edge `0.0203` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9652` n `199` status `ready` deltaP `-0.8929` edge `0.0179` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3715` n `199` status `ready` deltaP `10.3636` edge `0.0858` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3729` n `199` status `ready` deltaP `-10.3973` edge `-0.0138` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4632` n `199` status `ready` deltaP `-4.7448` edge `0.0186` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.1094` n `199` status `ready` deltaP `-14.2427` edge `-0.0974` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
