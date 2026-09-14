# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T16:22:31.373972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11022`

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

- `news_risk_high->unknown_4h` score `395.1488` n `78` status `ready` deltaP `-21.5408` edge `33.162` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7451` n `78` status `ready` deltaP `46.3809` edge `1.542` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.3301` n `78` status `ready` deltaP `34.1747` edge `1.3634` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.058` n `78` status `ready` deltaP `38.742` edge `1.0079` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6955` n `78` status `ready` deltaP `61.9391` edge `0.3293` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.9684` n `111` status `ready` deltaP `38.7153` edge `0.3226` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3413` n `78` status `ready` deltaP `37.7938` edge `0.3219` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.2136` n `51` status `ready` deltaP `38.7153` edge `0.2597` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2136` n `51` status `ready` deltaP `38.7153` edge `0.2597` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.7785` n `51` status `ready` deltaP `53.4211` edge `0.0463` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.7785` n `51` status `ready` deltaP `53.4211` edge `0.0463` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.3548` n `111` status `ready` deltaP `49.9765` edge `0.0513` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9241` n `52` status `ready` deltaP `25.8325` edge `0.0231` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9241` n `52` status `ready` deltaP `25.8325` edge `0.0231` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7244` n `137` status `ready` deltaP `21.2424` edge `0.0439` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7574` n `137` status `ready` deltaP `12.6623` edge `0.0164` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6524` n `78` status `ready` deltaP `15.8966` edge `0.0405` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.242` n `52` status `ready` deltaP `7.0475` edge `0.0084` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.242` n `52` status `ready` deltaP `7.0475` edge `0.0084` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2186` n `137` status `ready` deltaP `10.1589` edge `0.0079` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
