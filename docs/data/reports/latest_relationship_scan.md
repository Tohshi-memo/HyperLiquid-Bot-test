# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T03:22:27.097707+00:00`
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

- `market_context_high->unknown_4h` score `38.7136` n `90` status `ready` deltaP `-3.8965` edge `3.306` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8273` n `62` status `ready` deltaP `38.0542` edge `0.6689` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.937` n `62` status `ready` deltaP `22.2591` edge `0.5641` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.2462` n `62` status `ready` deltaP `15.6555` edge `0.4261` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.8364` n `62` status `ready` deltaP `35.0604` edge `0.1693` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.356` n `90` status `ready` deltaP `10.6563` edge `0.7848` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.989` n `62` status `ready` deltaP `32.6975` edge `0.0573` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4748` n `62` status `ready` deltaP `10.256` edge `0.1734` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3224` n `90` status `ready` deltaP `16.1187` edge `0.1825` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2136` n `62` status `ready` deltaP `17.8745` edge `0.1251` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.964` n `62` status `ready` deltaP `24.6541` edge `0.0143` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.7416` n `90` status `ready` deltaP `13.2182` edge `0.0999` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.4932` n `62` status `ready` deltaP `-6.8715` edge `0.2948` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4533` n `62` status `ready` deltaP `21.0144` edge `0.0878` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2401` n `90` status `ready` deltaP `21.5371` edge `0.1639` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.1003` n `62` status `ready` deltaP `2.9389` edge `0.124` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0938` n `90` status `ready` deltaP `22.0396` edge `0.0189` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7176` n `90` status `ready` deltaP `12.0179` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1436` n `90` status `ready` deltaP `10.1843` edge `0.0394` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1308` n `90` status `ready` deltaP `7.1964` edge `0.5626` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
