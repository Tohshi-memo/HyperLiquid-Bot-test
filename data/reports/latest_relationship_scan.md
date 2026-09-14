# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T21:22:28.295415+00:00`
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

- `news_risk_high->unknown_4h` score `397.0832` n `78` status `ready` deltaP `-22.4554` edge `33.3293` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.3187` n `78` status `ready` deltaP `18.9236` edge `1.9004` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.7953` n `78` status `ready` deltaP `46.0337` edge `1.5485` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.4374` n `78` status `ready` deltaP `33.3066` edge `1.2948` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.8458` n `78` status `ready` deltaP `42.2142` edge `1.0504` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7315` n `78` status `ready` deltaP `61.9391` edge `0.3323` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4373` n `78` status `ready` deltaP `37.7938` edge `0.3299` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.2273` n `125` status `ready` deltaP `36.1111` edge `0.2782` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.8517` n `51` status `ready` deltaP `36.1111` edge `0.2469` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8517` n `51` status `ready` deltaP `36.1111` edge `0.2469` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.4455` n `51` status `ready` deltaP `49.9489` edge `0.0417` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.4455` n `51` status `ready` deltaP `49.9489` edge `0.0417` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.0955` n `125` status `ready` deltaP `47.1097` edge `0.0488` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1373` n `52` status `ready` deltaP `27.3569` edge `0.0307` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1373` n `52` status `ready` deltaP `27.3569` edge `0.0307` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9376` n `137` status `ready` deltaP `22.7668` edge `0.0515` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7407` n `137` status `ready` deltaP `12.3629` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.636` n `78` status `ready` deltaP `15.8966` edge `0.0384` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
