# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T03:07:28.346914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7640`

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

- `market_context_high->unknown_4h` score `53.0277` n `95` status `ready` deltaP `0.8408` edge `4.4469` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.5655` n `107` status `ready` deltaP `2.1574` edge `1.4983` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.4045` n `46` status `ready` deltaP `18.6971` edge `0.0833` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `-0.0453` n `95` status `ready` deltaP `3.888` edge `0.0432` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2906` n `107` status `ready` deltaP `2.3323` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3746` n `107` status `ready` deltaP `-2.1826` edge `0.002` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.6172` n `95` status `ready` deltaP `-3.5976` edge `0.0047` maxDD `-0.4541`
- `market_context_high->index_1h` score `-0.6183` n `107` status `ready` deltaP `-1.2116` edge `-0.006` maxDD `-1.2155`
- `market_context_high->crypto_major_24h` score `-0.6394` n `46` status `ready` deltaP `9.5713` edge `0.0514` maxDD `-11.1077`
- `market_context_high->metal_1h` score `-0.8563` n `107` status `ready` deltaP `1.9685` edge `-0.0053` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.8988` n `46` status `ready` deltaP `0.2265` edge `0.0007` maxDD `-1.1691`
- `market_context_high->crypto_major_1h` score `-1.0638` n `107` status `ready` deltaP `5.399` edge `-0.0143` maxDD `-9.3126`
- `market_context_high->crypto_alt_24h` score `-1.7467` n `46` status `ready` deltaP `12.6057` edge `0.1076` maxDD `-28.9123`
- `market_context_high->equity_1h` score `-2.4918` n `107` status `ready` deltaP `-0.3498` edge `-0.0898` maxDD `-12.1865`
- `market_context_high->metal_4h` score `-2.617` n `95` status `ready` deltaP `-2.001` edge `-0.0288` maxDD `-5.742`
- `market_context_high->metal_24h` score `-2.7925` n `46` status `ready` deltaP `-8.1295` edge `-0.0075` maxDD `-6.6809`
- `market_context_high->crypto_alt_1h` score `-2.8511` n `107` status `ready` deltaP `-0.277` edge `-0.0513` maxDD `-11.7553`
- `market_context_high->index_4h` score `-4.1246` n `95` status `ready` deltaP `-15.3723` edge `-0.048` maxDD `-4.7923`
- `market_context_high->index_24h` score `-7.1046` n `46` status `ready` deltaP `-35.8243` edge `-0.1864` maxDD `-6.0121`
- `market_context_high->crypto_major_4h` score `-10.7918` n `95` status `ready` deltaP `-15.5248` edge `-0.2383` maxDD `-37.935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
