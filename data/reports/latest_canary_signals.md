# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T22:37:26.098210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.2145` n `228`; crypto_major avg `-0.2249` n `8`; equity avg `-0.062` n `88`; fx avg `0.0116` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0299` n `20`; unknown avg `-0.0398` n `765`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.3291` n `228`; crypto_major avg `-0.2756` n `8`; equity avg `0.0093` n `88`; fx avg `0.0054` n `6`; index avg `-0.0369` n `23`; metal avg `-0.0195` n `20`; unknown avg `-0.3243` n `763`
- 4h: commodity avg `-0.0731` n `12`; crypto_alt avg `-0.5361` n `228`; crypto_major avg `0.0195` n `8`; equity avg `0.3573` n `88`; fx avg `0.0302` n `6`; index avg `0.024` n `23`; metal avg `-0.0376` n `20`; unknown avg `0.109` n `763`
- 24h: commodity avg `-0.2995` n `12`; crypto_alt avg `1.8879` n `228`; crypto_major avg `3.421` n `8`; equity avg `1.6098` n `88`; fx avg `0.2222` n `6`; index avg `0.0647` n `23`; metal avg `-0.307` n `20`; unknown avg `1.8002` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
