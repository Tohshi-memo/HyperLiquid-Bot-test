# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T17:22:16.750922+00:00`
- Price records: `665`
- Market context records: `777`
- Flow alert records: `2189`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.3875` n `147` status `ready` deltaP `31.5783` edge `0.9385` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4558` n `147` status `ready` deltaP `7.2283` edge `0.4946` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6516` n `32` status `ready` deltaP `10.218` edge `0.2727` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6516` n `32` status `ready` deltaP `10.218` edge `0.2727` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.991` n `32` status `ready` deltaP `19.1037` edge `0.1307` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.991` n `32` status `ready` deltaP `19.1037` edge `0.1307` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.8269` n `32` status `ready` deltaP `21.0709` edge `0.1323` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8269` n `32` status `ready` deltaP `21.0709` edge `0.1323` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6772` n `32` status `ready` deltaP `21.5957` edge `0.0996` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6772` n `32` status `ready` deltaP `21.5957` edge `0.0996` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0611` n `33` status `ready` deltaP `12.9648` edge `0.025` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0611` n `33` status `ready` deltaP `12.9648` edge `0.025` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7585` n `32` status `ready` deltaP `4.7045` edge `0.149` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7585` n `32` status `ready` deltaP `4.7045` edge `0.149` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4689` n `147` status `ready` deltaP `2.7283` edge `0.2204` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.2935` n `33` status `ready` deltaP `8.8419` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2935` n `33` status `ready` deltaP `8.8419` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2482` n `33` status `ready` deltaP `7.6657` edge `0.0183` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2482` n `33` status `ready` deltaP `7.6657` edge `0.0183` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0606` n `33` status `ready` deltaP `4.777` edge `-0.0092` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
