# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T23:37:22.331826+00:00`
- Price records: `672`
- Market context records: `1679`
- Flow alert records: `6741`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.663` n `155` status `ready` deltaP `27.4372` edge `0.7816` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1814` n `195` status `ready` deltaP `22.8901` edge `0.5456` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8806` n `155` status `ready` deltaP `18.9273` edge `0.335` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.3306` n `195` status `ready` deltaP `18.9955` edge `0.4218` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.6853` n `195` status `ready` deltaP `14.6443` edge `0.2356` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.892` n `155` status `ready` deltaP `18.0768` edge `0.527` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.1702` n `155` status `ready` deltaP `13.7192` edge `0.5381` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5912` n `204` status `ready` deltaP `6.0203` edge `0.1115` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4808` n `155` status `ready` deltaP `25.3321` edge `1.0521` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.087` n `195` status `ready` deltaP `5.677` edge `0.0783` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.0704` n `155` status `ready` deltaP `24.1969` edge `0.7063` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.133` n `204` status `ready` deltaP `3.3404` edge `0.0475` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.3934` n `204` status `ready` deltaP `3.2553` edge `0.0729` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.5611` n `155` status `ready` deltaP `6.1424` edge `0.0172` maxDD `-1.3925`
- `market_context_high->metal_1h` score `-0.5759` n `204` status `ready` deltaP `6.7277` edge `0.0149` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6561` n `195` status `ready` deltaP `12.6469` edge `0.1302` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6597` n `204` status `ready` deltaP `-0.6898` edge `0.0128` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.857` n `204` status `ready` deltaP `-0.8835` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.2462` n `195` status `ready` deltaP `-8.3224` edge `-0.0114` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1561` n `204` status `ready` deltaP `0.1233` edge `-0.0318` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
