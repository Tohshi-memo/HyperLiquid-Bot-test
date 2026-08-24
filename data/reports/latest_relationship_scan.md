# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T17:07:24.098446+00:00`
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

- `news_risk_high->unknown_24h` score `46.3468` n `51` status `ready` deltaP `13.7153` edge `3.7708` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.3207` n `51` status `ready` deltaP `40.237` edge `0.9349` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8691` n `51` status `ready` deltaP `24.2587` edge `0.9153` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4556` n `51` status `ready` deltaP `48.9481` edge `0.1435` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.9284` n `86` status `ready` deltaP `7.9013` edge `0.3873` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.1002` n `51` status `ready` deltaP `27.995` edge `0.2321` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5778` n `51` status `ready` deltaP `16.4846` edge `0.2187` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3394` n `51` status `ready` deltaP `39.3024` edge `0.0297` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6646` n `130` status `ready` deltaP `19.2964` edge `0.0509` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2949` n `51` status `ready` deltaP `17.5942` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0747` n `51` status `ready` deltaP `15.0735` edge `0.0288` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0044` n `51` status `ready` deltaP `18.6421` edge `0.0409` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.7375` n `51` status `ready` deltaP `27.5531` edge `-0.118` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2566` n `51` status `ready` deltaP `8.9879` edge `-0.0077` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2325` n `51` status `ready` deltaP `8.9732` edge `0.0053` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1172` n `130` status `ready` deltaP `10.8678` edge `-0.0168` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0348` n `130` status `ready` deltaP `11.0548` edge `-0.0259` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1154` n `51` status `ready` deltaP `2.1927` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3089` n `51` status `ready` deltaP `5.996` edge `-0.0126` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3991` n `130` status `ready` deltaP `3.1598` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
