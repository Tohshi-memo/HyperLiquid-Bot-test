# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T22:52:25.953388+00:00`
- Price records: `672`
- Market context records: `5603`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.4915` n `174` status `ready` deltaP `15.0084` edge `0.6988` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4661` n `216` status `ready` deltaP `13.1437` edge `0.2638` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1852` n `174` status `ready` deltaP `20.9172` edge `0.0567` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7969` n `216` status `ready` deltaP `8.2487` edge `0.1755` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5083` n `216` status `ready` deltaP `6.4081` edge `0.1635` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3104` n `228` status `ready` deltaP `6.0038` edge `0.0348` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.335` n `228` status `ready` deltaP `0.5568` edge `0.0009` maxDD `-0.472`
- `market_context_high->metal_1h` score `-0.5522` n `228` status `ready` deltaP `-0.5673` edge `0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5825` n `228` status `ready` deltaP `1.2318` edge `0.0394` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5884` n `228` status `ready` deltaP `4.2468` edge `0.0472` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9021` n `228` status `ready` deltaP `0.8352` edge `0.0061` maxDD `-0.9472`
- `market_context_high->crypto_major_24h` score `-1.0707` n `174` status `ready` deltaP `10.5005` edge `0.2948` maxDD `-29.6555`
- `market_context_high->commodity_1h` score `-1.1876` n `228` status `ready` deltaP `-2.3427` edge `-0.0068` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5997` n `216` status `ready` deltaP `2.2075` edge `0.0129` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.6435` n `216` status `ready` deltaP `1.5922` edge `0.0077` maxDD `-1.0886`
- `market_context_high->index_24h` score `-2.3526` n `174` status `ready` deltaP `10.4346` edge `0.0275` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9218` n `216` status `ready` deltaP `-12.0653` edge `-0.0558` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2102` n `216` status `ready` deltaP `-5.9394` edge `-0.0437` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1452` n `174` status `ready` deltaP `-9.369` edge `-0.2457` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.1228` n `174` status `ready` deltaP `0.2874` edge `-0.0591` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
