# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T21:37:31.619978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9826`

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

- `market_context_high->unknown_1h` score `72.1891` n `47` status `ready` deltaP `10.116` edge `5.9554` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.989` n `46` status `ready` deltaP `20.4786` edge `2.7115` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.5936` n `46` status `ready` deltaP `17.8744` edge `1.5237` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.2729` n `46` status `ready` deltaP `15.4514` edge `1.3364` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.3329` n `97` status `ready` deltaP `-3.0087` edge `1.4003` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.6065` n `46` status `ready` deltaP `26.9022` edge `0.3799` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.5406` n `103` status `ready` deltaP `13.317` edge `0.3894` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5032` n `103` status `ready` deltaP `17.2804` edge `0.3178` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.3822` n `97` status `ready` deltaP `-5.1672` edge `0.8044` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7327` n `97` status `ready` deltaP `25.9521` edge `0.1726` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.473` n `103` status `ready` deltaP `13.1577` edge `0.1674` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3956` n `47` status `ready` deltaP `28.3861` edge `0.0258` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9881` n `103` status `ready` deltaP `15.5529` edge `0.1055` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4686` n `103` status `ready` deltaP `21.8521` edge `0.0403` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.3333` n `46` status `ready` deltaP `20.8787` edge `-0.0047` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.1601` n `47` status `ready` deltaP `9.5225` edge `0.075` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1094` n `97` status `ready` deltaP `27.6221` edge `0.1212` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7103` n `47` status `ready` deltaP `11.9155` edge `0.0076` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5811` n `103` status `ready` deltaP `14.7535` edge `0.0094` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5286` n `97` status `ready` deltaP `16.9566` edge `0.0465` maxDD `-3.0086`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
