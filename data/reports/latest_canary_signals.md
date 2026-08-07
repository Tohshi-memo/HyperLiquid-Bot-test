# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T03:22:42.451538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0712` n `12`; crypto_alt avg `-0.1729` n `230`; crypto_major avg `-0.1157` n `8`; equity avg `-0.1567` n `112`; fx avg `0.0066` n `6`; index avg `-0.0512` n `25`; metal avg `-0.0302` n `20`; unknown avg `-0.2318` n `782`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.2474` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `0.0946` n `112`; fx avg `0.0314` n `6`; index avg `-0.018` n `25`; metal avg `-0.0363` n `20`; unknown avg `-0.2481` n `782`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `0.1718` n `230`; crypto_major avg `0.0426` n `8`; equity avg `0.0033` n `112`; fx avg `-0.0226` n `6`; index avg `-0.1471` n `25`; metal avg `0.0825` n `20`; unknown avg `-0.1398` n `782`
- 24h: commodity avg `0.5389` n `12`; crypto_alt avg `0.4186` n `230`; crypto_major avg `-0.5946` n `8`; equity avg `0.7633` n `109`; fx avg `0.0421` n `6`; index avg `-0.1563` n `25`; metal avg `-0.0662` n `20`; unknown avg `113.2254` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
