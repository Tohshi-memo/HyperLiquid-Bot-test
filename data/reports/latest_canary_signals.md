# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T22:52:25.917906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.0823` n `229`; crypto_major avg `-0.0082` n `8`; equity avg `-0.0015` n `88`; fx avg `0.0051` n `6`; index avg `0.0061` n `25`; metal avg `-0.012` n `20`; unknown avg `0.1544` n `765`
- 1h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.0032` n `229`; crypto_major avg `-0.099` n `8`; equity avg `0.0881` n `88`; fx avg `-0.0061` n `6`; index avg `0.016` n `25`; metal avg `0.0005` n `20`; unknown avg `3.616` n `765`
- 4h: commodity avg `0.0141` n `12`; crypto_alt avg `-0.1878` n `229`; crypto_major avg `-0.7034` n `8`; equity avg `0.2619` n `88`; fx avg `0.0064` n `6`; index avg `0.0871` n `25`; metal avg `0.0121` n `20`; unknown avg `3.2127` n `765`
- 24h: commodity avg `0.0989` n `12`; crypto_alt avg `1.4877` n `228`; crypto_major avg `2.3199` n `8`; equity avg `-2.3394` n `88`; fx avg `-0.1395` n `6`; index avg `-0.4433` n `25`; metal avg `0.888` n `20`; unknown avg `4.0308` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
