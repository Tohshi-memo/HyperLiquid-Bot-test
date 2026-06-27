# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T17:22:29.991814+00:00`
- Price records: `672`
- Market context records: `4955`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9472`

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

- `market_context_high->unknown_1h` score `19.9234` n `94` status `ready` deltaP `10.0714` edge `1.6349` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.5588` n `91` status `ready` deltaP `28.4224` edge `0.9085` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4375` n `91` status `ready` deltaP `22.0065` edge `0.5955` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1959` n `91` status `ready` deltaP `22.5275` edge `0.5847` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8612` n `91` status `ready` deltaP `27.4935` edge `0.3394` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8709` n `91` status `ready` deltaP `15.2037` edge `0.1927` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.7648` n `91` status `ready` deltaP `13.4247` edge `0.1238` maxDD `-1.9651`
- `market_context_high->index_4h` score `1.0334` n `91` status `ready` deltaP `13.0629` edge `0.0452` maxDD `-0.6938`
- `market_context_high->equity_1h` score `1.0043` n `94` status `ready` deltaP `9.1254` edge `0.0802` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9872` n `94` status `ready` deltaP `9.6764` edge `0.1659` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.7666` n `94` status `ready` deltaP `10.4886` edge `0.1306` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1866` n `94` status `ready` deltaP `5.4051` edge `0.0375` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3424` n `94` status `ready` deltaP `2.7583` edge `0.0132` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3534` n `94` status `ready` deltaP `1.9302` edge `0.0078` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.838` n `91` status `ready` deltaP `7.8346` edge `-0.0034` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.2079` n `91` status `ready` deltaP `-7.9369` edge `-0.0049` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.422` n `91` status `ready` deltaP `-0.9558` edge `-0.0111` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.534` n `94` status `ready` deltaP `-9.4885` edge `-0.0046` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9959` n `91` status `ready` deltaP `19.6485` edge `0.0469` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.877` n `91` status `ready` deltaP `-8.8199` edge `0.0312` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
