# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:07:33.021610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0707` n `12`; crypto_alt avg `-0.1164` n `230`; crypto_major avg `-0.071` n `8`; equity avg `-0.0011` n `114`; fx avg `-0.0257` n `6`; index avg `0.0041` n `25`; metal avg `-0.036` n `20`; unknown avg `0.0203` n `791`
- 1h: commodity avg `-0.0776` n `12`; crypto_alt avg `-0.6171` n `230`; crypto_major avg `-0.3895` n `8`; equity avg `-0.0249` n `114`; fx avg `-0.0262` n `6`; index avg `0.0185` n `25`; metal avg `-0.0596` n `20`; unknown avg `-0.0717` n `791`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.9067` n `230`; crypto_major avg `-0.514` n `8`; equity avg `0.0063` n `114`; fx avg `-0.0243` n `6`; index avg `0.0284` n `25`; metal avg `-0.0862` n `20`; unknown avg `-0.0109` n `791`
- 24h: commodity avg `0.0097` n `12`; crypto_alt avg `-1.2335` n `230`; crypto_major avg `-0.6093` n `8`; equity avg `0.2703` n `114`; fx avg `-0.0322` n `6`; index avg `0.0551` n `25`; metal avg `-0.0289` n `20`; unknown avg `0.0401` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
