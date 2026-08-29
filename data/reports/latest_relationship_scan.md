# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T01:22:25.061010+00:00`
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

- `news_risk_high->unknown_24h` score `56.5713` n `50` status `ready` deltaP `18.3709` edge `4.5918` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6115` n `50` status `ready` deltaP `46.6066` edge `2.6177` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.3707` n `50` status `ready` deltaP `26.8076` edge `0.6515` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.7747` n `71` status `ready` deltaP `17.5863` edge `0.645` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.8383` n `50` status `ready` deltaP `30.1005` edge `0.462` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.88` n `120` status `ready` deltaP `11.7042` edge `0.4852` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4826` n `50` status `ready` deltaP `43.4073` edge `0.0884` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.2998` n `120` status `ready` deltaP `28.7406` edge `0.1853` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.075` n `75` status `ready` deltaP `7.9421` edge `0.239` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4502` n `50` status `ready` deltaP `26.9948` edge `0.0393` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2223` n `71` status `ready` deltaP `32.6112` edge `0.0227` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.2173` n `120` status `ready` deltaP `17.246` edge `0.1105` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9431` n `120` status `ready` deltaP `8.9421` edge `0.064` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.486` n `75` status `ready` deltaP `11.0619` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3972` n `75` status `ready` deltaP `11.7824` edge `0.0044` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0103` n `120` status `ready` deltaP `11.626` edge `0.0129` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3639` n `120` status `ready` deltaP `4.0619` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.5039` n `75` status `ready` deltaP `-1.7285` edge `-0.0094` maxDD `-0.8275`
- `market_context_high->crypto_alt_4h` score `-0.52` n `120` status `ready` deltaP `15.7723` edge `0.3128` maxDD `-31.4361`
- `market_context_high->crypto_major_4h` score `-0.5523` n `120` status `ready` deltaP `13.9431` edge `0.2061` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
