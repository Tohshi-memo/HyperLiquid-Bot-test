# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T22:38:01.478539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `12.9155` n `117` status `ready` deltaP `26.4557` edge `0.9229` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `12.9155` n `117` status `ready` deltaP `26.4557` edge `0.9229` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `7.868` n `241` status `ready` deltaP `19.1109` edge `0.611` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.9859` n `117` status `ready` deltaP `22.1421` edge `1.1548` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.9859` n `117` status `ready` deltaP `22.1421` edge `1.1548` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.5333` n `117` status `ready` deltaP `35.0558` edge `0.3479` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.5333` n `117` status `ready` deltaP `35.0558` edge `0.3479` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.5667` n `117` status `ready` deltaP `25.2189` edge `0.2983` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.5667` n `117` status `ready` deltaP `25.2189` edge `0.2983` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.6781` n `117` status `ready` deltaP `26.7762` edge `0.0489` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.6781` n `117` status `ready` deltaP `26.7762` edge `0.0489` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.9567` n `241` status `ready` deltaP `21.8714` edge `0.0566` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.8274` n `241` status `ready` deltaP `10.2431` edge `0.084` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1805` n `117` status `ready` deltaP `4.5461` edge `0.1033` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1805` n `117` status `ready` deltaP `4.5461` edge `0.1033` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `1.1422` n `117` status `ready` deltaP `10.2431` edge `0.0269` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1422` n `117` status `ready` deltaP `10.2431` edge `0.0269` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7996` n `117` status `ready` deltaP `19.7383` edge `0.0865` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7996` n `117` status `ready` deltaP `19.7383` edge `0.0865` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4916` n `117` status `ready` deltaP `14.8217` edge `-0.0047` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
