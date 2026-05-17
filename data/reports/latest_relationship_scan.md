# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T12:37:13.495054+00:00`
- Price records: `672`
- Market context records: `1012`
- Flow alert records: `4823`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.2866` n `200` status `ready` deltaP `32.2308` edge `0.9512` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.2179` n `200` status `ready` deltaP `11.0385` edge `0.4013` maxDD `-9.5387`
- `market_context_high->index_24h` score `0.008` n `200` status `ready` deltaP `5.5385` edge `0.1505` maxDD `-4.9405`
- `market_context_high->equity_24h` score `-0.2848` n `200` status `ready` deltaP `5.8462` edge `0.1705` maxDD `-9.99`
- `market_context_high->fx_1h` score `-0.3228` n `200` status `ready` deltaP `1.9072` edge `-0.0002` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5402` n `200` status `ready` deltaP `2.5449` edge `0.0188` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6437` n `200` status `ready` deltaP `2.2378` edge `0.0022` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.7323` n `200` status `ready` deltaP `-0.2186` edge `0.0173` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7419` n `200` status `ready` deltaP `2.6287` edge `0.006` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.2881` n `200` status `ready` deltaP `4.1048` edge `-0.0202` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4153` n `200` status `ready` deltaP `-1.8862` edge `-0.0249` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.4225` n `200` status `ready` deltaP `1.9146` edge `0.0839` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6526` n `200` status `ready` deltaP `-1.4756` edge `0.021` maxDD `-6.2438`
- `market_context_high->metal_1h` score `-1.8061` n `200` status `ready` deltaP `0.4611` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.0001` n `200` status `ready` deltaP `6.4939` edge `0.0773` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.0985` n `200` status `ready` deltaP `-1.2073` edge `0.0666` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.1782` n `200` status `ready` deltaP `-1.5061` edge `0.023` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.3718` n `200` status `ready` deltaP `-0.1923` edge `-0.0213` maxDD `-19.4425`
- `market_context_high->metal_4h` score `-4.5338` n `200` status `ready` deltaP `-3.7317` edge `-0.166` maxDD `-24.5633`
- `market_context_high->commodity_24h` score `-8.5022` n `200` status `ready` deltaP `1.5385` edge `0.3645` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
