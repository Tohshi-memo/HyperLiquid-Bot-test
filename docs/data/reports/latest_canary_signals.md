# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T11:07:26.629611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.0777` n `230`; crypto_major avg `0.089` n `8`; equity avg `0.1447` n `112`; fx avg `-0.0026` n `6`; index avg `0.0223` n `25`; metal avg `0.0335` n `20`; unknown avg `-0.0324` n `782`
- 1h: commodity avg `-0.0593` n `12`; crypto_alt avg `-0.0377` n `230`; crypto_major avg `0.092` n `8`; equity avg `0.0778` n `112`; fx avg `-0.0074` n `6`; index avg `0.0307` n `25`; metal avg `-0.0341` n `20`; unknown avg `-0.0652` n `782`
- 4h: commodity avg `-0.3569` n `12`; crypto_alt avg `0.0963` n `230`; crypto_major avg `0.8099` n `8`; equity avg `0.6024` n `112`; fx avg `-0.0225` n `6`; index avg `0.0721` n `25`; metal avg `0.1662` n `20`; unknown avg `0.1442` n `782`
- 24h: commodity avg `0.1554` n `12`; crypto_alt avg `0.8766` n `230`; crypto_major avg `0.5349` n `8`; equity avg `2.6286` n `109`; fx avg `-0.101` n `6`; index avg `0.1578` n `25`; metal avg `0.3446` n `20`; unknown avg `0.3683` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
