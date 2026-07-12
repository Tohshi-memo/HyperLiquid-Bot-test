# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T20:22:23.756472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.071` n `230`; crypto_major avg `-0.0291` n `8`; equity avg `-0.0058` n `92`; fx avg `-0.0034` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.0407` n `765`
- 1h: commodity avg `0.0525` n `12`; crypto_alt avg `-0.0312` n `230`; crypto_major avg `-0.0475` n `8`; equity avg `0.0176` n `92`; fx avg `-0.0128` n `6`; index avg `0.003` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.0203` n `765`
- 4h: commodity avg `0.1299` n `12`; crypto_alt avg `-0.1131` n `230`; crypto_major avg `-0.0299` n `8`; equity avg `0.123` n `92`; fx avg `-0.0175` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.2099` n `759`
- 24h: commodity avg `0.6079` n `12`; crypto_alt avg `-1.5137` n `230`; crypto_major avg `-0.624` n `8`; equity avg `-0.1881` n `92`; fx avg `-0.0024` n `6`; index avg `-0.0876` n `25`; metal avg `-0.0973` n `20`; unknown avg `0.1729` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
