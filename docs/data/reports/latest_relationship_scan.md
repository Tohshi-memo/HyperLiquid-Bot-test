# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T01:07:23.793129+00:00`
- Price records: `672`
- Market context records: `1172`
- Flow alert records: `5277`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.7171` n `141` status `ready` deltaP `45.9478` edge `1.5333` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1282` n `141` status `ready` deltaP `22.1779` edge `0.8978` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.4822` n `141` status `ready` deltaP `21.4687` edge `0.5734` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.667` n `141` status `ready` deltaP `20.6154` edge `0.3906` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.639` n `141` status `ready` deltaP `-3.2506` edge `0.6583` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5073` n `153` status `ready` deltaP `12.8657` edge `0.1895` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1868` n `153` status `ready` deltaP `9.51` edge `0.1038` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5499` n `153` status `ready` deltaP `8.1777` edge `0.023` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3123` n `153` status `ready` deltaP `3.0586` edge `0.0434` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1486` n `153` status `ready` deltaP `8.6484` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.076` n `153` status `ready` deltaP `8.1699` edge `0.1474` maxDD `-8.3693`
- `market_context_high->unknown_24h` score `0.051` n `141` status `ready` deltaP `3.5129` edge `0.2538` maxDD `-10.1706`
- `market_context_high->crypto_major_1h` score `-0.0786` n `153` status `ready` deltaP `6.0741` edge `0.026` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.1286` n `153` status `ready` deltaP `6.0358` edge `0.0707` maxDD `-6.7322`
- `market_context_high->metal_1h` score `-0.4393` n `153` status `ready` deltaP `5.764` edge `-0.014` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.5375` n `153` status `ready` deltaP `1.5283` edge `0.0293` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8412` n `153` status `ready` deltaP `-3.4451` edge `-0.0041` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0173` n `153` status `ready` deltaP `-3.8976` edge `-0.0048` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3649` n `153` status `ready` deltaP `3.795` edge `0.0962` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9169` n `153` status `ready` deltaP `4.7326` edge `-0.0819` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
