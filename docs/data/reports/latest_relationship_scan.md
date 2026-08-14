# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T14:07:27.754135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `106.6828` n `141` status `ready` deltaP `-33.3334` edge `9.4037` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9095` n `32` status `ready` deltaP `-44.7917` edge `4.5928` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9095` n `32` status `ready` deltaP `-44.7917` edge `4.5928` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5144` n `36` status `ready` deltaP `9.7222` edge `0.766` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.0982` n `36` status `ready` deltaP `37.6524` edge `0.3405` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8438` n `32` status `ready` deltaP `32.8125` edge `0.1849` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8438` n `32` status `ready` deltaP `32.8125` edge `0.1849` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.0324` n `141` status `ready` deltaP `22.1742` edge `0.1852` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.9382` n `32` status `ready` deltaP `20.503` edge `0.1264` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9382` n `32` status `ready` deltaP `20.503` edge `0.1264` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0404` n `36` status `ready` deltaP `13.7153` edge `0.0786` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.9573` n `32` status `ready` deltaP `16.1458` edge `0.2589` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9573` n `32` status `ready` deltaP `16.1458` edge `0.2589` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6385` n `36` status `ready` deltaP `19.3089` edge `0.021` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.623` n `36` status `ready` deltaP `8.2835` edge `0.1119` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2971` n `32` status `ready` deltaP `13.6602` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2971` n `32` status `ready` deltaP `13.6602` edge `0.0403` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.2601` n `141` status `ready` deltaP `15.4276` edge `0.066` maxDD `-2.1077`
- `risk_on_high->fx_24h` score `1.2485` n `32` status `ready` deltaP `14.7569` edge `0.0241` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2485` n `32` status `ready` deltaP `14.7569` edge `0.0241` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
