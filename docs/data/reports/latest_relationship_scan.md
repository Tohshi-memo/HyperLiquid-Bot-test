# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T02:22:25.980917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `53.0122` n `47` status `ready` deltaP `17.1875` edge `4.3031` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.8689` n `47` status `ready` deltaP `46.912` edge `1.1291` maxDD `-1.5549`
- `news_risk_high->unknown_4h` score `13.0541` n `51` status `ready` deltaP `23.4965` edge `0.9358` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.4738` n `47` status `ready` deltaP `54.3366` edge `0.1863` maxDD `-0.0585`
- `risk_on_high->unknown_1h` score `3.8771` n `36` status `ready` deltaP `-11.3606` edge `0.6177` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8771` n `36` status `ready` deltaP `-11.3606` edge `0.6177` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1287` n `51` status `ready` deltaP `36.8633` edge `0.0284` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.9287` n `51` status `ready` deltaP `24.0316` edge `0.1609` maxDD `-2.164`
- `news_risk_high->crypto_alt_24h` score `2.9168` n `47` status `ready` deltaP `27.4306` edge `0.0602` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2.9047` n `51` status `ready` deltaP `15.4367` edge `0.1696` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.869` n `36` status `ready` deltaP `3.1166` edge `0.2613` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.869` n `36` status `ready` deltaP `3.1166` edge `0.2613` maxDD `-0.773`
- `risk_on_high->metal_4h` score `2.3253` n `36` status `ready` deltaP `30.5048` edge `-0.0008` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3253` n `36` status `ready` deltaP `30.5048` edge `-0.0008` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1219` n `47` status `ready` deltaP `37.6292` edge `-0.0698` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.8448` n `145` status `ready` deltaP `21.3194` edge `0.0253` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.7093` n `157` status `ready` deltaP `10.7908` edge `0.1154` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2673` n `51` status `ready` deltaP `17.2948` edge `0.0073` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.0484` n `36` status `ready` deltaP `13.7026` edge `0.044` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.0484` n `36` status `ready` deltaP `13.7026` edge `0.044` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
