# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T23:07:20.845781+00:00`
- Price records: `672`
- Market context records: `2708`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.6483` n `111` status `ready` deltaP `16.3523` edge `1.1277` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6062` n `111` status `ready` deltaP `17.1312` edge `0.6358` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8926` n `143` status `ready` deltaP `6.249` edge `0.1377` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2571` n `143` status `ready` deltaP `12.0758` edge `0.0366` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `0.13` n `111` status `ready` deltaP `6.5175` edge `0.7295` maxDD `-44.169`
- `market_context_high->index_1h` score `-0.1433` n `143` status `ready` deltaP `3.35` edge `0.0087` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2734` n `143` status `ready` deltaP `2.4497` edge `0.0337` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.4165` n `143` status `ready` deltaP `0.8501` edge `0.004` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.4556` n `143` status `ready` deltaP `1.8488` edge `0.0046` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.4643` n `143` status `ready` deltaP `16.3633` edge `0.2863` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.4956` n `143` status `ready` deltaP `6.4445` edge `0.0695` maxDD `-10.747`
- `market_context_high->fx_24h` score `-0.7079` n `111` status `ready` deltaP `5.2647` edge `-0.0069` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.7216` n `143` status `ready` deltaP `-0.9506` edge `-0.0016` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.8948` n `143` status `ready` deltaP `-1.049` edge `0.0103` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9401` n `143` status `ready` deltaP `3.4976` edge `0.0431` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0965` n `143` status `ready` deltaP `3.8004` edge `0.0261` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.104` n `111` status `ready` deltaP `5.7057` edge `0.1298` maxDD `-12.4171`
- `market_context_high->equity_1h` score `-1.2583` n `143` status `ready` deltaP `-4.6354` edge `0.0099` maxDD `-2.7085`
- `market_context_high->index_24h` score `-1.3692` n `111` status `ready` deltaP `1.586` edge `-0.0266` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-2.0057` n `143` status `ready` deltaP `-1.034` edge `-0.0198` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
