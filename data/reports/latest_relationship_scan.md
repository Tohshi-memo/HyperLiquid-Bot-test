# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T14:52:28.635755+00:00`
- Price records: `672`
- Market context records: `8206`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8161.9635` n `43` status `ready` deltaP `36.9792` edge `679.9171` maxDD `0.0`
- `market_context_high->equity_24h` score `22.6192` n `35` status `ready` deltaP `43.1944` edge `1.688` maxDD `-4.9489`
- `market_context_high->crypto_alt_24h` score `14.7021` n `35` status `ready` deltaP `26.9196` edge `1.1573` maxDD `-4.5937`
- `market_context_high->equity_4h` score `9.0864` n `36` status `ready` deltaP `46.9173` edge `0.4487` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.8936` n `35` status `ready` deltaP `47.5694` edge `0.424` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `8.7334` n `35` status `ready` deltaP `26.3988` edge `1.1347` maxDD `-10.949`
- `news_risk_high->equity_4h` score `7.1557` n `54` status `ready` deltaP `25.621` edge `0.4852` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `4.0694` n `36` status `ready` deltaP `18.3096` edge `0.2903` maxDD `-2.8595`
- `market_context_high->index_4h` score `3.8955` n `36` status `ready` deltaP `38.1606` edge `0.0745` maxDD `-0.0092`
- `market_context_high->crypto_alt_4h` score `3.8948` n `36` status `ready` deltaP `15.6843` edge `0.2496` maxDD `-0.7011`
- `market_context_high->metal_4h` score `3.7299` n `36` status `ready` deltaP `36.9072` edge `0.0826` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.2165` n `54` status `ready` deltaP `22.7268` edge `0.1474` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.1855` n `35` status `ready` deltaP `29.9504` edge `0.2707` maxDD `-0.9576`
- `market_context_high->equity_1h` score `2.9194` n `36` status `ready` deltaP `15.3194` edge `0.1558` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `2.6967` n `54` status `ready` deltaP `13.68` edge `0.3239` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6785` n `54` status `ready` deltaP `22.4198` edge `0.0928` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `1.9805` n `54` status `ready` deltaP `13.4509` edge `0.1151` maxDD `-1.1783`
- `market_context_high->fx_24h` score `1.9155` n `35` status `ready` deltaP `34.9057` edge `0.0733` maxDD `-0.5004`
- `news_risk_high->crypto_alt_1h` score `1.871` n `54` status `ready` deltaP `15.0033` edge `0.0993` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4549` n `54` status `ready` deltaP `17.5362` edge `0.2088` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
