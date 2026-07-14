# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T17:32:33.879332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `0.025` n `230`; crypto_major avg `0.1193` n `8`; equity avg `0.0347` n `92`; fx avg `-0.0022` n `6`; index avg `-0.0032` n `25`; metal avg `0.0294` n `20`; unknown avg `-0.0035` n `766`
- 1h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.3095` n `230`; crypto_major avg `-0.4209` n `8`; equity avg `-0.0495` n `92`; fx avg `-0.0275` n `6`; index avg `0.0097` n `25`; metal avg `0.0321` n `20`; unknown avg `0.301` n `766`
- 4h: commodity avg `-0.1352` n `12`; crypto_alt avg `-0.1881` n `230`; crypto_major avg `0.0835` n `8`; equity avg `0.0995` n `92`; fx avg `-0.0299` n `6`; index avg `0.0635` n `25`; metal avg `-0.076` n `20`; unknown avg `-0.2892` n `758`
- 24h: commodity avg `0.3826` n `12`; crypto_alt avg `1.788` n `230`; crypto_major avg `3.1377` n `8`; equity avg `1.08` n `92`; fx avg `-0.0263` n `6`; index avg `0.3321` n `25`; metal avg `0.6574` n `20`; unknown avg `-0.0539` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
