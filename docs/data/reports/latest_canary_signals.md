# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T22:22:34.240243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.219` n `230`; crypto_major avg `-0.0833` n `8`; equity avg `0.0457` n `112`; fx avg `0.001` n `6`; index avg `0.0167` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.0378` n `782`
- 1h: commodity avg `0.092` n `12`; crypto_alt avg `0.105` n `230`; crypto_major avg `-0.0596` n `8`; equity avg `0.5072` n `112`; fx avg `0.0001` n `6`; index avg `0.0385` n `25`; metal avg `-0.0498` n `20`; unknown avg `-0.1726` n `782`
- 4h: commodity avg `0.2528` n `12`; crypto_alt avg `-0.3328` n `230`; crypto_major avg `-0.4637` n `8`; equity avg `-0.6194` n `112`; fx avg `0.0064` n `6`; index avg `-0.0595` n `25`; metal avg `-0.1048` n `20`; unknown avg `-0.2502` n `781`
- 24h: commodity avg `0.6107` n `12`; crypto_alt avg `0.1837` n `230`; crypto_major avg `-1.0906` n `8`; equity avg `0.4698` n `109`; fx avg `0.0322` n `6`; index avg `-0.1634` n `25`; metal avg `-0.1065` n `20`; unknown avg `113.237` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0955`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0756`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `669`, weak_sample_signal
