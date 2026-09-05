# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T22:22:30.496887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10805`

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

- `risk_on_high->unknown_4h` score `20.49` n `133` status `ready` deltaP `-2.7061` edge `1.9261` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.49` n `133` status `ready` deltaP `-2.7061` edge `1.9261` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.087` n `228` status `ready` deltaP `1.8052` edge `0.9087` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.4463` n `37` status `ready` deltaP `25.1783` edge `0.3963` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8851` n `37` status `ready` deltaP `20.1389` edge `0.1895` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2491` n `37` status `ready` deltaP `16.2657` edge `0.2036` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3381` n `37` status `ready` deltaP `23.694` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6039` n `37` status `ready` deltaP `13.2344` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5758` n `37` status `ready` deltaP `7.7703` edge `0.0996` maxDD `-0.2737`
- `market_context_high->equity_24h` score `1.3241` n `159` status `ready` deltaP `13.2109` edge `0.4453` maxDD `-20.5089`
- `news_risk_high->metal_1h` score `1.2957` n `37` status `ready` deltaP `15.4637` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1151` n `37` status `ready` deltaP `5.8667` edge `0.0721` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `0.9202` n `37` status `ready` deltaP `19.9559` edge `0.0452` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8302` n `37` status `ready` deltaP `8.2781` edge `0.0405` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.2751` n `37` status `ready` deltaP `15.8831` edge `0.207` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.203` n `37` status `ready` deltaP `3.8069` edge `0.0244` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0507` n `145` status `ready` deltaP `6.1666` edge `-0.0029` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0507` n `145` status `ready` deltaP `6.1666` edge `-0.0029` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0597` n `37` status `ready` deltaP `5.1263` edge `0.0028` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
