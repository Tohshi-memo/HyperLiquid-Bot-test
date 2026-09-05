# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T09:22:26.009240+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10935`

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

- `risk_on_high->unknown_4h` score `21.4139` n `142` status `ready` deltaP `8.5988` edge `1.789` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.4139` n `142` status `ready` deltaP `8.5988` edge `1.789` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.5948` n `228` status `ready` deltaP `8.673` edge `0.8981` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3451` n `37` status `ready` deltaP `25.1783` edge `0.4712` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.2092` n `37` status `ready` deltaP `23.7847` edge `0.1922` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.645` n `37` status `ready` deltaP `17.1803` edge `0.2305` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.114` n `37` status `ready` deltaP `21.1025` edge `0.0576` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.958` n `37` status `ready` deltaP `12.0386` edge `0.103` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6518` n `37` status `ready` deltaP `13.8332` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2083` n `37` status `ready` deltaP `14.4158` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.2062` n `37` status `ready` deltaP `6.4655` edge `0.0757` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2006` n `37` status `ready` deltaP `15.0227` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `0.8878` n `37` status `ready` deltaP `8.5775` edge `0.0433` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.5819` n `37` status `ready` deltaP `14.4942` edge `0.2556` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.5411` n `37` status `ready` deltaP `6.3983` edge `0.0353` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.3047` n `37` status `ready` deltaP `13.0114` edge `0.0402` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.105` n `151` status `ready` deltaP `12.4648` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.105` n `151` status `ready` deltaP `12.4648` edge `0.0016` maxDD `-1.699`
- `risk_on_high->crypto_major_24h` score `0.0198` n `133` status `ready` deltaP `21.952` edge `0.7297` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.0198` n `133` status `ready` deltaP `21.952` edge `0.7297` maxDD `-56.9519`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
