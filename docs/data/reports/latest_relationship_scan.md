# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T20:22:27.518147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4561.6795` n `66` status `ready` deltaP `24.3213` edge `380.0199` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.3341` n `40` status `ready` deltaP `54.9306` edge `1.0347` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0742` n `40` status `ready` deltaP `51.3194` edge `0.5935` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.5648` n `66` status `ready` deltaP `16.8098` edge `0.3447` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5971` n `66` status `ready` deltaP `15.7428` edge `0.0662` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0801` n `40` status `ready` deltaP `14.0549` edge `0.1294` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7178` n `40` status `ready` deltaP `8.3537` edge `0.1269` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.67` n `40` status `ready` deltaP `12.3952` edge `0.0407` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.6511` n `40` status `ready` deltaP `20.4573` edge `0.0267` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6166` n `66` status `ready` deltaP `9.4448` edge `0.0707` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.452` n `40` status `ready` deltaP `13.997` edge `0.0024` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.3255` n `66` status `ready` deltaP `14.4725` edge `0.0264` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.1576` n `66` status `ready` deltaP `7.2764` edge `0.0399` maxDD `-3.1233`
- `news_risk_high->metal_4h` score `0.0886` n `66` status `ready` deltaP `5.2892` edge `0.0237` maxDD `-0.8085`
- `news_risk_high->index_1h` score `-0.0122` n `66` status `ready` deltaP `3.5157` edge `0.0073` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0568` n `66` status `ready` deltaP `3.0122` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1326` n `66` status `ready` deltaP `2.5994` edge `0.006` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1601` n `66` status `ready` deltaP `3.3297` edge `0.0293` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4635` n `40` status `ready` deltaP `-0.2994` edge `0.0053` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6983` n `66` status `ready` deltaP `2.3952` edge `-0.0275` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
