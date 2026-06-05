# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T15:07:34.816667+00:00`
- Price records: `672`
- Market context records: `2980`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `15.5059` n `103` status `ready` deltaP `6.5753` edge `1.64` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.098` n `103` status `ready` deltaP `40.0081` edge `0.6762` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `10.252` n `103` status `ready` deltaP `15.9604` edge `0.7944` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7215` n `103` status `ready` deltaP `15.8391` edge `0.6549` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.1236` n `103` status `ready` deltaP `15.8711` edge `0.3359` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.8772` n `104` status `ready` deltaP `15.2556` edge `0.177` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.1356` n `104` status `ready` deltaP `20.0399` edge `0.1232` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `1.8334` n `104` status `ready` deltaP `14.294` edge `0.1222` maxDD `-2.8438`
- `market_context_high->equity_1h` score `0.929` n `105` status `ready` deltaP `7.4138` edge `0.063` maxDD `-1.1343`
- `market_context_high->index_1h` score `0.6772` n `105` status `ready` deltaP `8.9521` edge `0.0359` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.3895` n `104` status `ready` deltaP `21.2946` edge `0.3641` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `-0.2019` n `105` status `ready` deltaP `9.0476` edge `0.0773` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.2384` n `105` status `ready` deltaP `-0.3678` edge `0.0117` maxDD `-1.5182`
- `market_context_high->crypto_major_1h` score `-0.3762` n `105` status `ready` deltaP `8.3818` edge `0.0495` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.5456` n `105` status `ready` deltaP `-2.4223` edge `0.0014` maxDD `-0.1244`
- `market_context_high->fx_4h` score `-1.0399` n `104` status `ready` deltaP `-8.3021` edge `-0.0001` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.3397` n `105` status `ready` deltaP `-2.7474` edge `0.0005` maxDD `-3.8394`
- `market_context_high->unknown_4h` score `-1.369` n `104` status `ready` deltaP `-1.372` edge `0.0004` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.3851` n `103` status `ready` deltaP `-9.193` edge `-0.0291` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.603` n `105` status `ready` deltaP `2.1899` edge `-0.0751` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
