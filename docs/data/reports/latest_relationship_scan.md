# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T23:52:26.397774+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.7958` n `91` status `ready` deltaP `-3.749` edge `3.3952` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.0228` n `49` status `ready` deltaP `42.8354` edge `0.883` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6126` n `49` status `ready` deltaP `44.2416` edge `0.8462` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.5076` n `49` status `ready` deltaP `27.5386` edge `0.702` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.158` n `90` status `ready` deltaP `21.9122` edge `1.3254` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.8392` n `90` status `ready` deltaP `26.813` edge `0.5174` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.676` n `49` status `ready` deltaP `47.6603` edge `0.2386` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8749` n `49` status `ready` deltaP `32.3855` edge `0.2942` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5551` n `49` status `ready` deltaP `45.5202` edge `0.0806` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0054` n `49` status `ready` deltaP `11.5636` edge `0.2089` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.998` n `90` status `ready` deltaP `13.6145` edge `0.8874` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.5136` n `49` status `ready` deltaP `5.5909` edge `0.2039` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4278` n `49` status `ready` deltaP `29.986` edge `0.0164` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.2005` n `49` status `ready` deltaP `29.194` edge `-0.0028` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6489` n `91` status `ready` deltaP `17.554` edge `0.2274` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3025` n `90` status `ready` deltaP `22.2588` edge `0.1671` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2039` n `49` status `ready` deltaP `18.7531` edge `0.0709` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5819` n `91` status `ready` deltaP `16.6008` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4524` n `91` status `ready` deltaP `8.9426` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2421` n `91` status `ready` deltaP `9.9938` edge `0.0533` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
