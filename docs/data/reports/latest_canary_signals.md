# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T12:37:32.266454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0238` n `234`; crypto_major avg `0.103` n `8`; equity avg `-0.0017` n `141`; fx avg `0.0039` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.1347` n `962`
- 1h: commodity avg `-0.0154` n `12`; crypto_alt avg `0.122` n `234`; crypto_major avg `0.3103` n `8`; equity avg `0.0264` n `141`; fx avg `0.007` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0042` n `20`; unknown avg `1.7268` n `954`
- 4h: commodity avg `0.0422` n `12`; crypto_alt avg `-0.0886` n `234`; crypto_major avg `0.1439` n `8`; equity avg `0.0241` n `141`; fx avg `-0.0041` n `6`; index avg `-0.014` n `26`; metal avg `-0.0112` n `20`; unknown avg `1.9649` n `953`
- 24h: commodity avg `0.0413` n `12`; crypto_alt avg `1.0264` n `234`; crypto_major avg `1.0722` n `8`; equity avg `0.3775` n `141`; fx avg `-0.0261` n `6`; index avg `0.0285` n `26`; metal avg `-0.0074` n `20`; unknown avg `60.9052` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
