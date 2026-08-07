# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T09:27:39.169489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `-0.0622` n `230`; crypto_major avg `0.0888` n `8`; equity avg `0.0598` n `112`; fx avg `0.0071` n `6`; index avg `-0.007` n `25`; metal avg `0.0229` n `20`; unknown avg `-0.0102` n `782`
- 1h: commodity avg `-0.1153` n `12`; crypto_alt avg `-0.0305` n `230`; crypto_major avg `0.4943` n `8`; equity avg `0.1471` n `112`; fx avg `-0.0024` n `6`; index avg `0.0254` n `25`; metal avg `0.0723` n `20`; unknown avg `0.022` n `782`
- 4h: commodity avg `-0.1712` n `12`; crypto_alt avg `0.2171` n `230`; crypto_major avg `0.9294` n `8`; equity avg `0.8636` n `112`; fx avg `-0.0462` n `6`; index avg `0.0894` n `25`; metal avg `0.4368` n `20`; unknown avg `0.0391` n `766`
- 24h: commodity avg `0.476` n `12`; crypto_alt avg `0.4246` n `230`; crypto_major avg `-0.214` n `8`; equity avg `2.0999` n `109`; fx avg `-0.074` n `6`; index avg `0.0759` n `25`; metal avg `0.2782` n `20`; unknown avg `110.8288` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
