# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T07:07:29.644443+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.3299` n `107` status `ready` deltaP `21.2874` edge `0.5307` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3299` n `107` status `ready` deltaP `21.2874` edge `0.5307` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8764` n `151` status `ready` deltaP `17.58` edge `0.442` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2125` n `107` status `ready` deltaP `5.1682` edge `0.2076` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2125` n `107` status `ready` deltaP `5.1682` edge `0.2076` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0818` n `151` status `ready` deltaP `4.5307` edge `0.2063` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3065` n `61` status `ready` deltaP `2.2725` edge `0.1284` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.0463` n `107` status `ready` deltaP `11.3837` edge `0.1101` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.0463` n `107` status `ready` deltaP `11.3837` edge `0.1101` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.4503` n `151` status `ready` deltaP `10.7523` edge `0.0854` maxDD `-1.2314`
- `risk_on_high->crypto_alt_24h` score `0.2685` n `107` status `ready` deltaP `12.4027` edge `0.6421` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.2685` n `107` status `ready` deltaP `12.4027` edge `0.6421` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1669` n `61` status `ready` deltaP `10.8057` edge `0.0012` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0334` n `151` status `ready` deltaP `7.9738` edge `0.0146` maxDD `-1.5315`
- `risk_on_high->index_1h` score `0.0146` n `107` status `ready` deltaP `6.896` edge `0.0004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0146` n `107` status `ready` deltaP `6.896` edge `0.0004` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `-0.025` n `61` status `ready` deltaP `3.8335` edge `0.0129` maxDD `-1.3325`
- `risk_on_high->fx_24h` score `-0.0285` n `107` status `ready` deltaP `36.2977` edge `0.0241` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0285` n `107` status `ready` deltaP `36.2977` edge `0.0241` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0516` n `107` status `ready` deltaP `4.873` edge `0.0131` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
