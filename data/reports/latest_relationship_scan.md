# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T03:07:25.995475+00:00`
- Price records: `672`
- Market context records: `5940`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11219`

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

- `news_risk_high->fx_24h` score `6.7498` n `30` status `ready` deltaP `61.6319` edge `0.1516` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4932` n `30` status `ready` deltaP `39.2709` edge `0.2165` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6545` n `30` status `ready` deltaP `37.8659` edge `0.0567` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1028` n `30` status `ready` deltaP `25.4291` edge `0.0196` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4459` n `221` status `ready` deltaP `10.2804` edge `0.1614` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.887` n `30` status `ready` deltaP `10.9381` edge `0.0875` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2216` n `30` status `ready` deltaP `5.4691` edge `0.0381` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.074` n `222` status `ready` deltaP `6.3185` edge `0.0404` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.266` n `30` status `ready` deltaP `6.4583` edge `0.01` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3123` n `222` status `ready` deltaP `3.7587` edge `0.002` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4321` n `30` status `ready` deltaP `1.6866` edge `-0.03` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5309` n `222` status `ready` deltaP `1.6521` edge `0.0057` maxDD `-0.7819`
- `market_context_high->commodity_1h` score `-0.5724` n `222` status `ready` deltaP `-2.8551` edge `-0.0028` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6324` n `222` status `ready` deltaP `3.4607` edge `0.0314` maxDD `-6.5102`
- `market_context_high->crypto_alt_1h` score `-0.6786` n `222` status `ready` deltaP `2.8565` edge `0.0274` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7153` n `222` status `ready` deltaP `-1.5078` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->equity_24h` score `-1.0897` n `213` status `ready` deltaP `17.8379` edge `0.249` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0952` n `30` status `ready` deltaP `-10.1497` edge `-0.0213` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.721` n `221` status `ready` deltaP `-3.166` edge `-0.0363` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.7321` n `221` status `ready` deltaP `1.0926` edge `0.0171` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
