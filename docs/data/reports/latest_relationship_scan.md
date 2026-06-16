# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T14:22:38.767343+00:00`
- Price records: `672`
- Market context records: `4099`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10424`

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

- `risk_on_high->unknown_4h` score `144.7083` n `40` status `ready` deltaP `-8.811` edge `12.2994` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7083` n `40` status `ready` deltaP `-8.811` edge `12.2994` maxDD `-10.864`
- `market_context_high->unknown_1h` score `46.7342` n `181` status `ready` deltaP `2.1124` edge `4.0382` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.1081` n `144` status `ready` deltaP `-9.2396` edge `3.5568` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.665` n `177` status `ready` deltaP `-1.9042` edge `1.8604` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.5483` n `40` status `ready` deltaP `36.372` edge `-0.0254` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.5483` n `40` status `ready` deltaP `36.372` edge `-0.0254` maxDD `-0.0446`
- `market_context_high->equity_1h` score `0.4316` n `181` status `ready` deltaP `4.7392` edge `0.0633` maxDD `-2.3807`
- `risk_on_high->equity_1h` score `0.3656` n `40` status `ready` deltaP `10.9132` edge `-0.0032` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3656` n `40` status `ready` deltaP `10.9132` edge `-0.0032` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0902` n `40` status `ready` deltaP `5.0` edge `0.0012` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0902` n `40` status `ready` deltaP `5.0` edge `0.0012` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0285` n `40` status `ready` deltaP `10.509` edge `-0.0195` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0285` n `40` status `ready` deltaP `10.509` edge `-0.0195` maxDD `-2.3372`
- `market_context_high->equity_4h` score `-0.1852` n `177` status `ready` deltaP `11.7534` edge `0.0593` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `-0.201` n `40` status `ready` deltaP `15.9451` edge `-0.0565` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.201` n `40` status `ready` deltaP `15.9451` edge `-0.0565` maxDD `-2.6576`
- `market_context_high->metal_1h` score `-0.2478` n `181` status `ready` deltaP `6.849` edge `0.0255` maxDD `-4.9015`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
