# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T06:57:06.767354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.1085` n `230`; crypto_major avg `-0.1143` n `8`; equity avg `0.0853` n `92`; fx avg `-0.0083` n `6`; index avg `0.0013` n `25`; metal avg `0.003` n `20`; unknown avg `0.0053` n `765`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `0.0738` n `230`; crypto_major avg `0.0288` n `8`; equity avg `0.1271` n `92`; fx avg `-0.012` n `6`; index avg `0.0036` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0085` n `733`
- 4h: commodity avg `0.0478` n `12`; crypto_alt avg `-0.217` n `229`; crypto_major avg `0.0031` n `8`; equity avg `0.1061` n `92`; fx avg `0.0203` n `6`; index avg `0.0019` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0181` n `731`
- 24h: commodity avg `-0.2933` n `12`; crypto_alt avg `0.4727` n `229`; crypto_major avg `-0.0919` n `8`; equity avg `-0.1001` n `92`; fx avg `-0.0593` n `6`; index avg `0.1432` n `25`; metal avg `0.0285` n `20`; unknown avg `2.9035` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
