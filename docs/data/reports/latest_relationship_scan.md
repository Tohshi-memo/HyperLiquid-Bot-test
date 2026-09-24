# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T01:52:30.324482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.2081` n `47` status `ready` deltaP `11.0142` edge `5.951` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.1883` n `46` status `ready` deltaP `23.43` edge `2.8751` maxDD `-0.5817`
- `market_context_high->equity_24h` score `21.0261` n `46` status `ready` deltaP `20.8258` edge `1.6234` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.3758` n `46` status `ready` deltaP `18.4028` edge `1.5753` maxDD `0.0`
- `market_context_high->index_24h` score `7.0646` n `46` status `ready` deltaP `29.8536` edge `0.3984` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.8939` n `100` status `ready` deltaP `-2.2222` edge `1.3479` maxDD `-52.0207`
- `news_risk_high->crypto_alt_4h` score `4.9273` n `103` status `ready` deltaP `14.5365` edge `0.4135` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5596` n `103` status `ready` deltaP `17.2804` edge `0.3225` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `2.7359` n `100` status `ready` deltaP `-4.5972` edge `0.806` maxDD `-37.4554`
- `news_risk_high->crypto_alt_1h` score `2.5941` n `103` status `ready` deltaP `13.6068` edge `0.1745` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.471` n `47` status `ready` deltaP `29.1483` edge `0.027` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4312` n `100` status `ready` deltaP `23.7431` edge `0.1622` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0481` n `103` status `ready` deltaP `15.8523` edge `0.1085` maxDD `-1.8141`
- `market_context_high->metal_24h` score `2.0398` n `46` status `ready` deltaP `23.8301` edge `0.0345` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6112` n `103` status `ready` deltaP `23.5289` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4255` n `47` status `ready` deltaP `11.5042` edge `0.0839` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1703` n `100` status `ready` deltaP `28.6736` edge `0.122` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7798` n `47` status `ready` deltaP `12.664` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6338` n `103` status `ready` deltaP `15.2026` edge `0.0108` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.5819` n `47` status `ready` deltaP `8.7718` edge `0.0303` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
