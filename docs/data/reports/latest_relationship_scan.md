# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T21:22:27.403407+00:00`
- Price records: `672`
- Market context records: `7182`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->crypto_major_4h` score `6.3986` n `30` status `ready` deltaP `26.8394` edge `0.3926` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.3986` n `30` status `ready` deltaP `26.8394` edge `0.3926` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.8194` n `30` status `ready` deltaP `17.7744` edge `0.3224` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.8194` n `30` status `ready` deltaP `17.7744` edge `0.3224` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0388` n `34` status `ready` deltaP `22.1293` edge `0.0374` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0388` n `34` status `ready` deltaP `22.1293` edge `0.0374` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.6404` n `30` status `ready` deltaP `11.4329` edge `0.1448` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.6404` n `30` status `ready` deltaP `11.4329` edge `0.1448` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.4406` n `34` status `ready` deltaP `9.1229` edge `0.0247` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4406` n `34` status `ready` deltaP `9.1229` edge `0.0247` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.4161` n `34` status `ready` deltaP `4.5438` edge `0.0344` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.4161` n `34` status `ready` deltaP `4.5438` edge `0.0344` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.3359` n `177` status `ready` deltaP `2.9915` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.4904` n `177` status `ready` deltaP `5.6666` edge `0.0404` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5402` n `177` status `ready` deltaP `0.9489` edge `0.0283` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.5903` n `177` status `ready` deltaP `-0.104` edge `-0.0129` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.7506` n `177` status `ready` deltaP `-1.8083` edge `0.0137` maxDD `-1.4688`
- `risk_on_high->metal_4h` score `-0.8153` n `30` status `ready` deltaP `-11.1179` edge `0.0344` maxDD `-0.5181`
- `risk_on_and_context->metal_4h` score `-0.8153` n `30` status `ready` deltaP `-11.1179` edge `0.0344` maxDD `-0.5181`
- `market_context_high->index_1h` score `-0.8624` n `177` status `ready` deltaP `-0.2098` edge `-0.004` maxDD `-2.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
