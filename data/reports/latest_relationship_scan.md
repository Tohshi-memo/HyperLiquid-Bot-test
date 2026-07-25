# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T22:22:29.388921+00:00`
- Price records: `672`
- Market context records: `7923`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.5666` n `82` status `ready` deltaP `25.7749` edge `1.3429` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.404` n `82` status `ready` deltaP `39.5147` edge `0.4369` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7321` n `91` status `ready` deltaP `24.8681` edge `0.4845` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.3421` n `82` status `ready` deltaP `27.0114` edge `0.2517` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.8415` n `91` status `ready` deltaP `29.2923` edge `0.0775` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7163` n `91` status `ready` deltaP `24.1792` edge `0.1274` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7829` n `91` status `ready` deltaP `13.7297` edge `0.1388` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.3303` n `82` status `ready` deltaP `11.3059` edge `0.1622` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.3208` n `91` status `ready` deltaP `9.3725` edge `0.1593` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.2179` n `82` status `ready` deltaP `26.3635` edge `0.0345` maxDD `-3.0343`
- `market_context_high->index_1h` score `1.0588` n `91` status `ready` deltaP `16.1321` edge `0.0237` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `1.0432` n `91` status `ready` deltaP `10.6557` edge `0.1877` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.6408` n `91` status `ready` deltaP `8.9903` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5666` n `91` status `ready` deltaP `10.5893` edge `0.0429` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2125` n `91` status `ready` deltaP `4.5437` edge `0.0402` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.378` n `91` status `ready` deltaP `0.6039` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4238` n `91` status `ready` deltaP `0.693` edge `-0.0021` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5358` n `91` status `ready` deltaP `2.4314` edge `0.0156` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5955` n `91` status `ready` deltaP `3.006` edge `0.0051` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.9055` n `91` status `ready` deltaP `7.7927` edge `-0.1684` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
