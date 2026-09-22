# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T21:52:28.711417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.4622` n `46` status `ready` deltaP `6.7073` edge `3.7438` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5794` n `46` status `ready` deltaP `13.0133` edge `2.3938` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2073` n `46` status `ready` deltaP `12.1453` edge `1.2797` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.6082` n `46` status `ready` deltaP `10.9375` edge `1.0611` maxDD `0.0`
- `market_context_high->index_24h` score `5.5071` n `46` status `ready` deltaP `19.6105` edge `0.3369` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.0451` n `96` status `ready` deltaP `37.8472` edge `0.286` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8858` n `96` status `ready` deltaP `-9.7222` edge `1.1578` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.8965` n `96` status `ready` deltaP `14.1768` edge `0.2046` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.6821` n `96` status `ready` deltaP `10.3659` edge `0.2542` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.0868` n `96` status `ready` deltaP `11.6829` edge `0.1314` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8328` n `46` status `ready` deltaP `21.9445` edge `0.0198` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5242` n `96` status `ready` deltaP `13.7787` edge `0.0745` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2988` n `96` status `ready` deltaP `19.6393` edge `0.0409` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.8118` n `46` status `ready` deltaP `20.7051` edge `-0.047` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.7173` n `96` status `ready` deltaP `-8.8542` edge `0.6069` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.683` n `46` status `ready` deltaP `6.1638` edge `0.0401` maxDD `-0.2751`
- `news_risk_high->fx_24h` score `0.6815` n `96` status `ready` deltaP `21.5278` edge `0.1028` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6724` n `96` status `ready` deltaP `15.625` edge `0.0112` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.3586` n `96` status `ready` deltaP `17.5348` edge `0.0135` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
