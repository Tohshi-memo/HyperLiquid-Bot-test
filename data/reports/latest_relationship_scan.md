# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T10:07:19.622317+00:00`
- Price records: `636`
- Market context records: `744`
- Flow alert records: `2100`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.7984` n `146` status `ready` deltaP `30.4845` edge `0.8967` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6119` n `146` status `ready` deltaP `7.6484` edge `0.5048` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.2097` n `146` status `ready` deltaP `1.7685` edge `0.2052` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3273` n `162` status `ready` deltaP `4.144` edge `0.0029` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4364` n `156` status `ready` deltaP `6.2063` edge `0.0094` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-0.4468` n `146` status `ready` deltaP `0.1559` edge `0.2222` maxDD `-10.5047`
- `market_context_high->commodity_1h` score `-0.5529` n `162` status `ready` deltaP `1.8105` edge `0.0393` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8488` n `162` status `ready` deltaP `1.5177` edge `0.0045` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0381` n `162` status `ready` deltaP `-0.8512` edge `0.0002` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0582` n `162` status `ready` deltaP `5.8095` edge `-0.0021` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3837` n `162` status `ready` deltaP `4.7194` edge `-0.0153` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5221` n `162` status `ready` deltaP `-4.2253` edge `-0.0215` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5681` n `156` status `ready` deltaP `17.4483` edge `0.1236` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.763` n `156` status `ready` deltaP `1.7482` edge `-0.0063` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0496` n `162` status `ready` deltaP `-4.1765` edge `-0.039` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.1763` n `156` status `ready` deltaP `2.4483` edge `0.0593` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5732` n `156` status `ready` deltaP `-1.1738` edge `0.0086` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6845` n `156` status `ready` deltaP `-5.482` edge `0.0796` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7535` n `156` status `ready` deltaP `5.0744` edge `-0.1588` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3861` n `146` status `ready` deltaP `-15.6359` edge `-0.0691` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
