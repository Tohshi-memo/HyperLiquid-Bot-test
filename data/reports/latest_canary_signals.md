# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T20:34:03.965766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `-0.1865` n `234`; crypto_major avg `-0.0686` n `8`; equity avg `0.0006` n `141`; fx avg `0.0006` n `6`; index avg `0.0046` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0414` n `935`
- 1h: commodity avg `0.0379` n `12`; crypto_alt avg `-0.4597` n `234`; crypto_major avg `-0.3357` n `8`; equity avg `-0.1971` n `141`; fx avg `0.0046` n `6`; index avg `-0.0026` n `26`; metal avg `0.0189` n `20`; unknown avg `1.3352` n `861`
- 4h: commodity avg `0.1703` n `12`; crypto_alt avg `-0.9982` n `234`; crypto_major avg `-0.2882` n `8`; equity avg `-0.3749` n `141`; fx avg `-0.0083` n `6`; index avg `-0.0294` n `26`; metal avg `-0.0281` n `20`; unknown avg `3.3859` n `853`
- 24h: commodity avg `0.6432` n `12`; crypto_alt avg `-3.9375` n `234`; crypto_major avg `-3.6443` n `8`; equity avg `-1.6318` n `140`; fx avg `0.0263` n `6`; index avg `-0.3552` n `26`; metal avg `-0.8403` n `20`; unknown avg `575.1343` n `836`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
