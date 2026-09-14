# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T14:07:45.009287+00:00`
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

- `news_risk_high->unknown_4h` score `388.9215` n `79` status `ready` deltaP `-19.9869` edge `32.6327` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.3489` n `79` status `ready` deltaP `45.1037` edge `1.5175` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.4106` n `79` status `ready` deltaP `34.731` edge `1.3664` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.7361` n `79` status `ready` deltaP `37.5528` edge `0.989` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6112` n `79` status `ready` deltaP `61.7703` edge `0.3234` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1472` n `102` status `ready` deltaP `39.9306` edge `0.3294` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1871` n `79` status `ready` deltaP `36.8869` edge `0.3151` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.174` n `42` status `ready` deltaP `39.9306` edge `0.2483` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.174` n `42` status `ready` deltaP `39.9306` edge `0.2483` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.8567` n `42` status `ready` deltaP `54.5634` edge `0.0452` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8567` n `42` status `ready` deltaP `54.5634` edge `0.0452` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4573` n `102` status `ready` deltaP `51.062` edge `0.0526` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9667` n `52` status `ready` deltaP `26.2899` edge `0.0236` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9667` n `52` status `ready` deltaP `26.2899` edge `0.0236` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.767` n `137` status `ready` deltaP `21.6998` edge `0.0444` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6987` n `137` status `ready` deltaP `12.0635` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.643` n `79` status `ready` deltaP `15.79` edge `0.04` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2622` n `137` status `ready` deltaP `10.9211` edge `0.0084` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1833` n `52` status `ready` deltaP `6.4487` edge `0.0075` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1833` n `52` status `ready` deltaP `6.4487` edge `0.0075` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
