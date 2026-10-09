# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T06:01:10.066924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8870`

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

- `market_context_high->unknown_4h` score `40.8174` n `91` status `ready` deltaP `-3.4441` edge `3.4783` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `11.974` n `31` status `ready` deltaP `43.4451` edge `0.7082` maxDD `0.0`
- `news_risk_high->equity_24h` score `10.2627` n `31` status `ready` deltaP `27.0274` edge `0.685` maxDD `-0.1298`
- `news_risk_high->crypto_major_4h` score `10.103` n `31` status `ready` deltaP `42.1764` edge `0.5675` maxDD `-0.2073`
- `market_context_high->crypto_major_24h` score `9.9902` n `90` status `ready` deltaP `22.3611` edge `1.4291` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.5827` n `90` status `ready` deltaP `31.0417` edge `0.6345` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7808` n `31` status `ready` deltaP `51.9097` edge `0.219` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.2586` n `31` status `ready` deltaP `30.5665` edge `0.3383` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6641` n `31` status `ready` deltaP `44.1827` edge `0.0986` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.6109` n `90` status `ready` deltaP `14.0625` edge `0.963` maxDD `-34.5048`
- `news_risk_high->commodity_24h` score `2.7115` n `31` status `ready` deltaP `26.8817` edge `0.0552` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.3711` n `31` status `ready` deltaP `28.3997` edge `0.0172` maxDD `-0.0484`
- `news_risk_high->crypto_major_1h` score `2.155` n `31` status `ready` deltaP `7.5478` edge `0.1648` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `1.8527` n `91` status `ready` deltaP `17.8588` edge `0.2515` maxDD `-6.9761`
- `news_risk_high->crypto_alt_1h` score `1.5743` n `31` status `ready` deltaP `-1.8302` edge `0.1751` maxDD `-1.2034`
- `market_context_high->metal_24h` score `0.9906` n `90` status `ready` deltaP `18.1944` edge `0.1542` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.3506` n `91` status `ready` deltaP `7.745` edge `0.0018` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2764` n `91` status `ready` deltaP `13.2472` edge `0.0094` maxDD `-0.3077`
- `market_context_high->crypto_major_1h` score `0.2748` n `91` status `ready` deltaP `9.9938` edge `0.0575` maxDD `-3.7778`
- `news_risk_high->metal_4h` score `0.0008` n `31` status `ready` deltaP `5.5763` edge `0.0045` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
