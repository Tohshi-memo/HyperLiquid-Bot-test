# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T01:07:30.526577+00:00`
- Price records: `672`
- Market context records: `4991`
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

- `market_context_high->unknown_1h` score `20.5831` n `92` status `ready` deltaP `4.3869` edge `1.7361` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.2028` n `87` status `ready` deltaP `18.0964` edge `0.5448` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.0122` n `74` status `ready` deltaP `28.9461` edge `0.3423` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1806` n `87` status `ready` deltaP `12.7366` edge `0.4862` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5377` n `87` status `ready` deltaP `20.8894` edge `0.0911` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.9105` n `92` status `ready` deltaP `6.9643` edge `0.1212` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.8877` n `92` status `ready` deltaP `8.2075` edge `0.0766` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6236` n `87` status `ready` deltaP `5.1602` edge `0.1837` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.388` n `87` status `ready` deltaP `5.6052` edge `0.0432` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3874` n `92` status `ready` deltaP `6.5152` edge `0.0385` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2132` n `92` status `ready` deltaP `5.5454` edge `0.0926` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2691` n `74` status `ready` deltaP `5.565` edge `0.0046` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3514` n `92` status `ready` deltaP `1.3082` edge `0.0122` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5689` n `92` status `ready` deltaP `2.0242` edge `0.0132` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8271` n `87` status `ready` deltaP `-1.1845` edge `-0.0011` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2822` n `87` status `ready` deltaP `3.5867` edge `-0.0055` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7399` n `92` status `ready` deltaP `-11.7743` edge `-0.0056` maxDD `-0.5386`
- `market_context_high->commodity_24h` score `-3.9594` n `74` status `ready` deltaP `7.7045` edge `-0.0481` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.272` n `74` status `ready` deltaP `-1.2153` edge `0.0059` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
