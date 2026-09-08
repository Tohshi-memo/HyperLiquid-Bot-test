# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T16:07:32.168349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10444`

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

- `risk_on_high->crypto_alt_24h` score `7.1923` n `117` status `ready` deltaP `17.6015` edge `0.505` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.1923` n `117` status `ready` deltaP `17.6015` edge `0.505` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5774` n `117` status `ready` deltaP `30.7875` edge `0.2967` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5774` n `117` status `ready` deltaP `30.7875` edge `0.2967` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.4898` n `117` status `ready` deltaP `20.5796` edge `0.8452` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.4898` n `117` status `ready` deltaP `20.5796` edge `0.8452` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.4015` n `117` status `ready` deltaP `24.6092` edge `0.2886` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.4015` n `117` status `ready` deltaP `24.6092` edge `0.2886` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `2.1449` n `241` status `ready` deltaP `10.2567` edge `0.1931` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.8386` n `117` status `ready` deltaP `3.6479` edge `0.0808` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8386` n `117` status `ready` deltaP `3.6479` edge `0.0808` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.632` n `117` status `ready` deltaP `8.8942` edge `-0.0024` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.632` n `117` status `ready` deltaP `8.8942` edge `-0.0024` maxDD `-0.0051`
- `risk_on_high->metal_1h` score `0.2232` n `117` status `ready` deltaP `9.0806` edge `0.0011` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2232` n `117` status `ready` deltaP `9.0806` edge `0.0011` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.1836` n `117` status `ready` deltaP `12.5762` edge `-0.0154` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1836` n `117` status `ready` deltaP `12.5762` edge `-0.0154` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.1484` n `117` status `ready` deltaP `8.9693` edge `-0.0044` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1484` n `117` status `ready` deltaP `8.9693` edge `-0.0044` maxDD `-0.5764`
- `risk_on_high->crypto_major_1h` score `0.127` n `117` status `ready` deltaP `3.5852` edge `0.0594` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
