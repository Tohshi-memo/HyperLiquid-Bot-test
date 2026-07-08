# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T11:52:27.628513+00:00`
- Price records: `672`
- Market context records: `6084`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1594` n `30` status `ready` deltaP `72.7431` edge `0.195` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.4791` n `30` status `ready` deltaP `31.7014` edge `0.26` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3029` n `32` status `ready` deltaP `44.7409` edge `0.0649` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4207` n `32` status `ready` deltaP `29.0419` edge `0.022` maxDD `-0.1113`
- `market_context_high->equity_4h` score `2.0177` n `202` status `ready` deltaP `10.4338` edge `0.1903` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1108` n `32` status `ready` deltaP `12.9304` edge `0.1029` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.6491` n `30` status `ready` deltaP `18.7848` edge `-0.0506` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.5948` n `32` status `ready` deltaP `8.6265` edge `0.0649` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1008` n `30` status `ready` deltaP `9.2361` edge `0.0385` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.2905` n `202` status `ready` deltaP `4.6392` edge `0.0117` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4528` n `202` status `ready` deltaP `1.0716` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.4628` n `202` status `ready` deltaP `2.4174` edge `0.0361` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.6281` n `202` status `ready` deltaP `5.2509` edge `0.0314` maxDD `-3.4996`
- `market_context_high->crypto_alt_1h` score `-0.7179` n `202` status `ready` deltaP `5.1921` edge `0.0486` maxDD `-9.3536`
- `market_context_high->commodity_1h` score `-0.7202` n `202` status `ready` deltaP `-1.6467` edge `-0.0044` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7225` n `32` status `ready` deltaP `-1.7964` edge `-0.0309` maxDD `-1.6464`
- `market_context_high->index_4h` score `-0.741` n `202` status `ready` deltaP `3.3491` edge `0.0291` maxDD `-1.381`
- `market_context_high->crypto_major_1h` score `-0.7653` n `202` status `ready` deltaP `5.2262` edge `0.0438` maxDD `-9.807`
- `news_risk_high->index_1h` score `-0.9862` n `32` status `ready` deltaP `-8.0277` edge `-0.0166` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1171` n `202` status `ready` deltaP `-1.623` edge `0.0049` maxDD `-0.9736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
