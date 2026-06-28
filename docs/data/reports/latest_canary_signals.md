# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T09:07:26.352723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0898` n `228`; crypto_major avg `-0.1079` n `8`; equity avg `0.007` n `88`; fx avg `0.0189` n `6`; index avg `-0.0076` n `23`; metal avg `-0.005` n `20`; unknown avg `-0.1754` n `764`
- 1h: commodity avg `-0.0675` n `12`; crypto_alt avg `0.4098` n `228`; crypto_major avg `0.4528` n `8`; equity avg `0.1471` n `88`; fx avg `0.006` n `6`; index avg `0.0279` n `23`; metal avg `0.0131` n `20`; unknown avg `2.426` n `764`
- 4h: commodity avg `0.0102` n `12`; crypto_alt avg `0.5419` n `228`; crypto_major avg `0.764` n `8`; equity avg `0.2935` n `88`; fx avg `0.0186` n `6`; index avg `0.0612` n `23`; metal avg `0.0078` n `20`; unknown avg `-0.1596` n `724`
- 24h: commodity avg `0.2263` n `12`; crypto_alt avg `0.2` n `228`; crypto_major avg `-0.6458` n `8`; equity avg `0.132` n `88`; fx avg `0.0172` n `6`; index avg `-0.0649` n `23`; metal avg `-0.0301` n `20`; unknown avg `16.3218` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2184`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
