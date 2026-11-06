# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T15:07:29.849547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3928`

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

- `news_risk_high->equity_24h` score `0.9807` n `110` status `ready` deltaP `28.1347` edge `1.0968` maxDD `-86.0244`
- `news_risk_high->equity_4h` score `0.9724` n `110` status `ready` deltaP `12.8742` edge `0.2012` maxDD `-9.9884`
- `news_risk_high->index_4h` score `0.5367` n `110` status `ready` deltaP `12.2644` edge `0.0189` maxDD `-1.142`
- `news_risk_high->index_24h` score `-0.3345` n `110` status `ready` deltaP `0.3901` edge `0.138` maxDD `-6.6786`
- `news_risk_high->index_1h` score `-0.3606` n `110` status `ready` deltaP `6.1813` edge `0.0022` maxDD `-0.8765`
- `news_risk_high->fx_1h` score `-0.4898` n `110` status `ready` deltaP `-0.2449` edge `0.0008` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.6046` n `110` status `ready` deltaP `2.0958` edge `0.0313` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.8478` n `110` status `ready` deltaP `1.5078` edge `0.1449` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.8638` n `110` status `ready` deltaP `-1.9679` edge `-0.0085` maxDD `-1.0293`
- `news_risk_high->crypto_major_1h` score `-0.8732` n `110` status `ready` deltaP `-2.6102` edge `0.006` maxDD `-4.7103`
- `news_risk_high->equity_1h` score `-0.9458` n `110` status `ready` deltaP `0.7594` edge `0.0345` maxDD `-7.8651`
- `news_risk_high->crypto_major_4h` score `-1.0587` n `110` status `ready` deltaP `-2.2533` edge `0.0604` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.0939` n `110` status `ready` deltaP `-1.2639` edge `-0.0018` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.1817` n `110` status `ready` deltaP `-13.2683` edge `0.0004` maxDD `-0.4086`
- `news_risk_high->metal_4h` score `-1.8514` n `110` status `ready` deltaP `-3.5172` edge `-0.0382` maxDD `-1.7443`
- `news_risk_high->commodity_1h` score `-2.9294` n `110` status `ready` deltaP `-14.8449` edge `-0.0085` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.0896` n `110` status `ready` deltaP `0.0598` edge `-0.2069` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.3379` n `110` status `ready` deltaP `-27.1037` edge `-0.0287` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0297` n `110` status `ready` deltaP `-15.9767` edge `0.1838` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3473` n `110` status `ready` deltaP `-24.4322` edge `-0.0088` maxDD `-37.9143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
