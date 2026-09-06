# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T18:37:24.593455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10185`

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

- `risk_on_high->unknown_24h` score `219.3657` n `103` status `ready` deltaP `25.2124` edge `18.1223` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `219.3657` n `103` status `ready` deltaP `25.2124` edge `18.1223` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `18.9076` n `103` status `ready` deltaP `32.376` edge `1.4705` maxDD `-6.5235`
- `risk_on_and_context->crypto_major_24h` score `18.9076` n `103` status `ready` deltaP `32.376` edge `1.4705` maxDD `-6.5235`
- `risk_on_high->crypto_alt_24h` score `9.9707` n `103` status `ready` deltaP `21.7857` edge `0.8223` maxDD `-7.5986`
- `risk_on_and_context->crypto_alt_24h` score `9.9707` n `103` status `ready` deltaP `21.7857` edge `0.8223` maxDD `-7.5986`
- `market_context_high->crypto_alt_24h` score `5.9571` n `196` status `ready` deltaP `19.2` edge `0.5304` maxDD `-8.958`
- `market_context_high->equity_24h` score `5.6853` n `196` status `ready` deltaP `20.7342` edge `0.3924` maxDD `-2.2147`
- `risk_on_high->equity_24h` score `4.4818` n `103` status `ready` deltaP `17.5095` edge `0.3136` maxDD `-2.2147`
- `risk_on_and_context->equity_24h` score `4.4818` n `103` status `ready` deltaP `17.5095` edge `0.3136` maxDD `-2.2147`
- `risk_on_high->index_24h` score `1.2452` n `103` status `ready` deltaP `16.3009` edge `0.0694` maxDD `-1.9448`
- `risk_on_and_context->index_24h` score `1.2452` n `103` status `ready` deltaP `16.3009` edge `0.0694` maxDD `-1.9448`
- `market_context_high->index_24h` score `1.2401` n `196` status `ready` deltaP `18.2575` edge `0.0873` maxDD `-2.4542`
- `risk_on_high->metal_24h` score `0.1613` n `103` status `ready` deltaP `14.7013` edge `0.0755` maxDD `-6.1387`
- `risk_on_and_context->metal_24h` score `0.1613` n `103` status `ready` deltaP `14.7013` edge `0.0755` maxDD `-6.1387`
- `risk_on_high->index_1h` score `0.0398` n `129` status `ready` deltaP `7.9202` edge `-0.003` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0398` n `129` status `ready` deltaP `7.9202` edge `-0.003` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1181` n `129` status `ready` deltaP `3.2261` edge `0.0619` maxDD `-5.1264`
- `risk_on_and_context->crypto_alt_1h` score `-0.1181` n `129` status `ready` deltaP `3.2261` edge `0.0619` maxDD `-5.1264`
- `risk_on_high->metal_1h` score `-0.1989` n `129` status `ready` deltaP `6.4824` edge `-0.0025` maxDD `-1.6309`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
