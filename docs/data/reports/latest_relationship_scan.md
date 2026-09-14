# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T14:22:34.141509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11232`

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

- `news_risk_high->unknown_4h` score `395.4021` n `78` status `ready` deltaP `-20.4737` edge `33.176` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7504` n `78` status `ready` deltaP `46.2073` edge `1.5436` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.8348` n `78` status `ready` deltaP `35.5636` edge `1.3962` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.7717` n `78` status `ready` deltaP `37.3531` edge `0.9933` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.648` n `78` status `ready` deltaP `61.7655` edge `0.3265` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1616` n `103` status `ready` deltaP `39.9306` edge `0.3306` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2508` n `43` status `ready` deltaP `39.9306` edge `0.2547` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2508` n `43` status `ready` deltaP `39.9306` edge `0.2547` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1824` n `78` status `ready` deltaP `36.7521` edge `0.3156` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.8532` n `43` status `ready` deltaP `54.4452` edge `0.0457` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8532` n `43` status `ready` deltaP `54.4452` edge `0.0457` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.448` n `103` status `ready` deltaP `50.9456` edge `0.0526` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9631` n `52` status `ready` deltaP `26.2899` edge `0.0233` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9631` n `52` status `ready` deltaP `26.2899` edge `0.0233` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7634` n `137` status `ready` deltaP `21.6998` edge `0.0441` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6987` n `137` status `ready` deltaP `12.0635` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6152` n `78` status `ready` deltaP `15.2869` edge `0.0398` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2534` n `137` status `ready` deltaP `10.7686` edge `0.0083` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1833` n `52` status `ready` deltaP `6.4487` edge `0.0075` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1833` n `52` status `ready` deltaP `6.4487` edge `0.0075` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
