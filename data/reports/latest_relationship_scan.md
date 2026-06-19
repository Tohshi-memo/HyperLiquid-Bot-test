# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T21:52:25.671315+00:00`
- Price records: `672`
- Market context records: `4143`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10032`

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

- `risk_on_high->unknown_4h` score `144.7436` n `40` status `ready` deltaP `-10.1829` edge `12.3117` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.7436` n `40` status `ready` deltaP `-10.1829` edge `12.3117` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.087` n `202` status `ready` deltaP `1.3903` edge `3.3226` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `11.802` n `198` status `ready` deltaP `-12.2753` edge `1.4687` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7445` n `202` status `ready` deltaP `-4.8116` edge `1.3871` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.6024` n `40` status `ready` deltaP `35.4573` edge `-0.0148` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.6024` n `40` status `ready` deltaP `35.4573` edge `-0.0148` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.2643` n `40` status `ready` deltaP `17.0122` edge `0.0585` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2643` n `40` status `ready` deltaP `17.0122` edge `0.0585` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.422` n `40` status `ready` deltaP `-0.7319` edge `0.2682` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.422` n `40` status `ready` deltaP `-0.7319` edge `0.2682` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.2879` n `40` status `ready` deltaP `11.0629` edge `-0.0108` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2879` n `40` status `ready` deltaP `11.0629` edge `-0.0108` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.1679` n `40` status `ready` deltaP `9.2683` edge `-0.0067` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1679` n `40` status `ready` deltaP `9.2683` edge `-0.0067` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.1579` n `40` status `ready` deltaP `10.3593` edge `0.0054` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1579` n `40` status `ready` deltaP `10.3593` edge `0.0054` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0423` n `40` status `ready` deltaP `9.3293` edge `0.0023` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0423` n `40` status `ready` deltaP `9.3293` edge `0.0023` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0241` n `40` status `ready` deltaP `3.8024` edge `0.0007` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
