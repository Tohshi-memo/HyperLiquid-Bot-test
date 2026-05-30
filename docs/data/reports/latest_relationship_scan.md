# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T18:37:17.426753+00:00`
- Price records: `672`
- Market context records: `2377`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.908` n `43` status `ready` deltaP `50.2099` edge `1.5498` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.9563` n `43` status `ready` deltaP `48.5425` edge `1.2167` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2311` n `43` status `ready` deltaP `29.7925` edge `1.1021` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8886` n `43` status `ready` deltaP `19.7674` edge `0.917` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2349` n `43` status `ready` deltaP `28.1613` edge `0.5211` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.1574` n `133` status `ready` deltaP `18.4211` edge `0.8629` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.6211` n `147` status `ready` deltaP `24.0336` edge `0.4892` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.4737` n `133` status `ready` deltaP `23.7899` edge `0.3387` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3334` n `43` status `ready` deltaP `13.4448` edge `0.3967` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.5456` n `147` status `ready` deltaP `19.0943` edge `0.5194` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.4607` n `147` status `ready` deltaP `19.0943` edge `0.3054` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7326` n `43` status `ready` deltaP `32.0051` edge `0.3323` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4802` n `43` status `ready` deltaP `36.8823` edge `0.0626` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9857` n `43` status `ready` deltaP `25.4502` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6716` n `155` status `ready` deltaP `14.1028` edge `0.1647` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.5436` n `133` status `ready` deltaP `11.8186` edge `0.1016` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.4854` n `147` status `ready` deltaP `16.8097` edge `0.0943` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.2594` n `155` status `ready` deltaP `9.943` edge `0.1574` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.148` n `43` status `ready` deltaP `13.8578` edge `0.0756` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.9826` n `43` status `ready` deltaP `19.5481` edge `-0.0015` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
