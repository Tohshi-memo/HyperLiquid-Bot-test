# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T01:52:35.182605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.4289` n `158` status `ready` deltaP `15.925` edge `0.0802` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8779` n `170` status `ready` deltaP `11.423` edge `0.0313` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4436` n `137` status `ready` deltaP `18.4395` edge `0.0206` maxDD `-1.9329`
- `market_context_high->fx_1h` score `-0.2041` n `170` status `ready` deltaP `3.658` edge `-0.001` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3181` n `158` status `ready` deltaP `4.9109` edge `0.0018` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.5708` n `170` status `ready` deltaP `-3.0257` edge `-0.0053` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.5727` n `137` status `ready` deltaP `2.2975` edge `0.0901` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.8254` n `170` status `ready` deltaP `-2.1151` edge `-0.0047` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.852` n `170` status `ready` deltaP `-5.0898` edge `-0.0117` maxDD `-2.0884`
- `market_context_high->index_4h` score `-0.9093` n `158` status `ready` deltaP `-4.0696` edge `-0.0112` maxDD `-1.26`
- `market_context_high->metal_24h` score `-0.9283` n `137` status `ready` deltaP `-2.7689` edge `0.0362` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-1.0042` n `137` status `ready` deltaP `-0.2991` edge `0.2243` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.541` n `170` status `ready` deltaP `-8.6615` edge `-0.0377` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.5995` n `158` status `ready` deltaP `-6.0647` edge `-0.0328` maxDD `-5.2136`
- `market_context_high->equity_4h` score `-2.2078` n `158` status `ready` deltaP `-5.5843` edge `-0.0871` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.3711` n `170` status `ready` deltaP `-10.4702` edge `-0.0608` maxDD `-10.5372`
- `market_context_high->crypto_alt_24h` score `-4.4045` n `137` status `ready` deltaP `-11.3152` edge `-0.1473` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.6541` n `137` status `ready` deltaP `-1.143` edge `-0.1308` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-5.73` n `158` status `ready` deltaP `-12.0524` edge `-0.1554` maxDD `-12.6737`
- `market_context_high->unknown_1h` score `-7.5993` n `170` status `ready` deltaP `-5.0053` edge `-0.5542` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
