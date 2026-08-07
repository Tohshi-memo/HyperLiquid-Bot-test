# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T01:07:24.332075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `0.0589` n `8`; equity avg `0.0914` n `112`; fx avg `-0.006` n `6`; index avg `-0.001` n `25`; metal avg `0.1168` n `20`; unknown avg `0.3669` n `782`
- 1h: commodity avg `-0.055` n `12`; crypto_alt avg `0.1268` n `230`; crypto_major avg `-0.0331` n `8`; equity avg `-0.3209` n `112`; fx avg `-0.0336` n `6`; index avg `-0.0924` n `25`; metal avg `-0.0189` n `20`; unknown avg `0.3069` n `782`
- 4h: commodity avg `0.035` n `12`; crypto_alt avg `0.4231` n `230`; crypto_major avg `0.029` n `8`; equity avg `0.3769` n `112`; fx avg `-0.0255` n `6`; index avg `-0.0159` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.0381` n `782`
- 24h: commodity avg `0.5448` n `12`; crypto_alt avg `0.2492` n `230`; crypto_major avg `-0.9592` n `8`; equity avg `0.9564` n `109`; fx avg `0.0638` n `6`; index avg `-0.0286` n `25`; metal avg `-0.4057` n `20`; unknown avg `113.0951` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
