# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T14:07:12.696497+00:00`
- Price records: `652`
- Market context records: `762`
- Flow alert records: `2149`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.5263` n `146` status `ready` deltaP `32.2484` edge `0.9456` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.8051` n `146` status `ready` deltaP `7.4086` edge `0.5225` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3039` n `32` status `ready` deltaP `15.0849` edge `0.0311` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3039` n `32` status `ready` deltaP `15.0849` edge `0.0311` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5785` n `146` status `ready` deltaP `3.2584` edge `0.226` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4313` n `32` status `ready` deltaP `10.6561` edge `0.0032` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4313` n `32` status `ready` deltaP `10.6561` edge `0.0032` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.2199` n `32` status `ready` deltaP `6.8517` edge `0.0201` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2199` n `32` status `ready` deltaP `6.8517` edge `0.0201` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1408` n `32` status `ready` deltaP `7.0602` edge `-0.0005` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1408` n `32` status `ready` deltaP `7.0602` edge `-0.0005` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.044` n `146` status `ready` deltaP `1.7918` edge `0.2522` maxDD `-10.5047`
- `risk_on_high->crypto_alt_1h` score `-0.325` n `32` status `ready` deltaP `3.858` edge `-0.0204` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.325` n `32` status `ready` deltaP `3.858` edge `-0.0204` maxDD `-0.9258`
- `risk_on_high->index_1h` score `-0.3495` n `32` status `ready` deltaP `-1.4946` edge `0.0092` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3495` n `32` status `ready` deltaP `-1.4946` edge `0.0092` maxDD `-0.2687`
- `market_context_high->fx_4h` score `-0.3664` n `166` status `ready` deltaP `4.7945` edge `0.0082` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.5243` n `178` status `ready` deltaP `1.49` edge `0.0082` maxDD `-2.8282`
- `market_context_high->fx_1h` score `-0.529` n `178` status `ready` deltaP `1.7727` edge `0.0019` maxDD `-0.291`
- `market_context_high->equity_1h` score `-0.6015` n `178` status `ready` deltaP `-0.3733` edge `0.0064` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
