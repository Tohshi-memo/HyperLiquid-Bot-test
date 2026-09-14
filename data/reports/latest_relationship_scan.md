# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T20:52:29.493805+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10608`

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

- `news_risk_high->unknown_4h` score `396.9752` n `78` status `ready` deltaP `-22.4554` edge `33.3203` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.0115` n `78` status `ready` deltaP `18.9236` edge `1.8748` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.8375` n `78` status `ready` deltaP `46.3809` edge `1.5497` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.5576` n `78` status `ready` deltaP `33.6539` edge `1.3025` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.7784` n `78` status `ready` deltaP `41.867` edge `1.0471` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7303` n `78` status `ready` deltaP `61.9391` edge `0.3322` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4337` n `78` status `ready` deltaP `37.7938` edge `0.3296` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.2837` n `123` status `ready` deltaP `36.1111` edge `0.2829` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.8589` n `51` status `ready` deltaP `36.1111` edge `0.2475` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8589` n `51` status `ready` deltaP `36.1111` edge `0.2475` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.4781` n `51` status `ready` deltaP `50.2961` edge `0.0421` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.4781` n `51` status `ready` deltaP `50.2961` edge `0.0421` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.123` n `123` status `ready` deltaP `47.3789` edge `0.0493` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1373` n `52` status `ready` deltaP `27.3569` edge `0.0307` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1373` n `52` status `ready` deltaP `27.3569` edge `0.0307` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9376` n `137` status `ready` deltaP `22.7668` edge `0.0515` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.767` n `137` status `ready` deltaP `12.6623` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6265` n `78` status `ready` deltaP `15.7442` edge `0.0382` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2516` n `52` status `ready` deltaP `7.0475` edge `0.0092` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2516` n `52` status `ready` deltaP `7.0475` edge `0.0092` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
