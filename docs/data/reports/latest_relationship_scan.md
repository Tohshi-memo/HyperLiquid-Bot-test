# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T22:52:25.396207+00:00`
- Price records: `672`
- Market context records: `4981`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `11.7781` n `92` status `ready` deltaP `4.7253` edge `1.0001` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.7162` n `88` status `ready` deltaP `18.0571` edge `0.5536` maxDD `-6.4771`
- `market_context_high->unknown_24h` score `5.8243` n `79` status `ready` deltaP `28.0678` edge `0.3325` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.715` n `88` status `ready` deltaP `15.7012` edge `0.5068` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `3.0889` n `88` status `ready` deltaP `24.5288` edge `0.1606` maxDD `-3.004`
- `market_context_high->metal_4h` score `1.3254` n `88` status `ready` deltaP `12.5416` edge `0.1264` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7911` n `88` status `ready` deltaP `7.8853` edge `0.187` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5617` n `88` status `ready` deltaP `7.3725` edge `0.0438` maxDD `-0.691`
- `market_context_high->equity_1h` score `0.4585` n `92` status `ready` deltaP `6.0336` edge `0.0759` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.3202` n `92` status `ready` deltaP `3.8531` edge `0.1165` maxDD `-5.4247`
- `market_context_high->crypto_alt_1h` score `0.1835` n `92` status `ready` deltaP `5.3957` edge `0.0898` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0622` n `92` status `ready` deltaP `2.7662` edge `0.0364` maxDD `-1.3057`
- `market_context_high->fx_24h` score `-0.3872` n `79` status `ready` deltaP `3.9381` edge `0.0003` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4306` n `92` status `ready` deltaP `0.6704` edge `0.0063` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4424` n `92` status `ready` deltaP `0.7876` edge `0.013` maxDD `-0.6644`
- `market_context_high->fx_4h` score `-0.9625` n `88` status `ready` deltaP `-3.714` edge `-0.0016` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2466` n `88` status `ready` deltaP `4.2267` edge `-0.0068` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.617` n `92` status `ready` deltaP `-10.5376` edge `-0.0046` maxDD `-0.4587`
- `market_context_high->commodity_24h` score `-3.5037` n `79` status `ready` deltaP `11.9836` edge `-0.0182` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.4406` n `79` status `ready` deltaP `-5.0743` edge `0.01` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
