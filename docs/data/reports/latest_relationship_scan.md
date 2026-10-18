# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T23:07:33.951234+00:00`
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

- `market_context_high->commodity_24h` score `1.967` n `99` status `ready` deltaP `16.4199` edge `0.1396` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.7931` n `99` status `ready` deltaP `16.97` edge `0.4572` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.5895` n `66` status `ready` deltaP `16.9249` edge `0.0994` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.5895` n `66` status `ready` deltaP `16.9249` edge `0.0994` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.1117` n `66` status `ready` deltaP `15.9599` edge `0.2842` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.1117` n `66` status `ready` deltaP `15.9599` edge `0.2842` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5497` n `99` status `ready` deltaP `6.416` edge `0.1166` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0799` n `66` status `ready` deltaP `7.0571` edge `0.0016` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0799` n `66` status `ready` deltaP `7.0571` edge `0.0016` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.395` n `66` status `ready` deltaP `-1.5152` edge `-0.0033` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.395` n `66` status `ready` deltaP `-1.5152` edge `-0.0033` maxDD `-0.3121`
- `market_context_high->index_1h` score `-0.4686` n `99` status `ready` deltaP `2.5116` edge `-0.002` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.5491` n `99` status `ready` deltaP `-0.3161` edge `0.0817` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.6086` n `66` status `ready` deltaP `-0.1497` edge `0.0149` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6086` n `66` status `ready` deltaP `-0.1497` edge `0.0149` maxDD `-4.6876`
- `market_context_high->fx_1h` score `-0.6624` n `99` status `ready` deltaP `-4.5455` edge `-0.0025` maxDD `-0.503`
- `market_context_high->fx_4h` score `-0.7704` n `99` status `ready` deltaP `-5.222` edge `-0.0009` maxDD `-0.7115`
- `risk_on_high->equity_1h` score `-0.8406` n `66` status `ready` deltaP `8.0808` edge `0.0057` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.8406` n `66` status `ready` deltaP `8.0808` edge `0.0057` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.8667` n `99` status `ready` deltaP `-2.4314` edge `0.0388` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
