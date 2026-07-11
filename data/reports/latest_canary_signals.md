# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T09:37:24.204484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `-0.0067` n `8`; equity avg `0.0523` n `92`; fx avg `-0.0011` n `6`; index avg `0.0089` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.0037` n `765`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.1542` n `230`; crypto_major avg `0.007` n `8`; equity avg `0.0469` n `92`; fx avg `-0.0041` n `6`; index avg `0.0082` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0392` n `761`
- 4h: commodity avg `0.0756` n `12`; crypto_alt avg `0.0966` n `230`; crypto_major avg `0.0655` n `8`; equity avg `0.1655` n `92`; fx avg `-0.0128` n `6`; index avg `0.0213` n `25`; metal avg `-0.0117` n `20`; unknown avg `-0.0276` n `729`
- 24h: commodity avg `-0.1453` n `12`; crypto_alt avg `0.2036` n `229`; crypto_major avg `-0.6744` n `8`; equity avg `0.0579` n `92`; fx avg `-0.0869` n `6`; index avg `0.1552` n `25`; metal avg `0.179` n `20`; unknown avg `2.9944` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
