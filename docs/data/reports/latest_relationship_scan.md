# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T17:37:28.670654+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.169` n `51` status `ready` deltaP `13.3681` edge `3.7583` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2403` n `51` status `ready` deltaP `40.237` edge `0.9282` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8619` n `51` status `ready` deltaP `24.2587` edge `0.9147` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4388` n `51` status `ready` deltaP `48.9481` edge `0.1421` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.8884` n `88` status `ready` deltaP `7.6863` edge `0.3854` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.076` n `51` status `ready` deltaP `27.8426` edge `0.2311` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.561` n `51` status `ready` deltaP `16.3349` edge `0.2183` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3394` n `51` status `ready` deltaP `39.3024` edge `0.0297` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6574` n `130` status `ready` deltaP `19.2964` edge `0.0503` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2949` n `51` status `ready` deltaP `17.5942` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0735` n `51` status `ready` deltaP `15.0735` edge `0.0287` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0068` n `51` status `ready` deltaP `18.6421` edge `0.0412` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.6785` n `51` status `ready` deltaP `27.2059` edge `-0.1206` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2902` n `51` status `ready` deltaP `9.2873` edge `-0.0069` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `8.9732` edge `0.0052` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1208` n `130` status `ready` deltaP `10.8678` edge `-0.0165` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0181` n `130` status `ready` deltaP `10.9051` edge `-0.0263` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1146` n `51` status `ready` deltaP `2.1927` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3053` n `51` status `ready` deltaP `5.996` edge `-0.0123` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3991` n `130` status `ready` deltaP `3.1598` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
