# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T05:22:35.031714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.1838` n `228`; crypto_major avg `-0.1017` n `8`; equity avg `-0.0052` n `74`; fx avg `0.0016` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0026` n `18`; unknown avg `-0.1055` n `645`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.6921` n `228`; crypto_major avg `-0.3937` n `8`; equity avg `-0.0539` n `74`; fx avg `0.0079` n `6`; index avg `-0.0279` n `23`; metal avg `0.0006` n `18`; unknown avg `-0.1705` n `645`
- 4h: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.8076` n `228`; crypto_major avg `-0.6624` n `8`; equity avg `-0.0033` n `74`; fx avg `-0.0042` n `6`; index avg `-0.0649` n `23`; metal avg `-0.0133` n `18`; unknown avg `-1.267` n `629`
- 24h: commodity avg `-0.7576` n `12`; crypto_alt avg `1.2057` n `228`; crypto_major avg `1.66` n `8`; equity avg `0.7413` n `74`; fx avg `-0.0302` n `6`; index avg `0.2008` n `23`; metal avg `0.3251` n `18`; unknown avg `-1.1481` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
