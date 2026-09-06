# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T03:37:27.665087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11077`

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

- `risk_on_high->unknown_4h` score `22.1649` n `145` status `ready` deltaP `-3.1602` edge `2.0687` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `22.1649` n `145` status `ready` deltaP `-3.1602` edge `2.0687` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.422` n `243` status `ready` deltaP `1.148` edge `0.941` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.5506` n `37` status `ready` deltaP `22.2269` edge `0.258` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9535` n `37` status `ready` deltaP `20.1389` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2297` n `37` status `ready` deltaP `16.1132` edge `0.203` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4771` n `37` status `ready` deltaP `25.3708` edge `0.0594` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.969` n `163` status `ready` deltaP `13.8633` edge `0.4255` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5727` n `37` status `ready` deltaP `12.935` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5466` n `37` status `ready` deltaP `7.4654` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3688` n `37` status `ready` deltaP `16.3619` edge `0.0243` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.103` n `37` status `ready` deltaP `21.8656` edge `0.0477` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.0672` n `37` status `ready` deltaP `5.5673` edge `0.0701` maxDD `-0.4628`
- `risk_on_high->crypto_major_24h` score `0.8784` n `80` status `ready` deltaP `10.2778` edge `0.7767` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.8784` n `80` status `ready` deltaP `10.2778` edge `0.7767` maxDD `-47.9416`
- `news_risk_high->crypto_alt_1h` score `0.7858` n `37` status `ready` deltaP `8.2781` edge `0.0368` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `-0.0293` n `37` status `ready` deltaP `5.7251` edge `0.0027` maxDD `-0.9036`
- `news_risk_high->crypto_alt_4h` score `-0.083` n `37` status `ready` deltaP `2.5874` edge `0.0087` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.1162` n `145` status `ready` deltaP `4.937` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
