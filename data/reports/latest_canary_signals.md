# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T23:52:29.441599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.1748` n `239`; crypto_major avg `-0.1514` n `8`; equity avg `-0.046` n `168`; fx avg `-0.0057` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0082` n `20`; unknown avg `2.3692` n `1266`
- 1h: commodity avg `0.0051` n `13`; crypto_alt avg `0.103` n `239`; crypto_major avg `0.0302` n `8`; equity avg `0.0192` n `168`; fx avg `0.0008` n `6`; index avg `-0.0069` n `27`; metal avg `0.0154` n `20`; unknown avg `2.3944` n `1250`
- 4h: commodity avg `0.1635` n `13`; crypto_alt avg `0.1744` n `239`; crypto_major avg `0.1784` n `8`; equity avg `0.1188` n `168`; fx avg `0.0033` n `6`; index avg `0.0175` n `27`; metal avg `0.0191` n `20`; unknown avg `1.6013` n `1166`
- 24h: commodity avg `0.1109` n `13`; crypto_alt avg `-3.3831` n `239`; crypto_major avg `-0.93` n `8`; equity avg `-0.0189` n `168`; fx avg `0.0091` n `6`; index avg `-0.0015` n `27`; metal avg `0.0323` n `20`; unknown avg `0.2616` n `1067`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
