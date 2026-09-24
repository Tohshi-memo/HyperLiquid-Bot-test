# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T04:07:25.804695+00:00`
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

- `market_context_high->unknown_1h` score `71.9886` n `47` status `ready` deltaP `10.7148` edge `5.9347` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `37.6309` n `46` status `ready` deltaP `24.9925` edge `2.9849` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `22.2516` n `46` status `ready` deltaP `19.9653` edge `1.7212` maxDD `0.0`
- `market_context_high->equity_24h` score `21.7799` n `46` status `ready` deltaP `22.3883` edge `1.6758` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.2964` n `46` status `ready` deltaP `31.4161` edge `0.4073` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9875` n `103` status `ready` deltaP `14.6889` edge `0.4175` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7302` n `103` status `ready` deltaP `18.3475` edge `0.3296` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `3.8898` n `103` status `ready` deltaP `-2.6985` edge `1.2464` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.6073` n `103` status `ready` deltaP `13.9062` edge `0.1736` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5708` n `47` status `ready` deltaP `30.2154` edge `0.0282` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.3772` n `46` status `ready` deltaP `25.3926` edge `0.0522` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.3441` n `103` status `ready` deltaP `22.8796` edge `0.1607` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.1116` n `103` status `ready` deltaP `16.3014` edge `0.1108` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.6312` n `47` status `ready` deltaP `12.8762` edge `0.0919` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5722` n `103` status `ready` deltaP `23.0716` edge `0.0408` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2226` n `103` status `ready` deltaP `29.6639` edge `0.1221` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8577` n `47` status `ready` deltaP `13.5622` edge `0.0089` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6937` n `103` status `ready` deltaP `15.8014` edge `0.0118` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6897` n `47` status `ready` deltaP `9.67` edge `0.0333` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.4047` n `103` status `ready` deltaP `15.3371` edge `0.0454` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
