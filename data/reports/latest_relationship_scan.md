# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T08:22:37.219323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `691.8097` n `105` status `ready` deltaP `9.4246` edge `57.626` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `33.3866` n `105` status `ready` deltaP `-2.3548` edge `2.8518` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.896` n `62` status `ready` deltaP `34.6184` edge `0.6142` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.6155` n `62` status `ready` deltaP `22.0201` edge `0.5389` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4302` n `62` status `ready` deltaP `24.6528` edge `0.1215` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.4218` n `105` status `ready` deltaP `16.0162` edge `0.2748` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.3945` n `62` status `ready` deltaP `5.354` edge `0.1738` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.038` n `62` status `ready` deltaP `7.4802` edge `0.1555` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9924` n `62` status `ready` deltaP `25.1739` edge `0.0132` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8902` n `62` status `ready` deltaP `17.7764` edge `0.0988` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4123` n `62` status `ready` deltaP `20.1809` edge `0.0881` maxDD `-0.993`
- `market_context_high->crypto_alt_4h` score `1.1539` n `105` status `ready` deltaP `-0.8217` edge `0.274` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.9561` n `105` status `ready` deltaP `7.1181` edge `0.3725` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.9369` n `105` status `ready` deltaP `14.5038` edge `0.0056` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.8948` n `62` status `ready` deltaP `2.1103` edge `0.1124` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.786` n `105` status `ready` deltaP `18.5351` edge `0.0176` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.5249` n `62` status `ready` deltaP `26.3273` edge `0.0484` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.3301` n `105` status `ready` deltaP `7.592` edge `0.0145` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `0.3039` n `105` status `ready` deltaP `10.5831` edge `0.0573` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
