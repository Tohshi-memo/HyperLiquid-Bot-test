# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T10:35:59.270112+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `195.898` n `88` status `ready` deltaP `-21.512` edge `25.5269` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `13.4041` n `34` status `ready` deltaP `22.2733` edge `1.0011` maxDD `-0.9396`
- `news_risk_high->equity_4h` score `7.6852` n `34` status `ready` deltaP `36.8902` edge `0.3945` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5001` n `88` status `ready` deltaP `41.3037` edge `0.3554` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.7776` n `34` status `ready` deltaP `30.5556` edge `0.1111` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.9262` n `112` status `ready` deltaP `18.1838` edge `0.0864` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8406` n `34` status `ready` deltaP `20.9648` edge `0.0268` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.8252` n `34` status `ready` deltaP `8.216` edge `0.1292` maxDD `-0.5496`
- `news_risk_high->fx_4h` score `0.1467` n `34` status `ready` deltaP `7.0839` edge `-0.0065` maxDD `-0.0863`
- `news_risk_high->index_1h` score `0.0866` n `34` status `ready` deltaP `2.2367` edge `0.0149` maxDD `-0.141`
- `market_context_high->commodity_1h` score `-0.008` n `124` status `ready` deltaP `2.9506` edge `0.0208` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.0596` n `112` status `ready` deltaP `6.6637` edge `0.0084` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.1492` n `124` status `ready` deltaP `1.13` edge `0.0015` maxDD `-0.2527`
- `news_risk_high->fx_1h` score `-0.2106` n `34` status `ready` deltaP `0.8454` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5556` n `124` status `ready` deltaP `0.9803` edge `-0.0062` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.565` n `34` status `ready` deltaP `-5.1867` edge `-0.011` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7728` n `124` status `ready` deltaP `-6.5868` edge `-0.003` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0575` n `34` status `ready` deltaP `-2.439` edge `-0.03` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.0805` n `34` status `ready` deltaP `-5.6358` edge `-0.0217` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.1558` n `112` status `ready` deltaP `3.811` edge `-0.0162` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
