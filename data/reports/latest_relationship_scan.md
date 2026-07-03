# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T16:52:26.826281+00:00`
- Price records: `672`
- Market context records: `5576`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11397`

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

- `market_context_high->equity_24h` score `4.2811` n `174` status `ready` deltaP `15.0084` edge `0.7646` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2324` n `192` status `ready` deltaP `11.2424` edge `0.257` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.8576` n `174` status `ready` deltaP `13.7991` edge `0.4335` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.8348` n `174` status `ready` deltaP `17.2713` edge `0.0518` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.639` n `192` status `ready` deltaP `6.6946` edge `0.1727` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.6038` n `192` status `ready` deltaP `5.4878` edge `0.1776` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.2147` n `204` status `ready` deltaP `3.4872` edge `0.0082` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2707` n `204` status `ready` deltaP `5.7356` edge `0.0399` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.3057` n `192` status `ready` deltaP `5.7927` edge `0.0093` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.4648` n `204` status `ready` deltaP `1.0626` edge `0.001` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5288` n `204` status `ready` deltaP `-0.1908` edge `0.001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6425` n `204` status `ready` deltaP `0.5871` edge `0.0387` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7971` n `204` status `ready` deltaP `2.178` edge `0.0436` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2373` n `204` status `ready` deltaP `-2.7093` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5234` n `192` status `ready` deltaP `2.5915` edge `0.0167` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0147` n `174` status `ready` deltaP `13.2124` edge `0.0523` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0878` n `192` status `ready` deltaP `-14.342` edge `-0.0619` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.423` n `192` status `ready` deltaP `-7.19` edge `-0.0531` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8814` n `174` status `ready` deltaP `-7.8065` edge `-0.2223` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.159` n `174` status `ready` deltaP `3.7596` edge `0.0814` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
