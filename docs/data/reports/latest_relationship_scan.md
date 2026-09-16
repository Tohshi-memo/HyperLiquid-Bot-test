# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T10:07:30.828229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `356.2042` n `83` status `ready` deltaP `-21.6629` edge `29.9162` maxDD `-4.0481`
- `news_risk_high->crypto_alt_24h` score `24.278` n `78` status `ready` deltaP `47.7698` edge `1.7439` maxDD `-1.4689`
- `news_risk_high->crypto_major_24h` score `23.6636` n `78` status `ready` deltaP `39.7303` edge `1.8704` maxDD `-10.3977`
- `news_risk_high->equity_24h` score `15.671` n `78` status `ready` deltaP `47.7697` edge `1.1677` maxDD `-6.7534`
- `news_risk_high->metal_24h` score `8.9497` n `78` status `ready` deltaP `38.4882` edge `0.5389` maxDD `-0.9745`
- `news_risk_high->index_24h` score `7.0056` n `78` status `ready` deltaP `51.8696` edge `0.2594` maxDD `-0.0453`
- `risk_on_high->commodity_24h` score `5.9801` n `52` status `ready` deltaP `34.8958` edge `0.2657` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9801` n `52` status `ready` deltaP `34.8958` edge `0.2657` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6273` n `149` status `ready` deltaP `28.1844` edge `0.2524` maxDD `-1.0419`
- `risk_on_high->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2296` n `149` status `ready` deltaP `29.1562` edge `0.013` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1355` n `52` status `ready` deltaP `27.2045` edge `0.0319` maxDD `-0.1576`
- `risk_on_and_context->commodity_4h` score `2.1355` n `52` status `ready` deltaP `27.2045` edge `0.0319` maxDD `-0.1576`
- `market_context_high->commodity_4h` score `2.0816` n `149` status `ready` deltaP `23.7068` edge `0.0581` maxDD `-0.414`
- `market_context_high->commodity_1h` score `0.868` n `149` status `ready` deltaP `13.666` edge `0.0198` maxDD `-0.4189`
- `risk_on_high->crypto_alt_4h` score `0.5741` n `52` status `ready` deltaP `10.7646` edge `0.164` maxDD `-6.3065`
- `risk_on_and_context->crypto_alt_4h` score `0.5741` n `52` status `ready` deltaP `10.7646` edge `0.164` maxDD `-6.3065`
- `news_risk_high->index_4h` score `0.3307` n `83` status `ready` deltaP `11.185` edge `0.0288` maxDD `-0.5439`
- `risk_on_high->commodity_1h` score `0.2303` n `52` status `ready` deltaP `6.7481` edge `0.0098` maxDD `-0.1809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
