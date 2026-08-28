# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T22:52:29.207382+00:00`
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

- `news_risk_high->unknown_24h` score `55.775` n `50` status `ready` deltaP `16.6378` edge `4.537` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4207` n `50` status `ready` deltaP `46.6066` edge `2.6018` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `8.7965` n `71` status `ready` deltaP `17.7387` edge `0.6458` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `8.6091` n `50` status `ready` deltaP `26.2877` edge `0.5915` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.4939` n `50` status `ready` deltaP `30.1005` edge `0.4333` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.0837` n `120` status `ready` deltaP `9.9711` edge `0.4304` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4334` n `50` status `ready` deltaP `43.4073` edge `0.0843` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.5185` n `71` status `ready` deltaP `9.1064` edge `0.2682` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2506` n `120` status `ready` deltaP `28.7406` edge `0.1812` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4202` n `50` status `ready` deltaP `26.9948` edge `0.0368` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2391` n `120` status `ready` deltaP `17.3984` edge `0.1113` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1298` n `71` status `ready` deltaP `31.5441` edge `0.0221` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9311` n `120` status `ready` deltaP `8.9421` edge `0.063` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.583` n `71` status `ready` deltaP `12.2101` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3751` n `71` status `ready` deltaP `11.4616` edge `0.0037` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0776` n `120` status `ready` deltaP `13.1504` edge `0.014` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.4036` n `120` status `ready` deltaP `3.3134` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4592` n `71` status `ready` deltaP `-0.8813` edge `-0.0096` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.7009` n `71` status `ready` deltaP `-0.8539` edge `-0.0266` maxDD `-2.605`
- `news_risk_high->equity_1h` score `-0.7249` n `71` status `ready` deltaP `6.7597` edge `-0.0446` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
