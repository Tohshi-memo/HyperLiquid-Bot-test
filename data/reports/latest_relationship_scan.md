# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T12:07:28.963252+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.5458` n `83` status `ready` deltaP `-21.9678` edge `32.2814` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.7524` n `83` status `ready` deltaP `32.1013` edge `0.9866` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.2186` n `83` status `ready` deltaP `24.1675` edge `1.0566` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.1807` n `52` status `ready` deltaP `49.4792` edge `0.4352` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1807` n `52` status `ready` deltaP `49.4792` edge `0.4352` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.7703` n `83` status `ready` deltaP `33.4003` edge `0.6856` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.8816` n `149` status `ready` deltaP `42.7678` edge `0.4242` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.7404` n `83` status `ready` deltaP `38.8303` edge `0.2371` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.9778` n `83` status `ready` deltaP `31.4696` edge `0.1671` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.6885` n `52` status `ready` deltaP `31.4728` edge `0.0492` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6885` n `52` status `ready` deltaP `31.4728` edge `0.0492` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5883` n `149` status `ready` deltaP `27.9751` edge `0.071` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.4281` n `52` status `ready` deltaP `31.9311` edge `-0.0063` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4281` n `52` status `ready` deltaP `31.9311` edge `-0.0063` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2932` n `149` status `ready` deltaP `29.1562` edge `0.0183` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1013` n `149` status `ready` deltaP `16.2109` edge `0.0214` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.478` n `52` status `ready` deltaP `9.293` edge `0.0131` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.478` n `52` status `ready` deltaP `9.293` edge `0.0131` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1664` n `83` status `ready` deltaP `9.1445` edge `0.0232` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0711` n `149` status `ready` deltaP `4.9512` edge `0.0019` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
