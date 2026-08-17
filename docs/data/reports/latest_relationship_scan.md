# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T01:51:51.728341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `20.6441` n `74` status `ready` deltaP `-40.6297` edge `3.1859` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.2751` n `74` status `ready` deltaP `34.192` edge `0.1632` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `1.0473` n `104` status `ready` deltaP `12.1834` edge `0.0532` maxDD `-0.7718`
- `market_context_high->index_24h` score `1.0188` n `74` status `ready` deltaP `18.1681` edge `-0.0278` maxDD `-0.0069`
- `market_context_high->crypto_major_24h` score `0.3828` n `74` status `ready` deltaP `0.0` edge `0.2063` maxDD `-8.6185`
- `market_context_high->metal_4h` score `-0.1923` n `104` status `ready` deltaP `16.3345` edge `0.0158` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.375` n `109` status `ready` deltaP `5.403` edge `0.0043` maxDD `-1.7257`
- `market_context_high->commodity_1h` score `-0.5424` n `109` status `ready` deltaP `-1.4874` edge `0.0093` maxDD `-0.8998`
- `market_context_high->fx_4h` score `-0.5809` n `104` status `ready` deltaP `-1.2313` edge `-0.0058` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.7326` n `109` status `ready` deltaP `-3.211` edge `-0.0026` maxDD `-0.2968`
- `market_context_high->index_1h` score `-0.7624` n `109` status `ready` deltaP `-6.4467` edge `-0.0026` maxDD `-0.5064`
- `market_context_high->equity_24h` score `-1.1691` n `74` status `ready` deltaP `11.524` edge `-0.0603` maxDD `-6.4496`
- `market_context_high->crypto_major_4h` score `-1.4513` n `104` status `ready` deltaP `1.4188` edge `-0.0096` maxDD `-4.6638`
- `market_context_high->index_4h` score `-1.9488` n `104` status `ready` deltaP `-11.3861` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-2.1382` n `109` status `ready` deltaP `-7.1801` edge `-0.0251` maxDD `-4.7507`
- `market_context_high->crypto_major_1h` score `-2.1447` n `109` status `ready` deltaP `-7.0304` edge `-0.0308` maxDD `-4.0845`
- `market_context_high->equity_1h` score `-2.227` n `109` status `ready` deltaP `-8.9916` edge `-0.0389` maxDD `-3.606`
- `market_context_high->fx_24h` score `-2.9196` n `74` status `ready` deltaP `-26.769` edge `-0.0351` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-3.0109` n `74` status `ready` deltaP `-19.0832` edge `-0.0076` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.7172` n `104` status `ready` deltaP `-20.6028` edge `-0.1525` maxDD `-8.5929`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
