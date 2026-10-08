# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T04:52:26.185316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.8344` n `90` status `ready` deltaP `-3.2876` edge `3.312` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.0515` n `62` status `ready` deltaP `38.9675` edge `0.6815` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1937` n `62` status `ready` deltaP `23.1723` edge `0.5794` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.6039` n `62` status `ready` deltaP `16.6918` edge `0.449` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.9649` n `62` status `ready` deltaP `36.0967` edge `0.1731` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.5397` n `90` status `ready` deltaP `11.1744` edge `0.8049` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0956` n `62` status `ready` deltaP `33.6108` edge `0.0601` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5467` n `90` status `ready` deltaP `17.032` edge `0.1951` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.5151` n `62` status `ready` deltaP `10.3245` edge `0.1763` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4583` n `62` status `ready` deltaP `18.7878` edge `0.1394` maxDD `-2.7837`
- `market_context_high->equity_24h` score `2.0993` n `90` status `ready` deltaP `14.2545` edge `0.1228` maxDD `-1.0977`
- `news_risk_high->index_1h` score `2.0128` n `62` status `ready` deltaP `25.1739` edge `0.0149` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.614` n `62` status `ready` deltaP `-6.2626` edge `0.3008` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4463` n `62` status `ready` deltaP `21.0144` edge `0.0869` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2385` n `90` status `ready` deltaP `21.5371` edge `0.1637` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.197` n `62` status `ready` deltaP `3.4576` edge `0.1286` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0391` n `90` status `ready` deltaP `21.4307` edge `0.0184` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6987` n `90` status `ready` deltaP `11.7964` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.1909` n `90` status `ready` deltaP `7.5418` edge `0.568` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.1698` n `90` status `ready` deltaP `10.2528` edge `0.0423` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
