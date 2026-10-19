# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T00:22:28.335950+00:00`
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

- `market_context_high->commodity_24h` score `1.9185` n `94` status `ready` deltaP `16.0536` edge `0.138` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.6161` n `94` status `ready` deltaP `14.7671` edge `0.4492` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.3924` n `61` status `ready` deltaP `15.9315` edge `0.0896` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.3924` n `61` status `ready` deltaP `15.9315` edge `0.0896` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `0.7952` n `61` status `ready` deltaP `12.4825` edge `0.2668` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.7952` n `61` status `ready` deltaP `12.4825` edge `0.2668` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4054` n `94` status `ready` deltaP `4.1056` edge `0.1135` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1056` n `61` status `ready` deltaP `7.4263` edge `0.0013` maxDD `-0.6484`
- `risk_on_and_context->index_1h` score `0.1056` n `61` status `ready` deltaP `7.4263` edge `0.0013` maxDD `-0.6484`
- `risk_on_high->fx_1h` score `-0.1824` n `61` status `ready` deltaP `2.0085` edge `-0.0014` maxDD `-0.1628`
- `risk_on_and_context->fx_1h` score `-0.1824` n `61` status `ready` deltaP `2.0085` edge `-0.0014` maxDD `-0.1628`
- `market_context_high->index_1h` score `-0.4736` n `94` status `ready` deltaP `2.3513` edge `-0.0027` maxDD `-1.2285`
- `market_context_high->crypto_alt_1h` score `-0.5735` n `94` status `ready` deltaP `-0.5287` edge `0.08` maxDD `-7.3329`
- `market_context_high->fx_4h` score `-0.6556` n `94` status `ready` deltaP `-3.4778` edge `0.0022` maxDD `-0.7115`
- `risk_on_high->fx_4h` score `-0.6852` n `61` status `ready` deltaP `-4.4718` edge `0.0009` maxDD `-0.2551`
- `risk_on_and_context->fx_4h` score `-0.6852` n `61` status `ready` deltaP `-4.4718` edge `0.0009` maxDD `-0.2551`
- `market_context_high->metal_1h` score `-0.7788` n `94` status `ready` deltaP `-2.4908` edge `0.0037` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.8473` n `94` status `ready` deltaP `-2.5782` edge `-0.0013` maxDD `-0.503`
- `risk_on_high->crypto_major_1h` score `-0.9138` n `61` status `ready` deltaP `-4.2481` edge `0.0031` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.9138` n `61` status `ready` deltaP `-4.2481` edge `0.0031` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
