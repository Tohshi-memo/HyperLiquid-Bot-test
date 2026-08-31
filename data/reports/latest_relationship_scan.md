# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T17:52:23.334927+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->unknown_4h` score `7.9142` n `107` status `ready` deltaP `24.0313` edge `0.561` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.9142` n `107` status `ready` deltaP `24.0313` edge `0.561` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3669` n `159` status `ready` deltaP `20.7279` edge `0.4618` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `3.9865` n `77` status `ready` deltaP `22.9979` edge `0.8615` maxDD `-32.2981`
- `risk_on_and_context->crypto_alt_24h` score `3.9865` n `77` status `ready` deltaP `22.9979` edge `0.8615` maxDD `-32.2981`
- `risk_on_high->unknown_1h` score `2.5062` n `107` status `ready` deltaP `7.264` edge `0.2181` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.5062` n `107` status `ready` deltaP `7.264` edge `0.2181` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2823` n `159` status `ready` deltaP `6.6057` edge `0.2092` maxDD `-2.0436`
- `risk_on_high->fx_24h` score `1.8958` n `77` status `ready` deltaP `49.5536` edge `0.0316` maxDD `-2.1791`
- `risk_on_and_context->fx_24h` score `1.8958` n `77` status `ready` deltaP `49.5536` edge `0.0316` maxDD `-2.1791`
- `risk_on_high->commodity_24h` score `1.8424` n `77` status `ready` deltaP `12.5744` edge `0.1685` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.8424` n `77` status `ready` deltaP `12.5744` edge `0.1685` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.6005` n `61` status `ready` deltaP `4.3683` edge `0.1389` maxDD `-1.1049`
- `market_context_high->fx_24h` score `0.8598` n `120` status `ready` deltaP `31.4583` edge `0.0225` maxDD `-2.8455`
- `market_context_high->crypto_alt_24h` score `0.6745` n `120` status `ready` deltaP `10.8334` edge `0.5219` maxDD `-34.3662`
- `news_risk_high->commodity_4h` score `0.3055` n `61` status `ready` deltaP `8.2542` edge `0.0258` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1947` n `159` status `ready` deltaP `9.4801` edge `0.018` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1841` n `61` status `ready` deltaP `11.1106` edge `0.0006` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.175` n `44` status `ready` deltaP `4.7822` edge `0.0221` maxDD `-1.1904`
- `market_context_high->commodity_4h` score `0.1017` n `159` status `ready` deltaP `7.7284` edge `0.0467` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
