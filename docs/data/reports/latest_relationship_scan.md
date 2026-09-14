# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T22:22:27.375209+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10542`

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

- `news_risk_high->unknown_4h` score `397.2092` n `78` status `ready` deltaP `-22.4554` edge `33.3398` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.7603` n `78` status `ready` deltaP `18.9236` edge `1.9372` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.6588` n `78` status `ready` deltaP `45.5128` edge `1.5406` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.1791` n `78` status `ready` deltaP `32.6122` edge `1.2779` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.9734` n `78` status `ready` deltaP `42.9086` edge `1.0564` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7327` n `78` status `ready` deltaP `61.9391` edge `0.3324` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4409` n `78` status `ready` deltaP `37.7938` edge `0.3302` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `5.8591` n `129` status `ready` deltaP `34.9079` edge `0.2665` maxDD `-0.2099`
- `risk_on_high->commodity_24h` score `5.8255` n `52` status `ready` deltaP `36.4583` edge `0.2424` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8255` n `52` status `ready` deltaP `36.4583` edge `0.2424` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.3834` n `52` status `ready` deltaP `49.2922` edge `0.0409` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.3834` n `52` status `ready` deltaP `49.2922` edge `0.0409` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.0374` n `129` status `ready` deltaP `46.5641` edge `0.0476` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0837` n `52` status `ready` deltaP `26.7472` edge `0.0303` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0837` n `52` status `ready` deltaP `26.7472` edge `0.0303` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.884` n `137` status `ready` deltaP `22.1571` edge `0.0511` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7407` n `137` status `ready` deltaP `12.3629` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.674` n `78` status `ready` deltaP `16.5064` edge `0.0392` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
