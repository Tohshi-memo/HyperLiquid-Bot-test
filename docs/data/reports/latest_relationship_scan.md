# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T19:52:29.441953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.8418` n `46` status `ready` deltaP `7.0122` edge `3.7734` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.452` n `46` status `ready` deltaP `12.6661` edge `2.3855` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2229` n `46` status `ready` deltaP `12.1453` edge `1.281` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.9895` n `46` status `ready` deltaP `11.4583` edge `1.0894` maxDD `0.0`
- `market_context_high->index_24h` score `5.5251` n `46` status `ready` deltaP `19.6105` edge `0.3384` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.2846` n `96` status `ready` deltaP `39.2361` edge `0.2967` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.7585` n `96` status `ready` deltaP `-10.0694` edge `1.1495` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9921` n `96` status `ready` deltaP `14.7866` edge `0.2085` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.9549` n `96` status `ready` deltaP `11.5854` edge `0.2688` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.2126` n `96` status `ready` deltaP `12.4314` edge `0.1369` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8632` n `46` status `ready` deltaP `22.2494` edge `0.0203` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5506` n `96` status `ready` deltaP `13.9284` edge `0.0757` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.1832` n `96` status `ready` deltaP `18.4197` edge `0.0394` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.0985` n `96` status `ready` deltaP `-8.3334` edge `0.6352` maxDD `-32.7147`
- `market_context_high->metal_24h` score `1.0177` n `46` status `ready` deltaP `22.0939` edge `-0.0391` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7262` n `46` status `ready` deltaP `6.6129` edge `0.0407` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5933` n `96` status `ready` deltaP `14.7268` edge `0.0106` maxDD `-0.7468`
- `news_risk_high->fx_24h` score `0.5664` n `96` status `ready` deltaP `20.1389` edge `0.0973` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.4925` n `96` status `ready` deltaP `18.9236` edge `0.0214` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
