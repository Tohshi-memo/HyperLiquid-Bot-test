# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T09:37:25.313049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0492` n `228`; crypto_major avg `-0.0452` n `8`; equity avg `0.0166` n `88`; fx avg `-0.0007` n `6`; index avg `-0.0008` n `23`; metal avg `0.0076` n `20`; unknown avg `-0.0086` n `764`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `0.2238` n `228`; crypto_major avg `0.1922` n `8`; equity avg `0.0988` n `88`; fx avg `0.0201` n `6`; index avg `0.0121` n `23`; metal avg `0.0184` n `20`; unknown avg `-0.1289` n `764`
- 4h: commodity avg `0.0038` n `12`; crypto_alt avg `0.5487` n `228`; crypto_major avg `0.7978` n `8`; equity avg `0.3379` n `88`; fx avg `0.0368` n `6`; index avg `0.0513` n `23`; metal avg `0.0452` n `20`; unknown avg `-0.1972` n `724`
- 24h: commodity avg `0.2032` n `12`; crypto_alt avg `0.2705` n `228`; crypto_major avg `-0.4292` n `8`; equity avg `0.1318` n `88`; fx avg `-0.005` n `6`; index avg `-0.0632` n `23`; metal avg `-0.008` n `20`; unknown avg `16.3736` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
