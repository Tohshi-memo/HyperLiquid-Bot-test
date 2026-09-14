# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T18:37:28.974628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10692`

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

- `news_risk_high->unknown_4h` score `394.9292` n `78` status `ready` deltaP `-22.4554` edge `33.1498` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.9655` n `78` status `ready` deltaP `46.9017` edge `1.5569` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.0805` n `78` status `ready` deltaP `34.1747` edge `1.3426` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.423` n `78` status `ready` deltaP `40.3045` edge `1.0279` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7123` n `78` status `ready` deltaP `61.9391` edge `0.3307` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.5758` n `118` status `ready` deltaP `37.1528` edge `0.3003` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3881` n `78` status `ready` deltaP `37.7938` edge `0.3258` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.983` n `51` status `ready` deltaP `37.1528` edge `0.2509` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.983` n `51` status `ready` deltaP `37.1528` edge `0.2509` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.6295` n `51` status `ready` deltaP `51.8586` edge `0.0443` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.6295` n `51` status `ready` deltaP `51.8586` edge `0.0443` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.2507` n `118` status `ready` deltaP `48.7347` edge `0.0509` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0269` n `52` status `ready` deltaP `26.4423` edge `0.0276` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0269` n `52` status `ready` deltaP `26.4423` edge `0.0276` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8272` n `137` status `ready` deltaP `21.8522` edge `0.0484` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8077` n `137` status `ready` deltaP `13.1114` edge `0.0176` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6399` n `78` status `ready` deltaP `15.8966` edge `0.0389` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2923` n `52` status `ready` deltaP `7.4966` edge `0.0096` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2923` n `52` status `ready` deltaP `7.4966` edge `0.0096` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2107` n `137` status `ready` deltaP `10.0064` edge `0.0079` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
