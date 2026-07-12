# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T08:22:28.590450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.0502` n `230`; crypto_major avg `0.0732` n `8`; equity avg `0.0024` n `92`; fx avg `0.0046` n `6`; index avg `0.0004` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.9611` n `765`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.1026` n `230`; crypto_major avg `0.1698` n `8`; equity avg `0.0073` n `92`; fx avg `0.006` n `6`; index avg `0.0312` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.1343` n `765`
- 4h: commodity avg `0.0527` n `12`; crypto_alt avg `-0.4071` n `230`; crypto_major avg `-0.1908` n `8`; equity avg `-0.1528` n `92`; fx avg `0.0054` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.2839` n `747`
- 24h: commodity avg `0.4565` n `12`; crypto_alt avg `-0.5827` n `230`; crypto_major avg `-0.5417` n `8`; equity avg `-0.1951` n `92`; fx avg `0.0043` n `6`; index avg `-0.119` n `25`; metal avg `-0.1076` n `20`; unknown avg `-0.0114` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
