# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T04:07:27.096177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.1251` n `228`; crypto_major avg `-0.035` n `8`; equity avg `-0.0789` n `88`; fx avg `-0.0189` n `6`; index avg `-0.0307` n `23`; metal avg `-0.0235` n `20`; unknown avg `-0.2868` n `765`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `0.5682` n `228`; crypto_major avg `0.2414` n `8`; equity avg `0.064` n `88`; fx avg `-0.0081` n `6`; index avg `0.0213` n `23`; metal avg `-0.0764` n `20`; unknown avg `-0.2288` n `763`
- 4h: commodity avg `-0.0457` n `12`; crypto_alt avg `1.2691` n `228`; crypto_major avg `0.922` n `8`; equity avg `-0.4966` n `88`; fx avg `0.0213` n `6`; index avg `-0.2001` n `23`; metal avg `-0.3431` n `20`; unknown avg `0.5572` n `763`
- 24h: commodity avg `0.1213` n `12`; crypto_alt avg `-0.0462` n `228`; crypto_major avg `0.2829` n `8`; equity avg `0.575` n `88`; fx avg `0.1541` n `6`; index avg `-0.0173` n `23`; metal avg `-0.1128` n `20`; unknown avg `-1.0879` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
