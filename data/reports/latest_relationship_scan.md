# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T01:52:30.351216+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `80.8966` n `88` status `ready` deltaP `7.525` edge `6.736` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.7845` n `88` status `ready` deltaP `33.1281` edge `2.917` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `8.4278` n `30` status `ready` deltaP `30.1524` edge `0.6135` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.3` n `88` status `ready` deltaP `31.5499` edge `1.235` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1269` n `88` status `ready` deltaP `31.8497` edge `0.3445` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.7472` n `39` status `ready` deltaP `18.7817` edge `0.2583` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.0391` n `30` status `ready` deltaP `18.7805` edge `0.1534` maxDD `-0.3611`
- `market_context_high->metal_24h` score `2.824` n `88` status `ready` deltaP `27.036` edge `0.1104` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `1.5605` n `30` status `ready` deltaP `17.9268` edge `0.2293` maxDD `-9.2335`
- `news_risk_high->index_1h` score `1.4374` n `39` status `ready` deltaP `18.7817` edge `0.0247` maxDD `-0.4103`
- `news_risk_high->crypto_alt_4h` score `1.3028` n `30` status `ready` deltaP `24.8984` edge `0.1649` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.1385` n `39` status `ready` deltaP `15.9182` edge `0.0142` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.1091` n `30` status `ready` deltaP `20.1321` edge `0.0516` maxDD `-0.8235`
- `news_risk_high->metal_4h` score `1.0955` n `30` status `ready` deltaP `26.6667` edge `0.0003` maxDD `-1.0104`
- `news_risk_high->crypto_alt_1h` score `1.017` n `39` status `ready` deltaP `22.6739` edge `0.073` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6972` n `39` status `ready` deltaP `22.6739` edge `0.0434` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.3144` n `39` status `ready` deltaP `-6.5408` edge `0.0365` maxDD `-0.3228`
- `market_context_high->metal_1h` score `-0.3629` n `88` status `ready` deltaP `3.797` edge `0.0121` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3747` n `88` status `ready` deltaP `2.9872` edge `0.0003` maxDD `-1.7935`
- `news_risk_high->fx_1h` score `-0.5835` n `39` status `ready` deltaP `-2.0306` edge `-0.0059` maxDD `-0.3348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
