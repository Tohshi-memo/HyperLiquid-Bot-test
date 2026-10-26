# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T06:22:31.553070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `13`; crypto_alt avg `0.0209` n `237`; crypto_major avg `-0.0454` n `8`; equity avg `-0.0775` n `152`; fx avg `0.0118` n `6`; index avg `-0.0208` n `26`; metal avg `-0.0301` n `20`; unknown avg `0.0975` n `1240`
- 1h: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.2957` n `237`; crypto_major avg `-0.1479` n `8`; equity avg `-0.3537` n `152`; fx avg `0.0207` n `6`; index avg `-0.0891` n `26`; metal avg `-0.0885` n `20`; unknown avg `3.9526` n `1212`
- 4h: commodity avg `-0.0352` n `13`; crypto_alt avg `0.3107` n `237`; crypto_major avg `0.4054` n `8`; equity avg `0.1324` n `152`; fx avg `0.0457` n `6`; index avg `-0.005` n `26`; metal avg `0.051` n `20`; unknown avg `4.7116` n `1196`
- 24h: commodity avg `-0.6169` n `13`; crypto_alt avg `-0.7048` n `237`; crypto_major avg `-0.549` n `8`; equity avg `-0.5156` n `152`; fx avg `0.0788` n `6`; index avg `-0.032` n `26`; metal avg `0.129` n `20`; unknown avg `194.1256` n `987`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2565`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
