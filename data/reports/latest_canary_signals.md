# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T02:22:33.987212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `-0.0285` n `8`; equity avg `-0.3675` n `102`; fx avg `-0.0234` n `6`; index avg `-0.106` n `25`; metal avg `-0.0589` n `20`; unknown avg `-0.0669` n `779`
- 1h: commodity avg `-0.0745` n `12`; crypto_alt avg `0.5992` n `230`; crypto_major avg `0.5497` n `8`; equity avg `0.1828` n `102`; fx avg `0.0174` n `6`; index avg `0.1049` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.3746` n `779`
- 4h: commodity avg `-0.113` n `12`; crypto_alt avg `0.8441` n `230`; crypto_major avg `0.5135` n `8`; equity avg `1.0775` n `102`; fx avg `-0.0185` n `6`; index avg `0.2647` n `25`; metal avg `0.0548` n `20`; unknown avg `0.6638` n `778`
- 24h: commodity avg `0.428` n `12`; crypto_alt avg `-0.5333` n `230`; crypto_major avg `0.3687` n `8`; equity avg `-1.5134` n `102`; fx avg `0.0383` n `6`; index avg `-0.0234` n `25`; metal avg `0.2751` n `20`; unknown avg `-0.5691` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
