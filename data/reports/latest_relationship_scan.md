# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T01:22:27.738290+00:00`
- Price records: `672`
- Market context records: `6559`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.3354` n `144` status `ready` deltaP `11.5468` edge `0.781` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8143` n `210` status `ready` deltaP `-4.6806` edge `0.2725` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3791` n `144` status `ready` deltaP `13.4773` edge `0.2119` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.0529` n `199` status `ready` deltaP `11.0131` edge `0.0228` maxDD `-1.4885`
- `market_context_high->crypto_alt_4h` score `-0.2803` n `199` status `ready` deltaP `8.1391` edge `0.0981` maxDD `-9.3971`
- `market_context_high->fx_1h` score `-0.3386` n `210` status `ready` deltaP `1.1577` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.447` n `210` status `ready` deltaP `6.8976` edge `0.0233` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4947` n `210` status `ready` deltaP `6.6396` edge `0.0236` maxDD `-5.8368`
- `market_context_high->crypto_major_4h` score `-0.5653` n `199` status `ready` deltaP `10.8661` edge `0.0883` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.5721` n `210` status `ready` deltaP `-0.1098` edge `-0.0043` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6083` n `210` status `ready` deltaP `-1.2789` edge `0.0025` maxDD `-0.7564`
- `market_context_high->equity_4h` score `-0.8331` n `199` status `ready` deltaP `9.0084` edge `0.0404` maxDD `-8.2573`
- `market_context_high->unknown_4h` score `-1.0541` n `199` status `ready` deltaP `-16.6312` edge `0.2636` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.2041` n `210` status `ready` deltaP `1.9319` edge `-0.0022` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2284` n `210` status `ready` deltaP `-3.128` edge `-0.0008` maxDD `-2.1239`
- `market_context_high->metal_4h` score `-1.3796` n `199` status `ready` deltaP `0.6572` edge `0.033` maxDD `-3.1405`
- `market_context_high->commodity_4h` score `-1.3821` n `199` status `ready` deltaP `-2.1931` edge `-0.0131` maxDD `-5.6246`
- `market_context_high->metal_24h` score `-1.9733` n `144` status `ready` deltaP `5.966` edge `0.0888` maxDD `-5.7746`
- `market_context_high->fx_4h` score `-2.9447` n `199` status `ready` deltaP `-2.4873` edge `-0.0076` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.831` n `144` status `ready` deltaP `-4.6144` edge `-0.0069` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
