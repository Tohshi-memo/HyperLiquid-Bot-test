# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T11:07:29.428224+00:00`
- Price records: `672`
- Market context records: `7243`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13743`

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

- `risk_on_high->crypto_major_4h` score `5.9343` n `34` status `ready` deltaP `27.0804` edge `0.3523` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9343` n `34` status `ready` deltaP `27.0804` edge `0.3523` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2977` n `34` status `ready` deltaP `17.2525` edge `0.2824` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2977` n `34` status `ready` deltaP `17.2525` edge `0.2824` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1271` n `34` status `ready` deltaP `22.7974` edge `0.0403` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1271` n `34` status `ready` deltaP `22.7974` edge `0.0403` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0405` n `34` status `ready` deltaP `5.0741` edge `0.1372` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0405` n `34` status `ready` deltaP `5.0741` edge `0.1372` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2747` n `34` status `ready` deltaP `7.6259` edge `0.0134` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2747` n `34` status `ready` deltaP `7.6259` edge `0.0134` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2059` n `34` status `ready` deltaP `2.5311` edge `0.0303` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2059` n `34` status `ready` deltaP `2.5311` edge `0.0303` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1375` n `34` status `ready` deltaP `3.0667` edge `0.0218` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1375` n `34` status `ready` deltaP `3.0667` edge `0.0218` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2518` n `162` status `ready` deltaP `2.3941` edge `0.0007` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.649` n `34` status `ready` deltaP `-0.1078` edge `-0.0106` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.649` n `34` status `ready` deltaP `-0.1078` edge `-0.0106` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6514` n `162` status `ready` deltaP `-1.2041` edge `-0.0134` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.696` n `162` status `ready` deltaP `-0.1867` edge `0.0159` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7412` n `162` status `ready` deltaP `3.1234` edge `0.0252` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
