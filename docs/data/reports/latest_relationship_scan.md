# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T20:16:07.635663+00:00`
- Price records: `672`
- Market context records: `7388`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14654`

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

- `risk_on_high->crypto_major_4h` score `6.1358` n `32` status `ready` deltaP `35.4421` edge `0.2943` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1358` n `32` status `ready` deltaP `35.4421` edge `0.2943` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9039` n `32` status `ready` deltaP `15.3963` edge `0.349` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9039` n `32` status `ready` deltaP `15.3963` edge `0.349` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6734` n `32` status `ready` deltaP `27.3628` edge `0.2314` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6734` n `32` status `ready` deltaP `27.3628` edge `0.2314` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.1489` n `32` status `ready` deltaP `19.7792` edge `0.0399` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1489` n `32` status `ready` deltaP `19.7792` edge `0.0399` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.394` n `32` status `ready` deltaP `5.3491` edge `0.0251` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.394` n `32` status `ready` deltaP `5.3491` edge `0.0251` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0096` n `32` status `ready` deltaP `0.0` edge `0.0383` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0096` n `32` status `ready` deltaP `0.0` edge `0.0383` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1764` n `32` status `ready` deltaP `-0.4573` edge `0.0707` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1764` n `32` status `ready` deltaP `-0.4573` edge `0.0707` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1795` n `132` status `ready` deltaP `3.9312` edge `-0.0001` maxDD `-0.5967`
- `market_context_high->commodity_1h` score `-0.5314` n `132` status `ready` deltaP `-0.9009` edge `-0.0049` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7254` n `129` status `ready` deltaP `-0.3236` edge `0.006` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.8553` n `129` status `ready` deltaP `3.3323` edge `0.104` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
