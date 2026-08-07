# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T08:37:49.372364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `0.1179` n `8`; equity avg `0.07` n `112`; fx avg `-0.007` n `6`; index avg `-0.0054` n `25`; metal avg `0.0668` n `20`; unknown avg `0.0089` n `782`
- 1h: commodity avg `-0.0464` n `12`; crypto_alt avg `0.0672` n `230`; crypto_major avg `0.1548` n `8`; equity avg `0.4633` n `112`; fx avg `-0.0208` n `6`; index avg `0.017` n `25`; metal avg `0.1929` n `20`; unknown avg `0.1193` n `782`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `0.4842` n `230`; crypto_major avg `0.3284` n `8`; equity avg `0.9391` n `112`; fx avg `-0.0414` n `6`; index avg `0.1055` n `25`; metal avg `0.4535` n `20`; unknown avg `0.0292` n `766`
- 24h: commodity avg `0.5637` n `12`; crypto_alt avg `0.2642` n `230`; crypto_major avg `-0.7748` n `8`; equity avg `1.8594` n `109`; fx avg `-0.0932` n `6`; index avg `0.0074` n `25`; metal avg `0.3889` n `20`; unknown avg `110.8404` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
