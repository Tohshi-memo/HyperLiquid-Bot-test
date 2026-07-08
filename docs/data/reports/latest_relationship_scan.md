# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T09:42:13.031420+00:00`
- Price records: `672`
- Market context records: `6074`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.1606` n `30` status `ready` deltaP `72.7431` edge `0.1951` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3817` n `30` status `ready` deltaP `45.3354` edge `0.0675` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `4.0749` n `30` status `ready` deltaP `30.1389` edge `0.1534` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.1916` edge `0.022` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6325` n `206` status `ready` deltaP `9.0989` edge `0.1671` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2027` n `32` status `ready` deltaP `13.8286` edge `0.1087` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.1101` n `30` status `ready` deltaP `20.3473` edge `-0.0226` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6501` n `32` status `ready` deltaP `9.2253` edge `0.068` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0906` n `30` status `ready` deltaP `9.2361` edge `0.0372` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3643` n `206` status `ready` deltaP `3.7294` edge `0.0083` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5342` n `206` status `ready` deltaP `0.3081` edge `-0.0009` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.7606` n `32` status `ready` deltaP `-2.0958` edge `-0.0338` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7667` n `206` status `ready` deltaP `4.7047` edge `0.0456` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.7841` n `206` status `ready` deltaP `4.9997` edge `0.0429` maxDD `-9.807`
- `market_context_high->commodity_1h` score `-0.8057` n `206` status `ready` deltaP `-2.4315` edge `-0.0063` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.843` n `206` status `ready` deltaP `1.6787` edge `0.0314` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-0.8715` n `206` status `ready` deltaP `4.6383` edge `0.0152` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.8982` n `206` status `ready` deltaP `2.2629` edge `0.0231` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-0.9668` n `32` status `ready` deltaP `-7.7283` edge `-0.0161` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2043` n `206` status `ready` deltaP `-2.2368` edge `0.0044` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
