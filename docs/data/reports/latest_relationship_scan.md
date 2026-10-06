# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T17:52:32.730630+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1561.987` n `117` status `ready` deltaP `11.0847` edge `130.1297` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.4151` n `117` status `ready` deltaP `-0.3583` edge `2.4242` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `8.9909` n `62` status `ready` deltaP `32.4843` edge `0.553` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1172` n `62` status `ready` deltaP `18.6664` edge `0.4364` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.082` n `62` status `ready` deltaP `21.6495` edge `0.1125` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.778` n `62` status `ready` deltaP `8.1532` edge `0.1871` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.4455` n `62` status `ready` deltaP `27.7341` edge `0.0451` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.246` n `117` status `ready` deltaP `12.3437` edge `0.2013` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.912` n `62` status `ready` deltaP `7.3305` edge `0.146` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8163` n `62` status `ready` deltaP `23.2278` edge `0.0115` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.3857` n `62` status `ready` deltaP `14.5752` edge `0.0781` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1931` n `62` status `ready` deltaP `17.437` edge `0.0783` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.95` n `62` status `ready` deltaP `28.7275` edge `0.0869` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8678` n `117` status `ready` deltaP `19.1982` edge `0.02` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `0.8664` n `117` status `ready` deltaP `14.0101` edge `0.0488` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `0.7279` n `62` status `ready` deltaP `2.7091` edge `0.0945` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.6893` n `117` status `ready` deltaP `12.0938` edge `0.0052` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.544` n `117` status `ready` deltaP `10.259` edge `0.0166` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `-0.0076` n `117` status `ready` deltaP `-2.2462` edge `0.1867` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0947` n `62` status `ready` deltaP `4.5055` edge `0.0039` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
