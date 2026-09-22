# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T20:52:32.145571+00:00`
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

- `market_context_high->unknown_4h` score `45.5382` n `46` status `ready` deltaP `7.0122` edge `3.7481` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5374` n `46` status `ready` deltaP `13.0133` edge `2.3903` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2049` n `46` status `ready` deltaP `12.1453` edge `1.2795` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.775` n `46` status `ready` deltaP `10.9375` edge `1.075` maxDD `0.0`
- `market_context_high->index_24h` score `5.5155` n `46` status `ready` deltaP `19.6105` edge `0.3376` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.1631` n `96` status `ready` deltaP `38.5417` edge `0.2912` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8438` n `96` status `ready` deltaP `-9.7222` edge `1.1543` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9269` n `96` status `ready` deltaP `14.4817` edge `0.2051` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.8065` n `96` status `ready` deltaP `10.9756` edge `0.2605` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.1599` n `96` status `ready` deltaP `12.132` edge `0.1345` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8596` n `46` status `ready` deltaP `22.2494` edge `0.02` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5362` n `96` status `ready` deltaP `13.7787` edge `0.0755` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2392` n `96` status `ready` deltaP `19.0295` edge `0.04` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.9141` n `46` status `ready` deltaP `21.3995` edge `-0.0431` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.8841` n `96` status `ready` deltaP `-8.8542` edge `0.6208` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.7094` n `46` status `ready` deltaP `6.4632` edge `0.0403` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->fx_24h` score `0.6243` n `96` status `ready` deltaP `20.8333` edge `0.1001` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6209` n `96` status `ready` deltaP `15.0262` edge `0.0109` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.4252` n `96` status `ready` deltaP `18.2292` edge `0.0174` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
