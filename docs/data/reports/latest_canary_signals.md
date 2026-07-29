# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T13:22:28.801405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `-0.0104` n `230`; crypto_major avg `-0.0841` n `8`; equity avg `-0.1051` n `102`; fx avg `0.0045` n `6`; index avg `-0.0132` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0099` n `777`
- 1h: commodity avg `-0.0361` n `12`; crypto_alt avg `-0.0808` n `230`; crypto_major avg `-0.0536` n `8`; equity avg `0.0465` n `102`; fx avg `0.0024` n `6`; index avg `0.0542` n `25`; metal avg `0.1242` n `20`; unknown avg `0.0763` n `777`
- 4h: commodity avg `0.4611` n `12`; crypto_alt avg `-0.5896` n `230`; crypto_major avg `-0.4792` n `8`; equity avg `-0.5275` n `102`; fx avg `-0.0127` n `6`; index avg `-0.0347` n `25`; metal avg `-0.153` n `20`; unknown avg `0.6233` n `777`
- 24h: commodity avg `0.4245` n `12`; crypto_alt avg `-1.5864` n `230`; crypto_major avg `0.8627` n `8`; equity avg `-0.7925` n `102`; fx avg `-0.0827` n `6`; index avg `-0.1713` n `25`; metal avg `-0.1368` n `20`; unknown avg `0.069` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
