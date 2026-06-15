# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T17:53:02.313038+00:00`
- Price records: `672`
- Market context records: `4013`
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

- `risk_on_high->unknown_4h` score `146.9112` n `40` status `ready` deltaP `-4.6005` edge `12.4549` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.9112` n `40` status `ready` deltaP `-4.6005` edge `12.4549` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.3933` n `135` status `ready` deltaP `-3.7448` edge `4.4606` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.47` n `146` status `ready` deltaP `2.2831` edge `2.7329` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `7.3817` n `40` status `ready` deltaP `39.8614` edge `0.3494` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.3817` n `40` status `ready` deltaP `39.8614` edge `0.3494` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5843` n `40` status `ready` deltaP `36.6172` edge `0.0593` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.5843` n `40` status `ready` deltaP `36.6172` edge `0.0593` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.5297` n `135` status `ready` deltaP `26.0748` edge `0.1688` maxDD `-3.2125`
- `market_context_high->metal_24h` score `2.712` n `135` status `ready` deltaP `14.2512` edge `0.2499` maxDD `-6.5125`
- `market_context_high->equity_4h` score `1.7721` n `146` status `ready` deltaP `19.2542` edge `0.1474` maxDD `-6.9137`
- `risk_on_high->index_24h` score `1.6801` n `40` status `ready` deltaP `27.5563` edge `-0.0437` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.6801` n `40` status `ready` deltaP `27.5563` edge `-0.0437` maxDD `0.0`
- `market_context_high->equity_1h` score `1.2429` n `149` status `ready` deltaP `8.5862` edge `0.1023` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.1743` n `40` status `ready` deltaP `19.532` edge `0.0342` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1743` n `40` status `ready` deltaP `19.532` edge `0.0342` maxDD `-2.6576`
- `market_context_high->equity_24h` score `1.0885` n `135` status `ready` deltaP `16.1577` edge `0.2828` maxDD `-14.318`
- `market_context_high->crypto_major_1h` score `1.0247` n `149` status `ready` deltaP `10.1706` edge `0.0718` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.9896` n `40` status `ready` deltaP `4.2028` edge `0.2826` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9896` n `40` status `ready` deltaP `4.2028` edge `0.2826` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
