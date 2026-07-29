# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T19:22:34.039906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.047` n `12`; crypto_alt avg `-0.2551` n `230`; crypto_major avg `-0.3584` n `8`; equity avg `-1.0382` n `102`; fx avg `0.0226` n `6`; index avg `-0.1774` n `25`; metal avg `-0.1126` n `20`; unknown avg `-0.0626` n `778`
- 1h: commodity avg `-0.0322` n `12`; crypto_alt avg `-0.1968` n `230`; crypto_major avg `-0.3349` n `8`; equity avg `-0.0203` n `102`; fx avg `0.039` n `6`; index avg `-0.0008` n `25`; metal avg `0.145` n `20`; unknown avg `-0.2817` n `778`
- 4h: commodity avg `-0.0477` n `12`; crypto_alt avg `0.4809` n `230`; crypto_major avg `0.1577` n `8`; equity avg `0.7235` n `102`; fx avg `0.0449` n `6`; index avg `0.1651` n `25`; metal avg `0.6373` n `20`; unknown avg `-0.2786` n `778`
- 24h: commodity avg `1.324` n `12`; crypto_alt avg `-1.6738` n `230`; crypto_major avg `-0.02` n `8`; equity avg `-1.5755` n `102`; fx avg `-0.0136` n `6`; index avg `-0.2863` n `25`; metal avg `0.4118` n `20`; unknown avg `-0.6892` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
