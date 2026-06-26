# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T01:52:31.282385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.052` n `12`; crypto_alt avg `0.0783` n `228`; crypto_major avg `0.1874` n `8`; equity avg `-0.046` n `86`; fx avg `-0.0147` n `6`; index avg `-0.0433` n `23`; metal avg `-0.1152` n `20`; unknown avg `4.6419` n `765`
- 1h: commodity avg `-0.097` n `12`; crypto_alt avg `-0.5869` n `228`; crypto_major avg `-0.68` n `8`; equity avg `-0.5325` n `86`; fx avg `-0.0045` n `6`; index avg `-0.1182` n `23`; metal avg `-0.3086` n `20`; unknown avg `-0.7994` n `765`
- 4h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.5908` n `228`; crypto_major avg `-0.6516` n `8`; equity avg `-0.9732` n `86`; fx avg `0.0151` n `6`; index avg `-0.2302` n `23`; metal avg `-0.3649` n `20`; unknown avg `-0.6194` n `749`
- 24h: commodity avg `0.4619` n `12`; crypto_alt avg `-1.7422` n `228`; crypto_major avg `-1.9534` n `8`; equity avg `-2.9711` n `86`; fx avg `0.0255` n `6`; index avg `-0.3698` n `23`; metal avg `0.1539` n `20`; unknown avg `0.4921` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
