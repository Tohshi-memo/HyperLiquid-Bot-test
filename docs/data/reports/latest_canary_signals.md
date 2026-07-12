# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T23:22:32.246681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.0735` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0677` n `92`; fx avg `0.0063` n `6`; index avg `0.0044` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0101` n `766`
- 1h: commodity avg `-0.09` n `12`; crypto_alt avg `0.0288` n `230`; crypto_major avg `0.0686` n `8`; equity avg `-0.0914` n `92`; fx avg `0.0039` n `6`; index avg `-0.002` n `25`; metal avg `-0.0695` n `20`; unknown avg `-0.0717` n `765`
- 4h: commodity avg `-0.1514` n `12`; crypto_alt avg `-0.9523` n `230`; crypto_major avg `-0.9358` n `8`; equity avg `-0.4115` n `92`; fx avg `-0.0571` n `6`; index avg `-0.0946` n `25`; metal avg `-0.2618` n `20`; unknown avg `0.2162` n `765`
- 24h: commodity avg `0.0521` n `12`; crypto_alt avg `-0.9805` n `230`; crypto_major avg `-0.5282` n `8`; equity avg `-0.438` n `92`; fx avg `-0.0631` n `6`; index avg `-0.1142` n `25`; metal avg `-0.3501` n `20`; unknown avg `0.279` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
