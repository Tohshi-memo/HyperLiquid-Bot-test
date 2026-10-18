# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T14:52:29.993271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.1558` n `131` status `ready` deltaP `19.38` edge `0.1356` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.8706` n `90` status `ready` deltaP `20.6183` edge `0.0982` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8706` n `90` status `ready` deltaP `20.6183` edge `0.0982` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.9683` n `132` status `ready` deltaP `15.7936` edge `0.3593` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.8174` n `132` status `ready` deltaP `5.7612` edge `0.1186` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.5478` n `91` status `ready` deltaP `15.2858` edge `0.2164` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.5478` n `91` status `ready` deltaP `15.2858` edge `0.2164` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.0608` n `91` status `ready` deltaP `5.6067` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0608` n `91` status `ready` deltaP `5.6067` edge `0.0061` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1369` n `132` status `ready` deltaP `3.8922` edge `0.1065` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.3419` n `91` status `ready` deltaP `10.3093` edge `0.0324` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3419` n `91` status `ready` deltaP `10.3093` edge `0.0324` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.3747` n `132` status `ready` deltaP `4.5001` edge `0.0089` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4822` n `132` status `ready` deltaP `4.641` edge `0.0037` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4844` n `91` status `ready` deltaP `0.9952` edge `0.0044` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4844` n `91` status `ready` deltaP `0.9952` edge `0.0044` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.6964` n `91` status `ready` deltaP `-0.8489` edge `0.0083` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6964` n `91` status `ready` deltaP `-0.8489` edge `0.0083` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
