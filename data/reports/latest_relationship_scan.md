# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T00:22:25.849362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.6708` n `107` status `ready` deltaP `23.2691` edge `0.5458` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.6708` n `107` status `ready` deltaP `23.2691` edge `0.5458` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.1236` n `159` status `ready` deltaP `19.9657` edge `0.4466` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.0865` n `107` status `ready` deltaP `5.0185` edge `0.1981` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.0865` n `107` status `ready` deltaP `5.0185` edge `0.1981` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.8627` n `159` status `ready` deltaP `4.3602` edge `0.1892` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.621` n `94` status `ready` deltaP `13.2276` edge `0.1457` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.621` n `94` status `ready` deltaP `13.2276` edge `0.1457` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1809` n `61` status `ready` deltaP `2.1228` edge `0.1189` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.6925` n `94` status `ready` deltaP `41.1495` edge `0.0237` maxDD `-3.7401`
- `risk_on_and_context->fx_24h` score `0.6925` n `94` status `ready` deltaP `41.1495` edge `0.0237` maxDD `-3.7401`
- `risk_on_high->crypto_alt_24h` score `0.3582` n `94` status `ready` deltaP `12.1787` edge `0.6551` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.3582` n `94` status `ready` deltaP `12.1787` edge `0.6551` maxDD `-42.8959`
- `news_risk_high->commodity_4h` score `0.1799` n `61` status `ready` deltaP `6.2725` edge `0.0229` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1621` n `61` status `ready` deltaP `10.8057` edge `0.0008` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.1611` n `159` status `ready` deltaP `9.1807` edge `0.0172` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.0103` n `107` status `ready` deltaP `5.4718` edge `0.0144` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0103` n `107` status `ready` deltaP `5.4718` edge `0.0144` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0547` n `107` status `ready` deltaP `5.6984` edge `-0.0005` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0547` n `107` status `ready` deltaP `5.6984` edge `-0.0005` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
