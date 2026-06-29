# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T14:22:30.157914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0578` n `12`; crypto_alt avg `-0.1667` n `228`; crypto_major avg `-0.1243` n `8`; equity avg `-0.0914` n `88`; fx avg `-0.0131` n `6`; index avg `-0.0357` n `23`; metal avg `0.0675` n `20`; unknown avg `0.9335` n `764`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `-0.9822` n `228`; crypto_major avg `-1.14` n `8`; equity avg `-1.5532` n `88`; fx avg `0.0188` n `6`; index avg `-0.2295` n `23`; metal avg `-0.2223` n `20`; unknown avg `0.7614` n `764`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.8778` n `228`; crypto_major avg `-0.8159` n `8`; equity avg `-1.4708` n `88`; fx avg `0.0483` n `6`; index avg `-0.2486` n `23`; metal avg `-0.0912` n `20`; unknown avg `1.0468` n `764`
- 24h: commodity avg `-0.5759` n `12`; crypto_alt avg `-0.8202` n `228`; crypto_major avg `-0.6828` n `8`; equity avg `-1.0414` n `88`; fx avg `0.1177` n `6`; index avg `-0.1792` n `23`; metal avg `-0.5797` n `20`; unknown avg `1.8775` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
