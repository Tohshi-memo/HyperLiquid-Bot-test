# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T04:22:26.681083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10815`

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

- `risk_on_high->unknown_4h` score `21.8393` n `145` status `ready` deltaP `-3.4651` edge `2.0436` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.8393` n `145` status `ready` deltaP `-3.4651` edge `2.0436` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.3721` n `245` status `ready` deltaP `1.0951` edge `0.9372` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.3049` n `37` status `ready` deltaP `21.7061` edge `0.241` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9703` n `37` status `ready` deltaP `20.1389` edge `0.1966` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.1633` n `37` status `ready` deltaP `15.8084` edge `0.1995` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.5149` n `37` status `ready` deltaP `25.8281` edge `0.0595` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.7895` n `166` status `ready` deltaP `13.7195` edge `0.4115` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5596` n `37` status `ready` deltaP `12.7853` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5332` n `37` status `ready` deltaP `7.313` edge `0.0991` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3317` n `37` status `ready` deltaP `15.9128` edge `0.0242` maxDD `-0.2118`
- `risk_on_high->crypto_major_24h` score `1.244` n `83` status `ready` deltaP `11.293` edge `0.8168` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.244` n `83` status `ready` deltaP `11.293` edge `0.8168` maxDD `-47.9416`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.103` n `37` status `ready` deltaP `21.8656` edge `0.0477` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.0348` n `37` status `ready` deltaP `5.4176` edge `0.0684` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.7762` n `37` status `ready` deltaP `8.2781` edge `0.036` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `-0.0286` n `37` status `ready` deltaP `5.7251` edge `0.0028` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1162` n `145` status `ready` deltaP `4.937` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1162` n `145` status `ready` deltaP `4.937` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
