# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T13:37:30.789523+00:00`
- Price records: `672`
- Market context records: `5883`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10248`

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

- `news_risk_high->fx_4h` score `3.7752` n `30` status `ready` deltaP `39.3902` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3485` n `231` status `ready` deltaP `8.1301` edge `0.1682` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9728` n `30` status `ready` deltaP `11.8363` edge `0.0925` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3066` n `30` status `ready` deltaP `5.4691` edge `0.049` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0878` n `234` status `ready` deltaP `5.4852` edge `0.0448` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3001` n `234` status `ready` deltaP `3.4815` edge `0.0054` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4165` n `30` status `ready` deltaP `1.6866` edge `-0.028` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.473` n `234` status `ready` deltaP `4.0586` edge `0.0444` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.4927` n `234` status `ready` deltaP `-0.746` edge `-0.0011` maxDD `-1.9006`
- `market_context_high->crypto_alt_1h` score `-0.5409` n `234` status `ready` deltaP `3.0759` edge `0.0436` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.5456` n `234` status `ready` deltaP `1.4292` edge `0.0053` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.752` n `234` status `ready` deltaP `-1.9218` edge `-0.001` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2627` n `30` status `ready` deltaP `-12.8443` edge `-0.0248` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.5635` n `231` status `ready` deltaP `8.984` edge `0.1769` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7889` n `30` status `ready` deltaP `-13.4248` edge `-0.0523` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.8603` n `231` status `ready` deltaP `-0.1498` edge `0.0147` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.3032` n `30` status `ready` deltaP `-16.8598` edge `-0.0795` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.3734` n `231` status `ready` deltaP `-1.5634` edge `-0.016` maxDD `-6.3754`
- `market_context_high->metal_4h` score `-2.471` n `231` status `ready` deltaP `-2.0826` edge `-0.0288` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
