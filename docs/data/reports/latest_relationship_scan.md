# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T18:22:32.129854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11312`

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

- `market_context_high->unknown_1h` score `64.183` n `47` status `ready` deltaP `7.7207` edge `5.3042` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6221` n `47` status `ready` deltaP `30.9434` edge `4.0515` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0896` n `47` status `ready` deltaP `24.782` edge `2.5469` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3462` n `47` status `ready` deltaP `34.7628` edge `1.916` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7393` n `47` status `ready` deltaP `34.9364` edge `0.425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.146` n `47` status `ready` deltaP `35.4056` edge `0.1333` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7073` n `47` status `ready` deltaP `17.2969` edge `0.1521` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6858` n `47` status `ready` deltaP `30.9776` edge `0.0327` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4881` n `47` status `ready` deltaP `11.5172` edge `0.114` maxDD `-3.3417`
- `news_risk_high->commodity_24h` score `1.2014` n `62` status `ready` deltaP `19.5845` edge `0.0415` maxDD `-4.0892`
- `market_context_high->equity_1h` score `1.0301` n `47` status `ready` deltaP `12.2149` edge `0.0447` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9088` n `111` status `ready` deltaP `9.179` edge `0.1056` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.884` n `47` status `ready` deltaP `13.8616` edge `0.0091` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4698` n `47` status `ready` deltaP `10.1095` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4652` n `47` status `ready` deltaP `5.1472` edge `0.0949` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2991` n `47` status `ready` deltaP `5.0516` edge `0.073` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.0783` n `111` status `ready` deltaP `4.3616` edge `0.053` maxDD `-3.3776`
- `market_context_high->metal_1h` score `0.039` n `47` status `ready` deltaP `3.8763` edge `0.0108` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0375` n `111` status `ready` deltaP `8.9942` edge `0.0061` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `0.0144` n `111` status `ready` deltaP `3.0143` edge `0.0325` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
