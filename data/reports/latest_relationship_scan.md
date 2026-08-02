# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T20:37:28.223488+00:00`
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

- `news_risk_high->unknown_24h` score `4644.0113` n `65` status `ready` deltaP `24.2281` edge `386.8815` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.271` n `40` status `ready` deltaP `54.7569` edge `1.0306` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0778` n `40` status `ready` deltaP `51.3194` edge `0.5938` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.5244` n `65` status `ready` deltaP `16.3203` edge `0.3446` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5567` n `65` status `ready` deltaP `15.2533` edge `0.0661` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0651` n `40` status `ready` deltaP `13.9024` edge `0.1285` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7264` n `40` status `ready` deltaP `8.3537` edge `0.128` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.6599` n `40` status `ready` deltaP `12.2455` edge `0.0404` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.6503` n `40` status `ready` deltaP `20.4573` edge `0.0266` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.5718` n `65` status `ready` deltaP `8.8853` edge `0.0707` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.4443` n `40` status `ready` deltaP `13.8473` edge `0.0024` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2623` n `65` status `ready` deltaP `13.7265` edge `0.0261` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.1306` n `65` status `ready` deltaP `6.7734` edge `0.0398` maxDD `-3.1233`
- `news_risk_high->metal_4h` score `0.0281` n `65` status `ready` deltaP `4.6365` edge `0.0203` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0256` n `65` status `ready` deltaP `4.2285` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0234` n `65` status `ready` deltaP `3.655` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1721` n `65` status `ready` deltaP `1.9001` edge `0.0056` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2024` n `65` status `ready` deltaP `2.7568` edge `0.0277` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4549` n `40` status `ready` deltaP `-0.1497` edge `0.0054` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6636` n `65` status `ready` deltaP `3.0147` edge `-0.0277` maxDD `-2.8647`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
