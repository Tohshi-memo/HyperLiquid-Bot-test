# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T04:07:27.058859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9686`

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

- `risk_on_high->crypto_alt_4h` score `6.0086` n `52` status `ready` deltaP `20.6379` edge `0.4079` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.0086` n `52` status `ready` deltaP `20.6379` edge `0.4079` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3254` n `46` status `ready` deltaP `30.087` edge `0.2432` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3254` n `46` status `ready` deltaP `30.087` edge `0.2432` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.047` n `52` status `ready` deltaP `36.257` edge `0.4906` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.047` n `52` status `ready` deltaP `36.257` edge `0.4906` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `4.9014` n `104` status `ready` deltaP `15.8302` edge `0.4478` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `4.7008` n `104` status `ready` deltaP `19.9109` edge `0.4149` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.8291` n `116` status `ready` deltaP `13.2717` edge `0.1707` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.479` n `116` status `ready` deltaP `7.6812` edge `0.1526` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `0.4421` n `104` status `ready` deltaP `-4.3386` edge `0.1304` maxDD `-1.8373`
- `market_context_high->fx_1h` score `-0.2802` n `116` status `ready` deltaP `1.8691` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.4267` n `53` status `ready` deltaP `2.5901` edge `0.0194` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4267` n `53` status `ready` deltaP `2.5901` edge `0.0194` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.4982` n `104` status `ready` deltaP `7.9972` edge `0.0097` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.5346` n `116` status `ready` deltaP `5.699` edge `0.0044` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5586` n `116` status `ready` deltaP `0.7896` edge `-0.0021` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5985` n `53` status `ready` deltaP `-0.2542` edge `-0.0019` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5985` n `53` status `ready` deltaP `-0.2542` edge `-0.0019` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.6529` n `53` status `ready` deltaP `2.4715` edge `0.0024` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
