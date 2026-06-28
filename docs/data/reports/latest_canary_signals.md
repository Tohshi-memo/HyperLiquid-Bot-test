# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T10:07:25.728472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.0832` n `228`; crypto_major avg `-0.1146` n `8`; equity avg `-0.0645` n `88`; fx avg `0.0066` n `6`; index avg `-0.0072` n `23`; metal avg `0.0022` n `20`; unknown avg `0.0065` n `764`
- 1h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.4627` n `228`; crypto_major avg `-0.3476` n `8`; equity avg `-0.0783` n `88`; fx avg `0.0032` n `6`; index avg `-0.0069` n `23`; metal avg `-0.0001` n `20`; unknown avg `2.0616` n `750`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `0.3061` n `228`; crypto_major avg `0.49` n `8`; equity avg `0.2281` n `88`; fx avg `0.031` n `6`; index avg `0.0444` n `23`; metal avg `0.0044` n `20`; unknown avg `-0.1025` n `742`
- 24h: commodity avg `0.1505` n `12`; crypto_alt avg `-0.2084` n `228`; crypto_major avg `-0.7643` n `8`; equity avg `0.068` n `88`; fx avg `0.0198` n `6`; index avg `-0.0695` n `23`; metal avg `-0.0167` n `20`; unknown avg `16.3423` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2186`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
