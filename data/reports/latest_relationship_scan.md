# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T08:52:30.720432+00:00`
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

- `news_risk_high->unknown_24h` score `43.7138` n `51` status `ready` deltaP `2.7778` edge `3.6243` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.929` n `51` status `ready` deltaP `25.1733` edge `0.9142` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.302` n `51` status `ready` deltaP `37.6328` edge `0.7007` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.7879` n `51` status `ready` deltaP `46.6912` edge `0.1029` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.1033` n `51` status `ready` deltaP `36.7109` edge `0.0273` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0818` n `52` status `ready` deltaP `15.35` edge `0.1898` maxDD `-0.8252`
- `news_risk_high->equity_4h` score `2.6741` n `51` status `ready` deltaP `23.8791` edge `0.1407` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9349` n `133` status `ready` deltaP `19.6153` edge `0.0713` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.033` n `52` status `ready` deltaP `14.4404` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7798` n `52` status `ready` deltaP `16.9622` edge `0.0233` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.507` n `51` status `ready` deltaP `10.3479` edge `0.013` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.1955` n `52` status `ready` deltaP `8.5675` edge `-0.0097` maxDD `-0.4898`
- `news_risk_high->index_1h` score `0.0619` n `52` status `ready` deltaP `6.1723` edge `0.0021` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0005` n `133` status `ready` deltaP `11.2725` edge `-0.0303` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2909` n `51` status `ready` deltaP `5.996` edge `-0.0111` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4129` n `52` status `ready` deltaP `-0.4721` edge `-0.0088` maxDD `-0.13`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.6006` edge `-0.0003` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6432` n `51` status `ready` deltaP `21.6503` edge `-0.1937` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6787` n `133` status `ready` deltaP `6.2466` edge `-0.0345` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1412` n `133` status `ready` deltaP `-5.3228` edge `-0.0058` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
