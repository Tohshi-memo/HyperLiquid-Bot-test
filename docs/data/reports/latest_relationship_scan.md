# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T00:22:34.591749+00:00`
- Price records: `672`
- Market context records: `5610`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.3007` n `174` status `ready` deltaP `15.0084` edge `0.6829` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4858` n `222` status `ready` deltaP `13.9296` edge `0.2602` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2703` n `174` status `ready` deltaP `21.7852` edge `0.058` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8487` n `222` status `ready` deltaP `8.9266` edge `0.1753` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4438` n `222` status `ready` deltaP `6.2171` edge `0.1594` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3452` n `234` status `ready` deltaP `0.3839` edge `0.0008` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3659` n `234` status `ready` deltaP `5.5505` edge `0.0332` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5216` n `234` status `ready` deltaP `0.0217` edge `0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6164` n `234` status `ready` deltaP `1.1081` edge `0.0374` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6319` n `234` status `ready` deltaP `4.1238` edge `0.0444` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8961` n `234` status `ready` deltaP `0.9392` edge `0.0059` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1651` n `234` status `ready` deltaP `-2.1368` edge `-0.0063` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3175` n `222` status `ready` deltaP `0.8529` edge `0.0071` maxDD `-1.2021`
- `market_context_high->index_4h` score `-1.6596` n `222` status `ready` deltaP `1.6082` edge `0.0119` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-1.7` n `174` status `ready` deltaP `9.4588` edge `0.2493` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3878` n `174` status `ready` deltaP `10.0874` edge `0.0253` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8204` n `222` status `ready` deltaP `-10.326` edge `-0.0544` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.196` n `222` status `ready` deltaP `-5.9122` edge `-0.0427` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2454` n `174` status `ready` deltaP `-10.4107` edge `-0.2516` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.6933` n `174` status `ready` deltaP `-0.7543` edge `-0.0997` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
