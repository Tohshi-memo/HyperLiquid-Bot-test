# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T14:07:29.768254+00:00`
- Price records: `672`
- Market context records: `7361`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.818` n `32` status `ready` deltaP `37.7287` edge `0.3359` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.818` n `32` status `ready` deltaP `37.7287` edge `0.3359` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.5889` n `32` status `ready` deltaP `31.0213` edge `0.2833` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.5889` n `32` status `ready` deltaP `31.0213` edge `0.2833` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.2391` n `32` status `ready` deltaP `17.5305` edge `0.3627` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.2391` n `32` status `ready` deltaP `17.5305` edge `0.3627` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2121` n `32` status `ready` deltaP `19.9289` edge `0.047` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2121` n `32` status `ready` deltaP `19.9289` edge `0.047` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2271` n `32` status `ready` deltaP `3.9977` edge `0.0202` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2271` n `32` status `ready` deltaP `3.9977` edge `0.0202` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1538` n `32` status `ready` deltaP `3.9039` edge `0.0314` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1538` n `32` status `ready` deltaP `3.9039` edge `0.0314` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1149` n `32` status `ready` deltaP `0.5988` edge `0.0478` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1149` n `32` status `ready` deltaP `0.5988` edge `0.0478` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1514` n `32` status `ready` deltaP `-0.6098` edge `0.0738` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1514` n `32` status `ready` deltaP `-0.6098` edge `0.0738` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1715` n `129` status `ready` deltaP `4.089` edge `-0.0003` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.6375` n `129` status `ready` deltaP `5.4665` edge `0.1177` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7284` n `129` status `ready` deltaP `-3.4151` edge `-0.0134` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.8253` n `111` status `ready` deltaP `2.9963` edge `-0.003` maxDD `-2.1564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
