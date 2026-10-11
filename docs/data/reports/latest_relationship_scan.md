# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T13:22:27.185115+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7286`

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

- `market_context_high->unknown_24h` score `686.6074` n `48` status `ready` deltaP `-15.2777` edge `57.3555` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `47.3025` n `80` status `ready` deltaP `-8.2012` edge `4.0546` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9433` n `48` status `ready` deltaP `31.9444` edge `0.5752` maxDD `-1.0977`
- `market_context_high->index_24h` score `4.3212` n `48` status `ready` deltaP `36.9791` edge `0.1521` maxDD `-0.4155`
- `market_context_high->crypto_major_24h` score `3.3929` n `48` status `ready` deltaP `-7.8125` edge `0.8019` maxDD `-17.8526`
- `market_context_high->fx_24h` score `1.8672` n `48` status `ready` deltaP `25.0` edge `0.0274` maxDD `-0.4104`
- `market_context_high->fx_4h` score `1.131` n `80` status `ready` deltaP `17.0122` edge `0.0092` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.202` n `80` status `ready` deltaP `9.1159` edge `0.0094` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1881` n `85` status `ready` deltaP `4.7816` edge `0.0089` maxDD `-0.3417`
- `market_context_high->fx_1h` score `-0.2623` n `85` status `ready` deltaP `0.2043` edge `0.001` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.4732` n `85` status `ready` deltaP `2.8778` edge `0.0448` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.4938` n `80` status `ready` deltaP `-1.25` edge `0.0173` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.497` n `85` status `ready` deltaP `2.3212` edge `0.0022` maxDD `-0.7275`
- `market_context_high->unknown_1h` score `-0.6124` n `85` status `ready` deltaP `-6.4213` edge `0.0254` maxDD `-1.0231`
- `market_context_high->crypto_major_1h` score `-0.954` n `85` status `ready` deltaP `-1.3367` edge `0.0183` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-1.1776` n `80` status `ready` deltaP `-3.8415` edge `0.0852` maxDD `-11.1784`
- `market_context_high->index_1h` score `-1.1912` n `85` status `ready` deltaP `-9.4223` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.2353` n `85` status `ready` deltaP `-9.528` edge `-0.0079` maxDD `-2.2898`
- `market_context_high->index_4h` score `-1.265` n `80` status `ready` deltaP `-12.8049` edge `-0.0005` maxDD `-1.1051`
- `market_context_high->crypto_alt_4h` score `-1.9093` n `80` status `ready` deltaP `-6.9207` edge `0.0572` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
