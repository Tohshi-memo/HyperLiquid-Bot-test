# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T01:07:26.115652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10176`

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

- `risk_on_high->crypto_alt_24h` score `6.9842` n `117` status `ready` deltaP `16.5598` edge `0.4946` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.9842` n `117` status `ready` deltaP `16.5598` edge `0.4946` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.7438` n `117` status `ready` deltaP `31.3972` edge `0.3065` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7438` n `117` status `ready` deltaP `31.3972` edge `0.3065` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.0968` n `117` status `ready` deltaP `23.6945` edge `0.2693` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.0968` n `117` status `ready` deltaP `23.6945` edge `0.2693` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0326` n `117` status `ready` deltaP `16.9338` edge `0.8109` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0326` n `117` status `ready` deltaP `16.9338` edge `0.8109` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `1.9368` n `241` status `ready` deltaP `9.215` edge `0.1827` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.2789` n `117` status `ready` deltaP `14.9706` edge `0.011` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.2789` n `117` status `ready` deltaP `14.9706` edge `0.011` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.8279` n `117` status `ready` deltaP `3.3485` edge `0.0819` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8279` n `117` status `ready` deltaP `3.3485` edge `0.0819` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.5574` n `241` status `ready` deltaP `10.0658` edge `0.0187` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1742` n `117` status `ready` deltaP `8.3321` edge `-0.0002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1742` n `117` status `ready` deltaP `8.3321` edge `-0.0002` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.1584` n `117` status `ready` deltaP `12.4265` edge `-0.0165` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1584` n `117` status `ready` deltaP `12.4265` edge `-0.0165` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.146` n `117` status `ready` deltaP `8.9693` edge `-0.0047` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.146` n `117` status `ready` deltaP `8.9693` edge `-0.0047` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
