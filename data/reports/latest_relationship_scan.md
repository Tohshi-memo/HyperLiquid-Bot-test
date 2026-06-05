# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T15:52:25.991176+00:00`
- Price records: `672`
- Market context records: `2983`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `15.7331` n `100` status `ready` deltaP `5.3194` edge `1.6673` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.4149` n `100` status `ready` deltaP `40.3542` edge `0.7003` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `10.8494` n `100` status `ready` deltaP `16.8125` edge `0.8385` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7628` n `100` status `ready` deltaP `15.4861` edge `0.6607` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.2764` n `100` status `ready` deltaP `15.5764` edge `0.3506` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0443` n `101` status `ready` deltaP `14.8847` edge `0.1934` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.1937` n `101` status `ready` deltaP `19.6118` edge `0.1309` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.1272` n `101` status `ready` deltaP `16.4075` edge `0.1326` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.7107` n `101` status `ready` deltaP `23.1224` edge `0.3931` maxDD `-30.8239`
- `market_context_high->equity_1h` score `0.503` n `103` status `ready` deltaP `6.1523` edge `0.0509` maxDD `-2.3332`
- `market_context_high->index_1h` score `0.5025` n `103` status `ready` deltaP `7.6536` edge `0.0321` maxDD `-0.9667`
- `market_context_high->commodity_1h` score `-0.1539` n `103` status `ready` deltaP `-0.1904` edge `0.0141` maxDD `-0.9378`
- `market_context_high->fx_1h` score `-0.4675` n `103` status `ready` deltaP `-1.4607` edge `0.0015` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.5159` n `103` status `ready` deltaP `8.5518` edge `0.0635` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.633` n `103` status `ready` deltaP `6.9909` edge `0.0349` maxDD `-10.3462`
- `market_context_high->fx_4h` score `-1.0095` n `101` status `ready` deltaP `-7.883` edge `0.001` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.3368` n `101` status `ready` deltaP `-1.0294` edge `0.0008` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.3801` n `103` status `ready` deltaP `-1.8967` edge `0.0001` maxDD `-4.5307`
- `market_context_high->unknown_1h` score `-1.5988` n `103` status `ready` deltaP `2.2731` edge `-0.0753` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-2.0729` n `101` status `ready` deltaP `8.6528` edge `0.1891` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
