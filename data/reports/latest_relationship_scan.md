# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T05:07:25.361731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.223` n `73` status `ready` deltaP `30.8029` edge `0.1229` maxDD `-1.1071`
- `market_context_high->crypto_major_24h` score `1.7903` n `73` status `ready` deltaP `3.9075` edge `0.2608` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4673` n `73` status `ready` deltaP `21.7014` edge `-0.0224` maxDD `0.0`
- `market_context_high->equity_24h` score `1.4421` n `73` status `ready` deltaP `15.9127` edge `0.035` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.3234` n `32` status `ready` deltaP `14.4274` edge `0.0447` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.3234` n `32` status `ready` deltaP `14.4274` edge `0.0447` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.7646` n `32` status `ready` deltaP `12.1445` edge `0.0371` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7646` n `32` status `ready` deltaP `12.1445` edge `0.0371` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.7103` n `104` status `ready` deltaP `12.5352` edge `0.0562` maxDD `-0.8962`
- `risk_on_high->index_1h` score `0.4242` n `32` status `ready` deltaP `11.8638` edge `0.0128` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.4242` n `32` status `ready` deltaP `11.8638` edge `0.0128` maxDD `-0.3343`
- `risk_on_high->commodity_1h` score `0.1626` n `32` status `ready` deltaP `4.1542` edge `0.0182` maxDD `-0.3372`
- `risk_on_and_context->commodity_1h` score `0.1626` n `32` status `ready` deltaP `4.1542` edge `0.0182` maxDD `-0.3372`
- `risk_on_high->fx_1h` score `-0.0267` n `32` status `ready` deltaP `2.6759` edge `0.0015` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `-0.0267` n `32` status `ready` deltaP `2.6759` edge `0.0015` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1765` n `104` status `ready` deltaP `16.4869` edge `0.0161` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.368` n `116` status `ready` deltaP `-1.3112` edge `-0.0014` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.3685` n `116` status `ready` deltaP `-1.2337` edge `0.0079` maxDD `-1.087`
- `risk_on_high->crypto_alt_1h` score `-0.4331` n `32` status `ready` deltaP `-1.0479` edge `0.0306` maxDD `-1.7766`
- `risk_on_and_context->crypto_alt_1h` score `-0.4331` n `32` status `ready` deltaP `-1.0479` edge `0.0306` maxDD `-1.7766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
