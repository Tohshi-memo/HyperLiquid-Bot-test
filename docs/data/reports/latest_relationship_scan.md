# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T03:22:25.808088+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.8751` n `69` status `ready` deltaP `34.3523` edge `0.1288` maxDD `-0.4576`
- `market_context_high->equity_24h` score `1.7904` n `69` status `ready` deltaP `16.6515` edge `0.0591` maxDD `-0.6726`
- `market_context_high->crypto_major_24h` score `1.5606` n `69` status `ready` deltaP `2.5815` edge `0.2505` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4757` n `69` status `ready` deltaP `21.7014` edge `-0.0217` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.2219` n `101` status `ready` deltaP `13.6682` edge `0.059` maxDD `-0.864`
- `market_context_high->commodity_1h` score `-0.2738` n `109` status `ready` deltaP `0.0481` edge `0.0098` maxDD `-0.9516`
- `market_context_high->metal_4h` score `-0.3326` n `101` status `ready` deltaP `15.4205` edge `0.0102` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.358` n `109` status `ready` deltaP `-1.0575` edge `-0.0018` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.5063` n `109` status `ready` deltaP `4.0172` edge `0.0026` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.7251` n `101` status `ready` deltaP `-3.6962` edge `-0.0072` maxDD `-0.5564`
- `market_context_high->crypto_major_4h` score `-0.8711` n `101` status `ready` deltaP `1.6375` edge `-0.0018` maxDD `-4.6638`
- `market_context_high->index_1h` score `-0.9623` n `109` status `ready` deltaP `-3.9938` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->crypto_alt_1h` score `-1.1269` n `109` status `ready` deltaP `-4.7272` edge `-0.012` maxDD `-4.4101`
- `market_context_high->equity_1h` score `-1.1357` n `109` status `ready` deltaP `-5.771` edge `-0.024` maxDD `-3.3165`
- `market_context_high->crypto_major_1h` score `-1.8205` n `109` status `ready` deltaP `-4.7272` edge `-0.0198` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.9107` n `101` status `ready` deltaP `-11.0149` edge `-0.0049` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1785` n `69` status `ready` deltaP `-30.6235` edge `-0.0426` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.5041` n `101` status `ready` deltaP `-18.9371` edge `-0.1423` maxDD `-8.1221`
- `market_context_high->metal_24h` score `-5.5144` n `69` status `ready` deltaP `-23.196` edge `-0.0537` maxDD `-7.0954`
- `market_context_high->crypto_alt_4h` score `-5.8338` n `101` status `ready` deltaP `-9.3289` edge `-0.0558` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
