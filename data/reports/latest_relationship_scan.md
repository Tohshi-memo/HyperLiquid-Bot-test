# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T05:52:17.193613+00:00`
- Price records: `672`
- Market context records: `835`
- Flow alert records: `2345`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1278`

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

- `market_context_high->crypto_major_24h` score `12.1664` n `154` status `ready` deltaP `28.7946` edge `0.8553` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2362` n `154` status `ready` deltaP `7.1631` edge `0.3934` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4516` n `33` status `ready` deltaP `9.4281` edge `0.2613` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4516` n `33` status `ready` deltaP `9.4281` edge `0.2613` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.5434` n `33` status `ready` deltaP `14.5741` edge `0.1236` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5434` n `33` status `ready` deltaP `14.5741` edge `0.1236` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.3725` n `33` status `ready` deltaP `18.1356` edge `0.114` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.3725` n `33` status `ready` deltaP `18.1356` edge `0.114` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.009` n `33` status `ready` deltaP `18.0432` edge `0.0676` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.009` n `33` status `ready` deltaP `18.0432` edge `0.0676` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.05` n `33` status `ready` deltaP `12.3617` edge `0.0281` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.05` n `33` status `ready` deltaP `12.3617` edge `0.0281` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8317` n `33` status `ready` deltaP `5.363` edge `0.154` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8317` n `33` status `ready` deltaP `5.363` edge `0.154` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3226` n `33` status `ready` deltaP `8.4377` edge `0.0227` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3226` n `33` status `ready` deltaP `8.4377` edge `0.0227` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2345` n `33` status `ready` deltaP `7.7981` edge `0.0016` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2345` n `33` status `ready` deltaP `7.7981` edge `0.0016` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.2079` n `33` status `ready` deltaP `3.8333` edge `-0.0218` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.2079` n `33` status `ready` deltaP `3.8333` edge `-0.0218` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
