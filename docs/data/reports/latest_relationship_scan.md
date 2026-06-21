# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T04:22:25.168591+00:00`
- Price records: `672`
- Market context records: `4278`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10816`

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

- `risk_on_high->unknown_4h` score `130.4554` n `44` status `ready` deltaP `-2.9657` edge `11.0729` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.4554` n `44` status `ready` deltaP `-2.9657` edge `11.0729` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.7816` n `236` status `ready` deltaP `1.8574` edge `2.4607` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.812` n `236` status `ready` deltaP `0.0775` edge `1.2768` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.702` n `200` status `ready` deltaP `-8.9097` edge `1.1046` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.1251` n `44` status `ready` deltaP `32.0261` edge `-0.0317` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1251` n `44` status `ready` deltaP `32.0261` edge `-0.0317` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.8232` n `44` status `ready` deltaP `14.648` edge `0.0375` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8232` n `44` status `ready` deltaP `14.648` edge `0.0375` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `0.7571` n `40` status `ready` deltaP `-23.2986` edge `0.3138` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.7571` n `40` status `ready` deltaP `-23.2986` edge `0.3138` maxDD `-1.9133`
- `risk_on_high->fx_1h` score `0.4746` n `44` status `ready` deltaP `8.7915` edge `0.0039` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4746` n `44` status `ready` deltaP `8.7915` edge `0.0039` maxDD `-0.1704`
- `risk_on_high->equity_24h` score `0.3789` n `40` status `ready` deltaP `22.9167` edge `-0.1212` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.3789` n `40` status `ready` deltaP `22.9167` edge `-0.1212` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.095` n `44` status `ready` deltaP `7.6484` edge `0.0154` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.095` n `44` status `ready` deltaP `7.6484` edge `0.0154` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0423` n `44` status `ready` deltaP `8.9385` edge `0.0049` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0423` n `44` status `ready` deltaP `8.9385` edge `0.0049` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0489` n `44` status `ready` deltaP `6.9271` edge `-0.0113` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
