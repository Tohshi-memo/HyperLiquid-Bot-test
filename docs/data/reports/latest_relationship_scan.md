# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T06:52:27.859707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6337`

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

- `market_context_high->unknown_24h` score `7033.2985` n `55` status `ready` deltaP `4.8611` edge `586.0758` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.2139` n `55` status `ready` deltaP `5.3464` edge `30.9865` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `78.1996` n `108` status `ready` deltaP `-5.1951` edge `6.5799` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `48.9077` n `55` status `ready` deltaP `2.4143` edge `4.0706` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.8016` n `55` status `ready` deltaP `46.6193` edge `1.5296` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2069` n `98` status `ready` deltaP `30.8532` edge `1.0305` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.3245` n `55` status `ready` deltaP `60.4167` edge `0.2076` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.768` n `55` status `ready` deltaP `46.4836` edge `0.2852` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.8331` n `55` status `ready` deltaP `23.5976` edge `0.3582` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4959` n `55` status `ready` deltaP `30.5876` edge `0.2877` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.9181` n `108` status `ready` deltaP `18.5976` edge `0.4245` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.4023` n `55` status `ready` deltaP `31.8293` edge `0.0964` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3904` n `55` status `ready` deltaP `6.2001` edge `0.3114` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.6522` n `55` status `ready` deltaP `12.0739` edge `0.3272` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `2.009` n `55` status `ready` deltaP `-3.952` edge `0.4357` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5644` n `55` status `ready` deltaP `18.5033` edge `0.0495` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4291` n `55` status `ready` deltaP `1.9788` edge `0.1584` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3904` n `55` status `ready` deltaP `8.0321` edge `0.1233` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3523` n `55` status `ready` deltaP `3.9249` edge `0.1536` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
