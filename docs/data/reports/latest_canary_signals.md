# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T00:10:12.932972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `0.7246` n `230`; crypto_major avg `0.7627` n `8`; equity avg `0.3858` n `92`; fx avg `0.0205` n `6`; index avg `0.0819` n `25`; metal avg `0.128` n `20`; unknown avg `0.0109` n `766`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `0.7184` n `230`; crypto_major avg `0.7958` n `8`; equity avg `0.2564` n `92`; fx avg `0.0313` n `6`; index avg `0.0804` n `25`; metal avg `0.1901` n `20`; unknown avg `0.0178` n `766`
- 4h: commodity avg `-0.1761` n `12`; crypto_alt avg `-0.2085` n `230`; crypto_major avg `-0.0641` n `8`; equity avg `-0.1124` n `92`; fx avg `-0.0228` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0719` n `20`; unknown avg `-0.081` n `765`
- 24h: commodity avg `-0.0871` n `12`; crypto_alt avg `0.5883` n `230`; crypto_major avg `1.1442` n `8`; equity avg `-0.0115` n `92`; fx avg `-0.0388` n `6`; index avg `-0.0167` n `25`; metal avg `-0.1479` n `20`; unknown avg `0.4754` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
