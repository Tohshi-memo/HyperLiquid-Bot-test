# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T04:07:26.070119+00:00`
- Price records: `672`
- Market context records: `8160`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `20.1908` n `70` status `ready` deltaP `44.4742` edge `1.4771` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5192` n `71` status `ready` deltaP `37.7748` edge `0.5649` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.8059` n `43` status `ready` deltaP `33.1892` edge `0.5331` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.4511` n `70` status `ready` deltaP `40.1042` edge `0.4369` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.3784` n `43` status `ready` deltaP `19.8809` edge `0.3762` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `4.0038` n `44` status `ready` deltaP `30.1987` edge `0.1632` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.9556` n `71` status `ready` deltaP `36.2869` edge `0.092` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.3488` n `71` status `ready` deltaP `19.3472` edge `0.1704` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.3315` n `70` status `ready` deltaP `22.1925` edge `0.1967` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8006` n `43` status `ready` deltaP `23.316` edge `0.097` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.2393` n `71` status `ready` deltaP `23.1965` edge `0.0942` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9371` n `70` status `ready` deltaP `26.0665` edge `0.058` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.6492` n `43` status `ready` deltaP `15.4991` edge `0.0809` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.5484` n `71` status `ready` deltaP `18.8644` edge `0.0229` maxDD `-0.2368`
- `market_context_high->crypto_major_4h` score `1.5348` n `71` status `ready` deltaP `10.1855` edge `0.2318` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.5157` n `71` status `ready` deltaP `7.7894` edge `0.1861` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.4987` n `70` status `ready` deltaP `30.8978` edge `0.2747` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `1.474` n `44` status `ready` deltaP `7.3898` edge `0.1133` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1352` n `43` status `ready` deltaP `12.4078` edge `0.202` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `1.0818` n `71` status `ready` deltaP `11.9992` edge `0.0512` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
