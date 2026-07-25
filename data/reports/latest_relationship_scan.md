# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T11:37:26.362644+00:00`
- Price records: `672`
- Market context records: `7873`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.9425` n `116` status `ready` deltaP `29.2084` edge `1.018` maxDD `-6.0681`
- `market_context_high->metal_24h` score `3.112` n `117` status `ready` deltaP `16.9696` edge `0.2778` maxDD `-1.5277`
- `market_context_high->equity_4h` score `2.6774` n `117` status `ready` deltaP `11.413` edge `0.3707` maxDD `-5.2825`
- `market_context_high->crypto_major_4h` score `1.6841` n `117` status `ready` deltaP `17.6465` edge `0.1945` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.5828` n `117` status `ready` deltaP `14.0427` edge `0.15` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.4165` n `116` status `ready` deltaP `21.2233` edge `0.1349` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1853` n `117` status `ready` deltaP `13.2479` edge `0.0504` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.121` n `116` status `ready` deltaP `30.5217` edge `0.049` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7726` n `117` status `ready` deltaP `11.0418` edge `0.1072` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.326` n `117` status `ready` deltaP `4.6382` edge `0.0395` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.2755` n `117` status `ready` deltaP `6.3319` edge `0.0401` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.1727` n `117` status `ready` deltaP `7.2073` edge `0.0171` maxDD `-0.7743`
- `market_context_high->index_4h` score `0.0112` n `117` status `ready` deltaP `11.7188` edge `0.055` maxDD `-1.2014`
- `market_context_high->commodity_1h` score `-0.0768` n `117` status `ready` deltaP `4.0656` edge `0.0124` maxDD `-0.6722`
- `market_context_high->metal_4h` score `-0.2858` n `117` status `ready` deltaP `5.9803` edge `0.0898` maxDD `-1.2788`
- `market_context_high->fx_1h` score `-0.3421` n `117` status `ready` deltaP `1.5246` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->index_24h` score `-0.8142` n `116` status `ready` deltaP `-1.91` edge `0.1093` maxDD `-1.8201`
- `market_context_high->metal_1h` score `-0.9031` n `117` status `ready` deltaP `-0.2534` edge `0.0226` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.1115` n `117` status `ready` deltaP `-1.482` edge `0.0002` maxDD `-1.6253`
- `market_context_high->crypto_alt_24h` score `-1.5669` n `117` status `ready` deltaP `13.6264` edge `0.2378` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
