# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T03:07:28.828747+00:00`
- Price records: `672`
- Market context records: `5839`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `news_risk_high->fx_1h` score `1.9016` n `30` status `ready` deltaP `23.0339` edge `0.0188` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8254` n `30` status `ready` deltaP `11.2375` edge `0.0776` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6819` n `265` status `ready` deltaP `7.7111` edge `0.1512` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1827` n `30` status `ready` deltaP `4.5709` edge `0.0391` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3278` n `265` status `ready` deltaP `1.0214` edge `-0.0003` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3822` n `265` status `ready` deltaP `4.4018` edge `0.0395` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4219` n `30` status `ready` deltaP `1.3872` edge `-0.0267` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5352` n `265` status `ready` deltaP `-0.9683` edge `-0.0019` maxDD `-2.1545`
- `market_context_high->index_1h` score `-0.5456` n `265` status `ready` deltaP `1.3394` edge `0.0059` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.5862` n `237` status `ready` deltaP `16.0118` edge `0.3523` maxDD `-31.6316`
- `market_context_high->metal_1h` score `-0.6016` n `265` status `ready` deltaP `2.3935` edge `0.001` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-0.9987` n `265` status `ready` deltaP `2.6212` edge `0.0314` maxDD `-6.2348`
- `market_context_high->index_4h` score `-1.1729` n `265` status `ready` deltaP `0.5787` edge `0.0145` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.1836` n `265` status `ready` deltaP `1.1117` edge `0.0274` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2261` n `30` status `ready` deltaP `-12.2455` edge `-0.0241` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.6652` n `265` status `ready` deltaP `-2.5477` edge `-0.0016` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.675` n `237` status `ready` deltaP `7.0279` edge `0.0202` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1759` n `265` status `ready` deltaP `-5.0092` edge `-0.0438` maxDD `-8.8078`
- `market_context_high->commodity_4h` score `-2.5316` n `265` status `ready` deltaP `-0.7588` edge `-0.0145` maxDD `-7.9795`
- `market_context_high->index_24h` score `-2.9055` n `237` status `ready` deltaP `2.9206` edge `0.0225` maxDD `-18.1572`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
