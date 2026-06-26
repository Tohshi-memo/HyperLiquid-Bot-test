# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T20:37:32.586096+00:00`
- Price records: `672`
- Market context records: `4863`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `13.4298` n `110` status `ready` deltaP `10.0218` edge `1.0941` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.754` n `110` status `ready` deltaP `23.6197` edge `0.7085` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.2804` n `110` status `ready` deltaP `20.2938` edge `0.5233` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.996` n `110` status `ready` deltaP `17.5776` edge `0.5049` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1682` n `91` status `ready` deltaP `25.2957` edge `0.2963` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2876` n `110` status `ready` deltaP `9.7395` edge `0.1086` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8017` n `110` status `ready` deltaP `11.5244` edge `0.1641` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4618` n `110` status `ready` deltaP `10.1635` edge `0.0377` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4601` n `110` status `ready` deltaP `6.6195` edge `0.1187` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4168` n `110` status `ready` deltaP `8.1709` edge `0.1012` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2129` n `110` status `ready` deltaP `4.2352` edge `0.0588` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1308` n `110` status `ready` deltaP `1.4425` edge `0.0316` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2043` n `110` status `ready` deltaP `3.5819` edge `0.0159` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4876` n `110` status `ready` deltaP `0.3103` edge `0.0109` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6316` n `110` status `ready` deltaP `1.5244` edge `0.0059` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7785` n `110` status `ready` deltaP `7.0343` edge `0.0069` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3454` n `110` status `ready` deltaP `-7.0169` edge `-0.004` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8989` n `91` status `ready` deltaP `-6.8567` edge `-0.0115` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.7946` n `91` status `ready` deltaP `-8.3601` edge `-0.1504` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.3487` n `91` status `ready` deltaP `10.8535` edge `-0.0072` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
