# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T03:52:25.403881+00:00`
- Price records: `672`
- Market context records: `3245`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `risk_on_high->crypto_major_4h` score `16.7214` n `31` status `ready` deltaP `30.8517` edge `1.3` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.7214` n `31` status `ready` deltaP `30.8517` edge `1.3` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.072` n `103` status `ready` deltaP `17.7825` edge `2.6697` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.5222` n `103` status `ready` deltaP `48.3415` edge `0.8474` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.4508` n `103` status `ready` deltaP `31.1421` edge `0.8354` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.3819` n `103` status `ready` deltaP `18.5275` edge `1.5363` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.1905` n `31` status `ready` deltaP `12.1312` edge `0.769` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1905` n `31` status `ready` deltaP `12.1312` edge `0.769` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2312` n `31` status `ready` deltaP `18.9614` edge `0.5295` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2312` n `31` status `ready` deltaP `18.9614` edge `0.5295` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.5759` n `31` status `ready` deltaP `10.3776` edge `0.368` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5759` n `31` status `ready` deltaP `10.3776` edge `0.368` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.1627` n `103` status `ready` deltaP `21.8531` edge `2.2015` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.9867` n `143` status `ready` deltaP `18.0113` edge `0.1413` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.5992` n `31` status `ready` deltaP `5.9058` edge `0.2244` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5992` n `31` status `ready` deltaP `5.9058` edge `0.2244` maxDD `-1.7001`
- `risk_on_high->crypto_alt_1h` score `0.6958` n `31` status `ready` deltaP `3.559` edge `0.2092` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6958` n `31` status `ready` deltaP `3.559` edge `0.2092` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4732` n `31` status `ready` deltaP `8.0645` edge `0.0754` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4732` n `31` status `ready` deltaP `8.0645` edge `0.0754` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
