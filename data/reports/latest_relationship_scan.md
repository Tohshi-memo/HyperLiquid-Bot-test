# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T10:22:27.880114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6496` n `83` status `ready` deltaP `-21.5105` edge `32.287` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.4916` n `83` status `ready` deltaP `33.3166` edge `1.0401` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.6915` n `83` status `ready` deltaP `25.3828` edge `1.0879` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.2011` n `83` status `ready` deltaP `34.6156` edge `0.7134` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.9503` n `52` status `ready` deltaP `48.2639` edge `0.4241` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9503` n `52` status `ready` deltaP `48.2639` edge `0.4241` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6512` n `149` status `ready` deltaP `41.5525` edge `0.4131` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.8724` n `83` status `ready` deltaP `40.0456` edge `0.24` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.057` n `83` status `ready` deltaP `31.4696` edge `0.1737` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5481` n `52` status `ready` deltaP `33.1463` edge `-0.0044` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5481` n `52` status `ready` deltaP `33.1463` edge `-0.0044` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.536` n `52` status `ready` deltaP `30.4057` edge `0.0436` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.536` n `52` status `ready` deltaP `30.4057` edge `0.0436` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4357` n `149` status `ready` deltaP `26.908` edge `0.0654` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.4132` n `149` status `ready` deltaP `30.3714` edge `0.0202` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0282` n `149` status `ready` deltaP `15.4624` edge `0.0203` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.405` n `52` status `ready` deltaP `8.5445` edge `0.012` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.405` n `52` status `ready` deltaP `8.5445` edge `0.012` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2499` n `83` status `ready` deltaP `10.2116` edge `0.0268` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0657` n `52` status `ready` deltaP `5.0668` edge `0.0052` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
