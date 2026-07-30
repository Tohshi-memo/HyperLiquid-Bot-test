# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T10:22:29.053739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0695` n `12`; crypto_alt avg `-0.0531` n `230`; crypto_major avg `-0.0432` n `8`; equity avg `0.2563` n `102`; fx avg `-0.0451` n `6`; index avg `0.0619` n `25`; metal avg `0.0452` n `20`; unknown avg `-0.0389` n `779`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `0.1293` n `8`; equity avg `0.2992` n `102`; fx avg `-0.0637` n `6`; index avg `0.0622` n `25`; metal avg `0.0935` n `20`; unknown avg `-0.0007` n `779`
- 4h: commodity avg `-0.3398` n `12`; crypto_alt avg `0.2732` n `230`; crypto_major avg `0.7106` n `8`; equity avg `0.7709` n `102`; fx avg `-0.0177` n `6`; index avg `0.1479` n `25`; metal avg `0.4718` n `20`; unknown avg `0.0034` n `771`
- 24h: commodity avg `0.4692` n `12`; crypto_alt avg `-0.2904` n `230`; crypto_major avg `-0.1972` n `8`; equity avg `-2.9056` n `102`; fx avg `-0.0331` n `6`; index avg `-0.4135` n `25`; metal avg `0.4539` n `20`; unknown avg `-0.1295` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
