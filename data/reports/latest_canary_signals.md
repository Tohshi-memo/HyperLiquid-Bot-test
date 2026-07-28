# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T20:37:57.098555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.1555` n `230`; crypto_major avg `-0.1323` n `8`; equity avg `0.0382` n `102`; fx avg `-0.0089` n `6`; index avg `0.0382` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0345` n `776`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.1105` n `230`; crypto_major avg `0.0176` n `8`; equity avg `0.4593` n `102`; fx avg `-0.0138` n `6`; index avg `-0.0149` n `25`; metal avg `-0.015` n `20`; unknown avg `0.9794` n `776`
- 4h: commodity avg `0.2069` n `12`; crypto_alt avg `-0.3092` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `0.6321` n `102`; fx avg `-0.0179` n `6`; index avg `-0.0894` n `25`; metal avg `-0.1682` n `20`; unknown avg `0.7791` n `774`
- 24h: commodity avg `-0.8715` n `12`; crypto_alt avg `-2.2099` n `230`; crypto_major avg `-1.8252` n `8`; equity avg `-2.8816` n `102`; fx avg `-0.0987` n `6`; index avg `-0.4154` n `25`; metal avg `-0.4342` n `20`; unknown avg `1.0561` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
