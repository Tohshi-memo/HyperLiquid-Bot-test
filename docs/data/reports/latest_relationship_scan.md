# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T08:52:19.423876+00:00`
- Price records: `672`
- Market context records: `3162`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.7955` n `103` status `ready` deltaP `47.0621` edge `0.8787` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1076` n `103` status `ready` deltaP `15.6098` edge `2.4458` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7736` n `103` status `ready` deltaP `20.7642` edge `0.8915` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.2895` n `103` status `ready` deltaP `29.7599` edge `0.8634` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8428` n `103` status `ready` deltaP `13.963` edge `1.3694` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.947` n `136` status `ready` deltaP `18.5527` edge `0.1677` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6273` n `103` status `ready` deltaP `12.0702` edge `0.0029` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2298` n `136` status `ready` deltaP `4.5615` edge `0.031` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4108` n `136` status `ready` deltaP `5.7591` edge `0.1219` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4273` n `136` status `ready` deltaP `5.1603` edge `0.0171` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.7155` n `136` status `ready` deltaP `9.8996` edge `0.0966` maxDD `-14.7778`
- `market_context_high->equity_1h` score `-0.8781` n `136` status `ready` deltaP `3.54` edge `0.0124` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.0064` n `136` status `ready` deltaP `14.4728` edge `0.0654` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0372` n `136` status `ready` deltaP `2.8971` edge `0.074` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0992` n `136` status `ready` deltaP `-10.1048` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.3857` n `136` status `ready` deltaP `-12.2669` edge `-0.0074` maxDD `-1.4115`
- `market_context_high->crypto_alt_4h` score `-1.9903` n `136` status `ready` deltaP `19.0369` edge `0.4224` maxDD `-58.6918`
- `market_context_high->metal_1h` score `-2.0868` n `136` status `ready` deltaP `-3.9495` edge `-0.0082` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.9298` n `136` status `ready` deltaP `14.123` edge `0.0608` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.1555` n `136` status `ready` deltaP `2.1266` edge `-0.0745` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
