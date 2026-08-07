# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T07:52:28.219989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.0049` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `-0.0013` n `112`; fx avg `0.0025` n `6`; index avg `-0.0095` n `25`; metal avg `0.0145` n `20`; unknown avg `0.0691` n `782`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0142` n `230`; crypto_major avg `0.0796` n `8`; equity avg `0.1403` n `112`; fx avg `0.0251` n `6`; index avg `0.0388` n `25`; metal avg `-0.0241` n `20`; unknown avg `-0.0302` n `782`
- 4h: commodity avg `0.0581` n `12`; crypto_alt avg `0.2162` n `230`; crypto_major avg `0.0297` n `8`; equity avg `0.4803` n `112`; fx avg `-0.0247` n `6`; index avg `0.0996` n `25`; metal avg `0.2978` n `20`; unknown avg `-0.0683` n `766`
- 24h: commodity avg `0.5427` n `12`; crypto_alt avg `0.1837` n `230`; crypto_major avg `-0.8462` n `8`; equity avg `1.4388` n `109`; fx avg `-0.1028` n `6`; index avg `0.0074` n `25`; metal avg `0.3808` n `20`; unknown avg `110.7382` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
