# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T19:37:28.319902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0578` n `12`; crypto_alt avg `-0.0205` n `234`; crypto_major avg `0.0656` n `8`; equity avg `0.0258` n `141`; fx avg `-0.0034` n `6`; index avg `0.0079` n `26`; metal avg `-0.0136` n `20`; unknown avg `15.184` n `943`
- 1h: commodity avg `0.0469` n `12`; crypto_alt avg `0.1811` n `234`; crypto_major avg `0.4143` n `8`; equity avg `-0.0548` n `141`; fx avg `-0.0003` n `6`; index avg `0.001` n `26`; metal avg `-0.0311` n `20`; unknown avg `12.104` n `941`
- 4h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.6397` n `234`; crypto_major avg `-0.1754` n `8`; equity avg `-0.335` n `141`; fx avg `-0.0359` n `6`; index avg `-0.0485` n `26`; metal avg `0.0088` n `20`; unknown avg `14.7908` n `919`
- 24h: commodity avg `0.8053` n `12`; crypto_alt avg `-3.1023` n `234`; crypto_major avg `-3.2719` n `8`; equity avg `-1.4712` n `140`; fx avg `-0.0153` n `6`; index avg `-0.3976` n `26`; metal avg `-0.9623` n `20`; unknown avg `20.1942` n `878`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
