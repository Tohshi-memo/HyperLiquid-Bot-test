# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T22:36:30.265399+00:00`
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

- `news_risk_high->unknown_4h` score `397.4456` n `78` status `ready` deltaP `-22.4554` edge `33.3595` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.8635` n `78` status `ready` deltaP `18.9236` edge `1.9458` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.6005` n `78` status `ready` deltaP `45.3392` edge `1.5369` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.1064` n `78` status `ready` deltaP `32.4386` edge `1.273` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.0004` n `78` status `ready` deltaP `43.0822` edge `1.0575` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7315` n `78` status `ready` deltaP `61.9391` edge `0.3323` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4421` n `78` status `ready` deltaP `37.7938` edge `0.3303` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.8442` n `52` status `ready` deltaP `36.6319` edge `0.2428` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8442` n `52` status `ready` deltaP `36.6319` edge `0.2428` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.6992` n `130` status `ready` deltaP `34.3242` edge `0.2626` maxDD `-0.3193`
- `risk_on_high->fx_24h` score `4.3671` n `52` status `ready` deltaP `49.1186` edge `0.0407` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.3671` n `52` status `ready` deltaP `49.1186` edge `0.0407` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.0204` n `130` status `ready` deltaP `46.4263` edge `0.0471` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0667` n `52` status `ready` deltaP `26.5947` edge `0.0299` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0667` n `52` status `ready` deltaP `26.5947` edge `0.0299` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.867` n `137` status `ready` deltaP `22.0046` edge `0.0507` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7419` n `137` status `ready` deltaP `12.3629` edge `0.0171` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6835` n `78` status `ready` deltaP `16.6588` edge `0.0394` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2264` n `52` status `ready` deltaP `6.7481` edge `0.0091` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2264` n `52` status `ready` deltaP `6.7481` edge `0.0091` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
