# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T21:37:28.246925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `55.3133` n `50` status `ready` deltaP `15.7712` edge `4.5043` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.1488` n `50` status `ready` deltaP `46.4333` edge `2.5803` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `9.1259` n `69` status `ready` deltaP `18.5865` edge `0.6676` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `7.9716` n `50` status `ready` deltaP `25.5945` edge `0.543` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.3175` n `50` status `ready` deltaP `30.1005` edge `0.4186` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `4.622` n `120` status `ready` deltaP `9.1045` edge `0.3977` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4022` n `50` status `ready` deltaP `43.4073` edge `0.0817` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4753` n `71` status `ready` deltaP `9.2561` edge `0.2636` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2194` n `120` status `ready` deltaP `28.7406` edge `0.1786` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4058` n `50` status `ready` deltaP `26.9948` edge `0.0356` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2701` n `120` status `ready` deltaP `17.246` edge `0.1149` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1706` n `69` status `ready` deltaP `31.9945` edge `0.0225` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.8879` n `120` status `ready` deltaP `9.0918` edge `0.0584` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6081` n `71` status `ready` deltaP `12.5095` edge `0.006` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3665` n `71` status `ready` deltaP `11.3119` edge `0.0036` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0855` n `120` status `ready` deltaP `13.3028` edge `0.014` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3873` n `120` status `ready` deltaP `3.6128` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4841` n `71` status `ready` deltaP `-1.3304` edge `-0.0098` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.6767` n `71` status `ready` deltaP `-0.4048` edge `-0.0265` maxDD `-2.605`
- `news_risk_high->index_4h` score `-0.6792` n `69` status `ready` deltaP `-0.5722` edge `-0.0201` maxDD `-1.7198`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
