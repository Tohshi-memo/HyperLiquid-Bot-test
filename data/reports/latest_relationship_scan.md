# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T14:37:29.050097+00:00`
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

- `news_risk_high->unknown_4h` score `395.3648` n `78` status `ready` deltaP `-20.6261` edge `33.1739` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.736` n `78` status `ready` deltaP `46.2073` edge `1.5424` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.7573` n `78` status `ready` deltaP `35.39` edge `1.3909` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.812` n `78` status `ready` deltaP `37.5267` edge `0.9955` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.654` n `78` status `ready` deltaP `61.7655` edge `0.327` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1748` n `104` status `ready` deltaP `39.9306` edge `0.3317` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.3228` n `44` status `ready` deltaP `39.9306` edge `0.2607` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3228` n `44` status `ready` deltaP `39.9306` edge `0.2607` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.2106` n `78` status `ready` deltaP `36.9257` edge `0.3168` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.8471` n `44` status `ready` deltaP `54.3245` edge `0.046` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8471` n `44` status `ready` deltaP `54.3245` edge `0.046` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4373` n `104` status `ready` deltaP `50.828` edge `0.0525` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9485` n `52` status `ready` deltaP `26.1374` edge `0.0231` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9485` n `52` status `ready` deltaP `26.1374` edge `0.0231` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7488` n `137` status `ready` deltaP `21.5473` edge `0.0439` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6963` n `137` status `ready` deltaP `12.0635` edge `0.0153` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6247` n `78` status `ready` deltaP `15.4393` edge `0.04` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2447` n `137` status `ready` deltaP `10.6162` edge `0.0082` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
