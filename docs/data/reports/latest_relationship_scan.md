# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T09:07:18.772226+00:00`
- Price records: `672`
- Market context records: `2230`
- Flow alert records: `8313`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `25.9219` n `33` status `ready` deltaP `56.613` edge `1.8416` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.6` n `33` status `ready` deltaP `46.9697` edge `0.9475` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9442` n `131` status `ready` deltaP `37.322` edge `0.9235` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.7091` n `33` status `ready` deltaP `37.9419` edge `0.8376` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7399` n `131` status `ready` deltaP `42.2129` edge `0.7499` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.5725` n `33` status `ready` deltaP `37.5158` edge `0.5702` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.5517` n `33` status `ready` deltaP `19.4603` edge `0.8965` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.4968` n `131` status `ready` deltaP `20.8388` edge `0.3756` maxDD `-1.8499`
- `news_risk_high->commodity_4h` score `3.9323` n `43` status `ready` deltaP `32.9197` edge `0.3518` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4664` n `131` status `ready` deltaP `23.1486` edge `0.2337` maxDD `-4.5993`
- `market_context_high->index_4h` score `3.3317` n `131` status `ready` deltaP `26.806` edge `0.1609` maxDD `-1.6242`
- `market_context_high->crypto_major_1h` score `3.1471` n `142` status `ready` deltaP `17.3062` edge `0.1946` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9628` n `33` status `ready` deltaP `31.0606` edge `0.0583` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.8981` n `142` status `ready` deltaP `16.0475` edge `0.2209` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.3878` n `33` status `ready` deltaP `-1.5941` edge `0.2913` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1622` n `43` status `ready` deltaP `27.4319` edge `0.0157` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `2.0253` n `131` status `ready` deltaP `23.7291` edge `0.4563` maxDD `-30.3243`
- `market_context_high->index_24h` score `1.6964` n `131` status `ready` deltaP `8.666` edge `0.1987` maxDD `-3.8749`
- `news_risk_high->index_24h` score `1.4191` n `33` status `ready` deltaP `10.4009` edge `0.0908` maxDD `-1.3507`
- `market_context_high->metal_4h` score `1.2803` n `131` status `ready` deltaP `16.716` edge `0.134` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
