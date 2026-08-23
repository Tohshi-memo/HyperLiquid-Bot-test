# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T11:07:27.573247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.2034` n `230`; crypto_major avg `0.0989` n `8`; equity avg `0.0363` n `121`; fx avg `0.0007` n `6`; index avg `0.0051` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.1589` n `795`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.6696` n `230`; crypto_major avg `0.2475` n `8`; equity avg `0.0413` n `121`; fx avg `-0.0129` n `6`; index avg `0.007` n `25`; metal avg `0.0143` n `20`; unknown avg `0.2161` n `794`
- 4h: commodity avg `-0.0162` n `12`; crypto_alt avg `2.4177` n `230`; crypto_major avg `1.1828` n `8`; equity avg `0.2879` n `121`; fx avg `-0.0554` n `6`; index avg `0.0449` n `25`; metal avg `0.0075` n `20`; unknown avg `0.4572` n `794`
- 24h: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0216` n `230`; crypto_major avg `0.7226` n `8`; equity avg `0.4177` n `121`; fx avg `0.03` n `6`; index avg `0.0417` n `25`; metal avg `0.0642` n `20`; unknown avg `2.8202` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
