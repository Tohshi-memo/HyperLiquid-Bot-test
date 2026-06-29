# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T23:37:28.545006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.115` n `228`; crypto_major avg `-0.0046` n `8`; equity avg `0.0578` n `88`; fx avg `-0.0073` n `6`; index avg `0.0033` n `23`; metal avg `-0.0082` n `20`; unknown avg `0.0919` n `765`
- 1h: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.0288` n `228`; crypto_major avg `-0.1338` n `8`; equity avg `0.1197` n `88`; fx avg `-0.0073` n `6`; index avg `0.0175` n `23`; metal avg `0.0966` n `20`; unknown avg `0.3244` n `765`
- 4h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.6059` n `228`; crypto_major avg `-0.4602` n `8`; equity avg `0.3075` n `88`; fx avg `0.024` n `6`; index avg `0.0072` n `23`; metal avg `0.0752` n `20`; unknown avg `0.6441` n `763`
- 24h: commodity avg `-0.215` n `12`; crypto_alt avg `1.3151` n `228`; crypto_major avg `2.4322` n `8`; equity avg `1.6541` n `88`; fx avg `0.2184` n `6`; index avg `0.1063` n `23`; metal avg `-0.2004` n `20`; unknown avg `2.0335` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
