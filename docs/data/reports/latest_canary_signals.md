# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T13:56:11.142931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `12`; crypto_alt avg `-0.016` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `-0.3186` n `112`; fx avg `0.0064` n `6`; index avg `-0.0656` n `25`; metal avg `-0.0715` n `20`; unknown avg `-0.0396` n `782`
- 1h: commodity avg `0.1897` n `12`; crypto_alt avg `-0.0145` n `230`; crypto_major avg `-0.0977` n `8`; equity avg `-1.1576` n `112`; fx avg `0.031` n `6`; index avg `-0.1659` n `25`; metal avg `-0.1906` n `20`; unknown avg `-0.0567` n `782`
- 4h: commodity avg `0.0721` n `12`; crypto_alt avg `0.0137` n `230`; crypto_major avg `0.322` n `8`; equity avg `-0.0287` n `112`; fx avg `-0.0309` n `6`; index avg `0.0354` n `25`; metal avg `-0.195` n `20`; unknown avg `-0.1522` n `782`
- 24h: commodity avg `0.3809` n `12`; crypto_alt avg `0.2071` n `230`; crypto_major avg `0.7526` n `8`; equity avg `1.7205` n `109`; fx avg `-0.1228` n `6`; index avg `0.0586` n `25`; metal avg `0.4416` n `20`; unknown avg `0.1303` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
