# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T11:22:31.238403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `-0.1269` n `237`; crypto_major avg `-0.1008` n `8`; equity avg `-0.0218` n `151`; fx avg `-0.0047` n `6`; index avg `0.0135` n `26`; metal avg `0.0092` n `20`; unknown avg `0.079` n `1198`
- 1h: commodity avg `0.0742` n `13`; crypto_alt avg `0.0079` n `237`; crypto_major avg `-0.0843` n `8`; equity avg `-0.3374` n `151`; fx avg `-0.0061` n `6`; index avg `-0.0497` n `26`; metal avg `-0.0064` n `20`; unknown avg `3.7804` n `1196`
- 4h: commodity avg `0.1965` n `13`; crypto_alt avg `-0.5335` n `237`; crypto_major avg `-0.3537` n `8`; equity avg `-0.7217` n `151`; fx avg `-0.0112` n `6`; index avg `-0.0943` n `26`; metal avg `-0.1292` n `20`; unknown avg `0.3683` n `1180`
- 24h: commodity avg `0.24` n `13`; crypto_alt avg `0.3902` n `237`; crypto_major avg `-0.475` n `8`; equity avg `-2.1204` n `151`; fx avg `-0.0292` n `6`; index avg `-0.2986` n `26`; metal avg `-0.3608` n `20`; unknown avg `0.5735` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
