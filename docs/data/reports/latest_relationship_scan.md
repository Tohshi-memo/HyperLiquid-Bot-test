# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T22:22:23.885129+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8526`

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

- `market_context_high->commodity_24h` score `1.9247` n `102` status `ready` deltaP `16.5814` edge `0.135` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.9087` n `102` status `ready` deltaP `18.188` edge `0.4639` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `1.3301` n `69` status `ready` deltaP `17.8044` edge `0.2999` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.3301` n `69` status `ready` deltaP `17.8044` edge `0.2999` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0293` n `69` status `ready` deltaP `17.3913` edge `0.0958` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0293` n `69` status `ready` deltaP `17.3913` edge `0.0958` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6544` n `102` status `ready` deltaP `7.6934` edge `0.1215` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.203` n `69` status `ready` deltaP `9.0808` edge `0.0039` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.203` n `69` status `ready` deltaP `9.0808` edge `0.0039` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2808` n `69` status `ready` deltaP `0.5744` edge `-0.0026` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.2808` n `69` status `ready` deltaP `0.5744` edge `-0.0026` maxDD `-0.3121`
- `market_context_high->crypto_alt_1h` score `-0.3667` n `102` status `ready` deltaP `1.3179` edge `0.0942` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.379` n `102` status `ready` deltaP `3.9657` edge `-0.0002` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.4191` n `69` status `ready` deltaP `2.0242` edge `0.0247` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.4191` n `69` status `ready` deltaP `2.0242` edge `0.0247` maxDD `-4.6876`
- `risk_on_high->equity_1h` score `-0.5265` n `69` status `ready` deltaP `10.3865` edge `0.0165` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.5265` n `69` status `ready` deltaP `10.3865` edge `0.0165` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.589` n `69` status `ready` deltaP `-1.1803` edge `0.0055` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.589` n `69` status `ready` deltaP `-1.1803` edge `0.0055` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.7357` n `102` status `ready` deltaP `-0.6785` edge `0.0439` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
