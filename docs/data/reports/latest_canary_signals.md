# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T11:07:24.785215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.2009` n `234`; crypto_major avg `0.0106` n `8`; equity avg `-0.0066` n `141`; fx avg `0.0031` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.1266` n `960`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.2161` n `234`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0267` n `141`; fx avg `0.0013` n `6`; index avg `-0.0088` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.1661` n `960`
- 4h: commodity avg `0.0043` n `12`; crypto_alt avg `0.248` n `234`; crypto_major avg `0.63` n `8`; equity avg `0.1127` n `141`; fx avg `-0.0137` n `6`; index avg `0.0192` n `26`; metal avg `-0.0057` n `20`; unknown avg `1.7215` n `943`
- 24h: commodity avg `0.0639` n `12`; crypto_alt avg `0.5159` n `234`; crypto_major avg `0.6973` n `8`; equity avg `0.3567` n `141`; fx avg `-0.0211` n `6`; index avg `0.0293` n `26`; metal avg `0.0005` n `20`; unknown avg `4.6396` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
