# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T05:07:28.193681+00:00`
- Price records: `672`
- Market context records: `4281`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10856`

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

- `risk_on_high->unknown_4h` score `130.5072` n `44` status `ready` deltaP `-2.8132` edge `11.0762` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.5072` n `44` status `ready` deltaP `-2.8132` edge `11.0762` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.76` n `236` status `ready` deltaP `2.0071` edge `2.4579` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.8638` n `236` status `ready` deltaP `0.23` edge `1.2801` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.7639` n `200` status `ready` deltaP `-8.7361` edge `1.1086` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.1395` n `44` status `ready` deltaP `32.0261` edge `-0.0305` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1395` n `44` status `ready` deltaP `32.0261` edge `-0.0305` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.8812` n `44` status `ready` deltaP `14.9529` edge `0.0403` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8812` n `44` status `ready` deltaP `14.9529` edge `0.0403` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `0.8754` n `40` status `ready` deltaP `-22.7778` edge `0.3255` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.8754` n `40` status `ready` deltaP `-22.7778` edge `0.3255` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `0.4953` n `40` status `ready` deltaP `22.9167` edge `-0.1115` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.4953` n `40` status `ready` deltaP `22.9167` edge `-0.1115` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1129` n `44` status `ready` deltaP `7.7981` edge `0.0167` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1129` n `44` status `ready` deltaP `7.7981` edge `0.0167` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0399` n `44` status `ready` deltaP `8.9385` edge `0.0046` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0399` n `44` status `ready` deltaP `8.9385` edge `0.0046` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.019` n `44` status `ready` deltaP `7.0768` edge `-0.0098` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
