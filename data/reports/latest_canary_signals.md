# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T10:01:36.389607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0371` n `12`; crypto_alt avg `0.0084` n `230`; crypto_major avg `0.0428` n `8`; equity avg `0.0263` n `114`; fx avg `0.004` n `6`; index avg `0.0198` n `25`; metal avg `0.0235` n `20`; unknown avg `0.001` n `795`
- 1h: commodity avg `-0.0691` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `-0.1124` n `8`; equity avg `-0.2126` n `114`; fx avg `-0.0314` n `6`; index avg `-0.0001` n `25`; metal avg `0.05` n `20`; unknown avg `-0.0182` n `795`
- 4h: commodity avg `-0.1595` n `12`; crypto_alt avg `0.5488` n `230`; crypto_major avg `0.1529` n `8`; equity avg `-0.7676` n `114`; fx avg `-0.0107` n `6`; index avg `-0.037` n `25`; metal avg `-0.0098` n `20`; unknown avg `0.0339` n `793`
- 24h: commodity avg `0.4245` n `12`; crypto_alt avg `-0.6455` n `230`; crypto_major avg `0.1924` n `8`; equity avg `-2.7272` n `114`; fx avg `-0.0493` n `6`; index avg `-0.525` n `25`; metal avg `-0.1995` n `20`; unknown avg `0.0084` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
