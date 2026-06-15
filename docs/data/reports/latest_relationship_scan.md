# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T18:37:42.231293+00:00`
- Price records: `672`
- Market context records: `4016`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `146.6216` n `40` status `ready` deltaP `-4.9049` edge `12.4328` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.6216` n `40` status `ready` deltaP `-4.9049` edge `12.4328` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.8597` n `135` status `ready` deltaP `-4.2647` edge `4.4196` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.1805` n `146` status `ready` deltaP `1.9787` edge `2.7108` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.9585` n `40` status `ready` deltaP `39.3414` edge `0.3176` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.9585` n `40` status `ready` deltaP `39.3414` edge `0.3176` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.477` n `40` status `ready` deltaP `36.1606` edge `0.0534` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.477` n `40` status `ready` deltaP `36.1606` edge `0.0534` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.2853` n `135` status `ready` deltaP `25.5549` edge `0.1519` maxDD `-3.2125`
- `market_context_high->metal_24h` score `2.4328` n `135` status `ready` deltaP `13.7313` edge `0.2301` maxDD `-6.5125`
- `market_context_high->equity_4h` score `1.6648` n `146` status `ready` deltaP `18.7976` edge `0.1415` maxDD `-6.9137`
- `risk_on_high->index_24h` score `1.4357` n `40` status `ready` deltaP `27.0364` edge `-0.0606` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.4357` n `40` status `ready` deltaP `27.0364` edge `-0.0606` maxDD `0.0`
- `market_context_high->equity_1h` score `1.2249` n `149` status `ready` deltaP `8.4365` edge `0.1018` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.1321` n `40` status `ready` deltaP `19.3798` edge `0.0317` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1321` n `40` status `ready` deltaP `19.3798` edge `0.0317` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.0175` n `149` status `ready` deltaP `10.0209` edge `0.0722` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.9716` n `40` status `ready` deltaP `4.2028` edge `0.2811` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9716` n `40` status `ready` deltaP `4.2028` edge `0.2811` maxDD `-12.9187`
- `market_context_high->equity_24h` score `0.6653` n `135` status `ready` deltaP `15.6377` edge `0.251` maxDD `-14.318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
