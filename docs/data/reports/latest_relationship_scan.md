# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T14:52:26.381579+00:00`
- Price records: `672`
- Market context records: `2979`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6956`

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

- `market_context_high->crypto_alt_24h` score `15.5616` n `104` status `ready` deltaP `6.9712` edge `1.642` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.019` n `104` status `ready` deltaP `39.8905` edge `0.6704` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `10.1284` n `104` status `ready` deltaP `15.9455` edge `0.7842` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7492` n `104` status `ready` deltaP `15.9455` edge `0.6565` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.0898` n `104` status `ready` deltaP `15.9588` edge `0.3325` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.8358` n `105` status `ready` deltaP `15.3688` edge `0.1728` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.1161` n `105` status `ready` deltaP `20.1713` edge `0.1207` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `1.8239` n `105` status `ready` deltaP `14.4164` edge `0.1206` maxDD `-2.8438`
- `market_context_high->equity_1h` score `1.0817` n `105` status `ready` deltaP `8.2164` edge `0.0687` maxDD `-1.0004`
- `market_context_high->index_1h` score `0.7666` n `105` status `ready` deltaP `9.7548` edge `0.038` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.4232` n `105` status `ready` deltaP `21.5085` edge `0.367` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `-0.1216` n `105` status `ready` deltaP `9.0476` edge `0.0876` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.1647` n `105` status `ready` deltaP `0.4349` edge `0.0158` maxDD `-1.5182`
- `market_context_high->crypto_major_1h` score `-0.2674` n `105` status `ready` deltaP `9.1845` edge `0.0581` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.4742` n `105` status `ready` deltaP `-1.6196` edge `0.002` maxDD `-0.1244`
- `market_context_high->fx_4h` score `-1.02` n `105` status `ready` deltaP `-7.9051` edge `-0.0002` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.1641` n `105` status `ready` deltaP `-0.8958` edge `0.0143` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.2847` n `105` status `ready` deltaP `-2.7474` edge `0.0` maxDD `-3.4325`
- `market_context_high->fx_24h` score `-1.3786` n `104` status `ready` deltaP `-9.0678` edge `-0.0291` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.4938` n `105` status `ready` deltaP `2.1899` edge `-0.066` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
