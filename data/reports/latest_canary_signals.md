# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T01:37:23.538446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.0414` n `231`; crypto_major avg `0.1164` n `8`; equity avg `-0.0181` n `127`; fx avg `0.0143` n `6`; index avg `0.0022` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.0056` n `793`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.1553` n `231`; crypto_major avg `-0.0199` n `8`; equity avg `-0.0005` n `127`; fx avg `0.007` n `6`; index avg `0.0048` n `26`; metal avg `-0.034` n `20`; unknown avg `-0.0044` n `793`
- 4h: commodity avg `-0.0392` n `12`; crypto_alt avg `0.4068` n `231`; crypto_major avg `0.2104` n `8`; equity avg `0.0621` n `127`; fx avg `0.0089` n `6`; index avg `0.0071` n `26`; metal avg `0.0106` n `20`; unknown avg `-0.0379` n `793`
- 24h: commodity avg `-0.0372` n `12`; crypto_alt avg `-3.7003` n `231`; crypto_major avg `-3.6887` n `8`; equity avg `-2.2092` n `127`; fx avg `-0.0787` n `6`; index avg `-0.2228` n `26`; metal avg `-0.2456` n `20`; unknown avg `-0.5753` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
