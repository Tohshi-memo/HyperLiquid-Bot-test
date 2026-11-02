# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T00:07:29.565641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7065`

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

- `market_context_high->unknown_24h` score `7604.8411` n `55` status `ready` deltaP `1.3889` edge `633.7275` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.565` n `55` status `ready` deltaP `7.1757` edge `27.5869` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `37.2458` n `55` status `ready` deltaP `4.3604` edge `3.0858` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2992` n `55` status `ready` deltaP `42.7999` edge `1.5132` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.3496` n `94` status `ready` deltaP `31.4827` edge `1.0382` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.171` n `55` status `ready` deltaP `49.1319` edge `0.1867` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0603` n `55` status `ready` deltaP `23.9024` edge `0.3751` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.871` n `55` status `ready` deltaP `40.5808` edge `0.2498` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.4985` n `55` status `ready` deltaP `30.7401` edge `0.2869` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.235` n `55` status `ready` deltaP `5.7428` edge `0.3015` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0438` n `55` status `ready` deltaP `29.2378` edge `0.0838` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.3966` n `55` status `ready` deltaP `10.3378` edge `0.306` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.3823` n `126` status `ready` deltaP `9.7754` edge `0.272` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `1.9876` n `55` status `ready` deltaP `-3.7784` edge `0.4318` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7555` n `55` status `ready` deltaP `20.6374` edge `0.0512` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5201` n `55` status `ready` deltaP `3.1764` edge `0.158` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.3884` n `55` status `ready` deltaP `3.6255` edge `0.1586` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.3844` n `55` status `ready` deltaP `8.0321` edge `0.1228` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9558` n `55` status `ready` deltaP `11.9243` edge `0.025` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5646` n `55` status `ready` deltaP `13.6364` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
