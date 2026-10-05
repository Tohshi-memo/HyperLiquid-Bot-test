# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T12:37:30.616790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8432`

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

- `market_context_high->crypto_major_24h` score `10.9952` n `81` status `ready` deltaP `29.8032` edge `0.7312` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3683` n `65` status `ready` deltaP `32.5516` edge `0.584` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1662` n `81` status `ready` deltaP `25.3666` edge `0.4067` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7682` n `65` status `ready` deltaP `19.6341` edge `0.4842` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.4053` n `112` status `ready` deltaP `15.2439` edge `0.2619` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.0444` n `65` status `ready` deltaP `9.992` edge `0.1971` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.928` n `65` status `ready` deltaP `32.371` edge `0.0544` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5277` n `65` status `ready` deltaP `9.8664` edge `0.1804` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4584` n `65` status `ready` deltaP `20.5769` edge `0.1287` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0746` n `65` status `ready` deltaP `25.6172` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.766` n `65` status `ready` deltaP `16.7918` edge `0.0768` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6317` n `112` status `ready` deltaP `27.5915` edge `0.0277` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2081` n `65` status `ready` deltaP `3.6711` edge `0.1281` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.1826` n `112` status `ready` deltaP `15.9625` edge `0.0592` maxDD `-1.3656`
- `market_context_high->equity_24h` score `1.1375` n `81` status `ready` deltaP `13.6767` edge `0.0097` maxDD `-0.1536`
- `market_context_high->crypto_alt_4h` score `0.9806` n `112` status `ready` deltaP `3.027` edge `0.2339` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.9349` n `81` status `ready` deltaP `27.3534` edge `0.0766` maxDD `-5.7943`
- `market_context_high->fx_1h` score `0.8982` n `121` status `ready` deltaP `14.6001` edge `0.0059` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.4606` n `65` status `ready` deltaP `24.9119` edge `0.0961` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
