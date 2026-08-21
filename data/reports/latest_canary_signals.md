# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T00:52:23.289826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.1604` n `230`; crypto_major avg `0.3424` n `8`; equity avg `0.3158` n `121`; fx avg `0.0202` n `6`; index avg `0.0608` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.1881` n `793`
- 1h: commodity avg `0.0283` n `12`; crypto_alt avg `0.1655` n `230`; crypto_major avg `0.4878` n `8`; equity avg `0.6272` n `121`; fx avg `-0.0458` n `6`; index avg `0.1326` n `25`; metal avg `-0.0497` n `20`; unknown avg `-0.0753` n `793`
- 4h: commodity avg `0.0175` n `12`; crypto_alt avg `0.9661` n `230`; crypto_major avg `1.1607` n `8`; equity avg `0.5947` n `121`; fx avg `-0.0655` n `6`; index avg `0.0887` n `25`; metal avg `0.0406` n `20`; unknown avg `-0.3824` n `793`
- 24h: commodity avg `0.3232` n `12`; crypto_alt avg `4.5153` n `230`; crypto_major avg `5.6089` n `8`; equity avg `-0.7678` n `121`; fx avg `0.0588` n `6`; index avg `-0.0986` n `25`; metal avg `0.1757` n `20`; unknown avg `2.5217` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
