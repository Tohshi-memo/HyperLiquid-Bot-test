# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T00:07:25.006345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.9517` n `74` status `ready` deltaP `7.9763` edge `0.1594` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.229` n `74` status `ready` deltaP `8.8703` edge `0.018` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.1035` n `74` status `ready` deltaP `8.2497` edge `0.0036` maxDD `-0.2931`
- `news_risk_high->index_24h` score `0.0922` n `74` status `ready` deltaP `5.4664` edge `0.1422` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `0.0646` n `74` status `ready` deltaP `2.1039` edge `0.0492` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0127` n `74` status `ready` deltaP `6.0234` edge `0.0028` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.2002` n `74` status `ready` deltaP `-2.2991` edge `0.0429` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2403` n `74` status `ready` deltaP `0.9144` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.3886` n `74` status `ready` deltaP `-1.1976` edge `-0.0061` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-1.1589` n `74` status `ready` deltaP `-5.4135` edge `-0.0186` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.254` n `74` status `ready` deltaP `-4.5937` edge `-0.0396` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-2.192` n `74` status `ready` deltaP `-3.4634` edge `-0.0368` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-2.7409` n `74` status `ready` deltaP `-7.3047` edge `-0.0111` maxDD `-9.1553`
- `news_risk_high->commodity_1h` score `-2.7925` n `74` status `ready` deltaP `-17.5635` edge `-0.0076` maxDD `-1.6417`
- `news_risk_high->equity_24h` score `-3.1164` n `74` status `ready` deltaP `21.7343` edge `0.6142` maxDD `-86.0244`
- `news_risk_high->metal_24h` score `-3.3028` n `74` status `ready` deltaP `0.0704` edge `-0.2343` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0499` n `74` status `ready` deltaP `-26.2648` edge `-0.0026` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.7423` n `74` status `ready` deltaP `-9.4388` edge `-0.0694` maxDD `-14.0292`
- `news_risk_high->commodity_24h` score `-9.6976` n `74` status `ready` deltaP `-26.478` edge `-0.0637` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.162` n `74` status `ready` deltaP `-29.9268` edge `-0.047` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
