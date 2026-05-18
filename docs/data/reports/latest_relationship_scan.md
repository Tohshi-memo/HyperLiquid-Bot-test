# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T00:07:16.964593+00:00`
- Price records: `672`
- Market context records: `1064`
- Flow alert records: `4969`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.3528` n `172` status `ready` deltaP `34.4332` edge `1.0962` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.1385` n `172` status `ready` deltaP `11.8358` edge `0.4727` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.1458` n `172` status `ready` deltaP `12.7368` edge `0.3144` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.5153` n `172` status `ready` deltaP `12.8215` edge `0.2466` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.0695` n `172` status `ready` deltaP `-5.1286` edge `0.4567` maxDD `-6.3373`
- `market_context_high->equity_4h` score `0.2453` n `174` status `ready` deltaP `3.818` edge `0.1003` maxDD `-5.0914`
- `market_context_high->fx_1h` score `-0.0377` n `174` status `ready` deltaP `6.0517` edge `0.0004` maxDD `-0.3124`
- `market_context_high->index_4h` score `-0.1137` n `174` status `ready` deltaP `2.4338` edge `0.057` maxDD `-3.283`
- `market_context_high->crypto_major_1h` score `-0.2329` n `174` status `ready` deltaP `7.5246` edge `0.0228` maxDD `-5.3898`
- `market_context_high->index_1h` score `-0.3629` n `174` status `ready` deltaP `4.1692` edge `0.0144` maxDD `-2.128`
- `market_context_high->equity_1h` score `-0.4277` n `174` status `ready` deltaP `0.6487` edge `0.0309` maxDD `-4.0028`
- `market_context_high->fx_4h` score `-0.6902` n `174` status `ready` deltaP `1.3142` edge `0.0024` maxDD `-1.6381`
- `market_context_high->metal_1h` score `-0.8976` n `174` status `ready` deltaP `5.0572` edge `-0.0243` maxDD `-4.0706`
- `market_context_high->crypto_alt_1h` score `-0.9536` n `174` status `ready` deltaP `1.7586` edge `0.0174` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-0.9768` n `174` status `ready` deltaP `-1.0531` edge `0.0064` maxDD `-3.7959`
- `market_context_high->crypto_major_4h` score `-1.1522` n `174` status `ready` deltaP `9.1025` edge `0.0949` maxDD `-13.1277`
- `market_context_high->crypto_alt_4h` score `-1.8972` n `174` status `ready` deltaP `2.7947` edge `0.0737` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.4263` n `174` status `ready` deltaP `1.011` edge `-0.1224` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.6305` n `174` status `ready` deltaP `-7.4379` edge `0.0291` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0763` n `172` status `ready` deltaP `5.0901` edge `-0.0207` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
