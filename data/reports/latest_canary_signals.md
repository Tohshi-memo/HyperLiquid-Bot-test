# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T21:55:49.649602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1383` n `12`; crypto_alt avg `0.3897` n `230`; crypto_major avg `0.0306` n `8`; equity avg `0.3907` n `112`; fx avg `-0.0152` n `6`; index avg `0.0091` n `25`; metal avg `-0.0399` n `20`; unknown avg `-0.143` n `782`
- 1h: commodity avg `0.1383` n `12`; crypto_alt avg `0.3897` n `230`; crypto_major avg `0.0306` n `8`; equity avg `0.3907` n `112`; fx avg `-0.0152` n `6`; index avg `0.0091` n `25`; metal avg `-0.0399` n `20`; unknown avg `-0.143` n `782`
- 4h: commodity avg `0.2995` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.3743` n `8`; equity avg `-0.7342` n `112`; fx avg `-0.0089` n `6`; index avg `-0.0887` n `25`; metal avg `-0.0947` n `20`; unknown avg `-0.2183` n `781`
- 24h: commodity avg `0.5847` n `12`; crypto_alt avg `0.5407` n `230`; crypto_major avg `-1.0639` n `8`; equity avg `0.5998` n `109`; fx avg `0.0136` n `6`; index avg `-0.1497` n `25`; metal avg `-0.0894` n `20`; unknown avg `113.2655` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `671`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1148`, n `671`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `671`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0979`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0919`, n `671`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0876`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0749`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `671`, weak_sample_signal
