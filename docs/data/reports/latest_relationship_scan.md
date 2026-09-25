# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T15:37:32.405431+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11076`

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

- `market_context_high->unknown_1h` score `63.1283` n `47` status `ready` deltaP `7.4213` edge `5.2183` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4385` n `47` status `ready` deltaP `30.9434` edge `4.0362` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8664` n `47` status `ready` deltaP `24.782` edge `2.5283` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2651` n `47` status `ready` deltaP `34.5892` edge `1.9104` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7513` n `47` status `ready` deltaP `34.9364` edge `0.426` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3274` n `47` status `ready` deltaP `36.9681` edge `0.138` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `2.712` n `58` status `ready` deltaP `25.0838` edge `0.0936` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6496` n `47` status `ready` deltaP `30.8251` edge `0.0307` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3707` n `47` status `ready` deltaP `15.925` edge `0.1332` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1652` n `47` status `ready` deltaP `10.4502` edge `0.0942` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9487` n `47` status `ready` deltaP `11.3167` edge `0.0439` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.8932` n `111` status `ready` deltaP `9.0293` edge `0.1053` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8493` n `47` status `ready` deltaP `13.4125` edge `0.0092` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4206` n `47` status `ready` deltaP `9.5107` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.202` n `47` status `ready` deltaP `4.3031` edge `0.0699` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.0674` n `47` status `ready` deltaP `3.7753` edge `0.0709` maxDD `-5.2359`
- `market_context_high->metal_1h` score `0.032` n `47` status `ready` deltaP `3.7266` edge `0.0109` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0267` n `111` status `ready` deltaP `8.8445` edge `0.0062` maxDD `-0.7016`
- `news_risk_high->index_1h` score `-0.0137` n `111` status `ready` deltaP `3.311` edge `0.006` maxDD `-0.3863`
- `news_risk_high->crypto_major_1h` score `-0.0188` n `111` status `ready` deltaP `3.6131` edge `0.0499` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
