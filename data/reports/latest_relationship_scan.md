# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T23:37:25.319054+00:00`
- Price records: `672`
- Market context records: `4984`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `12.616` n `89` status `ready` deltaP `3.7089` edge `1.0767` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1876` n `88` status `ready` deltaP `17.0732` edge `0.5405` maxDD `-7.4281`
- `market_context_high->unknown_24h` score `5.8724` n `76` status `ready` deltaP `28.189` edge `0.3357` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.2664` n `88` status `ready` deltaP `13.7334` edge `0.4867` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.9096` n `88` status `ready` deltaP `21.577` edge `0.1059` maxDD `-4.916`
- `market_context_high->metal_4h` score `1.1431` n `88` status `ready` deltaP `11.5577` edge `0.1261` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.6118` n `88` status `ready` deltaP `4.9335` edge `0.1837` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.5752` n `89` status `ready` deltaP `7.7525` edge `0.0794` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.5205` n `89` status `ready` deltaP `5.3522` edge `0.1249` maxDD `-4.841`
- `market_context_high->index_4h` score `0.453` n `88` status `ready` deltaP `6.3886` edge `0.0429` maxDD `-0.8193`
- `market_context_high->metal_1h` score `0.1841` n `89` status `ready` deltaP `4.0789` edge `0.0378` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1768` n `89` status `ready` deltaP `4.9805` edge `0.0917` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2512` n `76` status `ready` deltaP `5.9393` edge `0.0044` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.3469` n `89` status `ready` deltaP `2.3599` edge `0.0139` maxDD `-0.595`
- `market_context_high->commodity_1h` score `-0.4574` n `89` status `ready` deltaP `0.185` edge `0.0061` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.8044` n `88` status `ready` deltaP `-0.7622` edge `-0.001` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.213` n `88` status `ready` deltaP `4.2267` edge `-0.004` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.5419` n `89` status `ready` deltaP `-9.7776` edge `-0.0035` maxDD `-0.4511`
- `market_context_high->commodity_24h` score `-3.754` n `76` status `ready` deltaP `9.5852` edge `-0.0343` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.3866` n `76` status `ready` deltaP `-3.2255` edge `0.0046` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
