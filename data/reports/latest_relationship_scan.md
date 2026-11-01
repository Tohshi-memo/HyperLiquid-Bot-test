# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T17:52:28.312566+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6619`

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

- `market_context_high->unknown_24h` score `7219.4839` n `55` status `ready` deltaP `1.3889` edge `601.6144` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.2768` n `55` status `ready` deltaP `6.4135` edge `31.6513` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `63.7058` n `55` status `ready` deltaP `4.2107` edge `5.2918` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1192` n `55` status `ready` deltaP `42.7999` edge `1.4982` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1988` n `94` status `ready` deltaP `30.9619` edge `1.0291` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5823` n `55` status `ready` deltaP `53.2986` edge `0.1932` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2513` n `55` status `ready` deltaP `43.8795` edge `0.2595` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1702` n `55` status `ready` deltaP `24.5122` edge `0.3802` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6745` n `55` status `ready` deltaP `31.3498` edge `0.2975` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.508` n `55` status `ready` deltaP `6.2001` edge `0.3212` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3551` n `55` status `ready` deltaP `31.5244` edge `0.0945` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.6209` n `125` status `ready` deltaP `10.9122` edge `0.2843` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3657` n `55` status `ready` deltaP `10.1642` edge `0.3032` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8896` n `55` status `ready` deltaP `-4.2992` edge `0.4227` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6884` n `55` status `ready` deltaP `19.7228` edge `0.0517` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5908` n `55` status `ready` deltaP `3.6255` edge `0.1609` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.489` n `55` status `ready` deltaP `4.5237` edge `0.161` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4707` n `55` status `ready` deltaP `8.6309` edge `0.126` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9642` n `55` status `ready` deltaP `11.9243` edge `0.0257` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5553` n `55` status `ready` deltaP `13.4867` edge `-0.0003` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
