# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T03:22:39.995875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.09` n `230`; crypto_major avg `-0.1044` n `8`; equity avg `-0.1558` n `102`; fx avg `0.0082` n `6`; index avg `-0.0232` n `25`; metal avg `-0.0362` n `20`; unknown avg `0.0562` n `777`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0696` n `230`; crypto_major avg `0.0295` n `8`; equity avg `-0.3411` n `102`; fx avg `0.0023` n `6`; index avg `-0.0949` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.016` n `777`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.5746` n `230`; crypto_major avg `0.3877` n `8`; equity avg `-0.6916` n `102`; fx avg `-0.0052` n `6`; index avg `-0.3516` n `25`; metal avg `0.0567` n `20`; unknown avg `3.1052` n `776`
- 24h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.8363` n `230`; crypto_major avg `0.386` n `8`; equity avg `-2.3896` n `102`; fx avg `-0.0982` n `6`; index avg `-0.472` n `25`; metal avg `-0.1201` n `20`; unknown avg `0.4689` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
