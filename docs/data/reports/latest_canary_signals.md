# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T18:52:38.837968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `0.037` n `107`; fx avg `0.0071` n `6`; index avg `0.0036` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0083` n `782`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.2793` n `230`; crypto_major avg `0.2695` n `8`; equity avg `0.0705` n `107`; fx avg `0.0352` n `6`; index avg `0.0526` n `25`; metal avg `-0.0768` n `20`; unknown avg `0.006` n `782`
- 4h: commodity avg `-0.1933` n `12`; crypto_alt avg `0.477` n `230`; crypto_major avg `0.2372` n `8`; equity avg `1.19` n `107`; fx avg `0.0483` n `6`; index avg `0.3099` n `25`; metal avg `0.0467` n `20`; unknown avg `-0.1918` n `782`
- 24h: commodity avg `-1.2251` n `12`; crypto_alt avg `-0.1312` n `230`; crypto_major avg `0.3981` n `8`; equity avg `4.0469` n `107`; fx avg `0.1444` n `6`; index avg `0.8605` n `25`; metal avg `1.0355` n `20`; unknown avg `0.525` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
