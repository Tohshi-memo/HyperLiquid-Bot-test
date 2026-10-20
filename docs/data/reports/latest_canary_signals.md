# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T10:22:25.348154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.0254` n `237`; crypto_major avg `0.0019` n `8`; equity avg `0.008` n `151`; fx avg `-0.0113` n `6`; index avg `0.0177` n `26`; metal avg `0.0391` n `20`; unknown avg `0.0893` n `1198`
- 1h: commodity avg `0.0048` n `13`; crypto_alt avg `-0.1271` n `237`; crypto_major avg `-0.0361` n `8`; equity avg `0.0019` n `151`; fx avg `0.0092` n `6`; index avg `0.0257` n `26`; metal avg `-0.0364` n `20`; unknown avg `0.5198` n `1196`
- 4h: commodity avg `0.2239` n `13`; crypto_alt avg `-0.5093` n `237`; crypto_major avg `-0.3018` n `8`; equity avg `-0.3306` n `151`; fx avg `-0.0287` n `6`; index avg `-0.041` n `26`; metal avg `-0.0575` n `20`; unknown avg `-0.0084` n `1180`
- 24h: commodity avg `0.1526` n `13`; crypto_alt avg `-0.2349` n `237`; crypto_major avg `-0.7767` n `8`; equity avg `-1.7587` n `151`; fx avg `-0.001` n `6`; index avg `-0.2379` n `26`; metal avg `-0.2572` n `20`; unknown avg `0.329` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
