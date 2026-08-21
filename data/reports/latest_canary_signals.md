# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T03:26:04.916204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `0.1946` n `230`; crypto_major avg `0.331` n `8`; equity avg `0.0041` n `121`; fx avg `0.0089` n `6`; index avg `0.0036` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.5066` n `793`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `0.0047` n `230`; crypto_major avg `-0.2928` n `8`; equity avg `-0.0901` n `121`; fx avg `0.0117` n `6`; index avg `0.0001` n `25`; metal avg `0.0491` n `20`; unknown avg `1.178` n `793`
- 4h: commodity avg `0.0207` n `12`; crypto_alt avg `0.869` n `230`; crypto_major avg `0.9931` n `8`; equity avg `0.7391` n `121`; fx avg `-0.1214` n `6`; index avg `0.1325` n `25`; metal avg `0.1831` n `20`; unknown avg `0.0551` n `793`
- 24h: commodity avg `0.3338` n `12`; crypto_alt avg `5.8017` n `230`; crypto_major avg `7.0758` n `8`; equity avg `-0.3674` n `121`; fx avg `-0.0248` n `6`; index avg `-0.0845` n `25`; metal avg `0.5015` n `20`; unknown avg `2.5898` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
