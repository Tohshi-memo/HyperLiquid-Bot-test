# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T12:37:26.107970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0786` n `228`; crypto_major avg `0.0215` n `8`; equity avg `0.019` n `88`; fx avg `0.0` n `6`; index avg `0.0006` n `23`; metal avg `-0.0019` n `20`; unknown avg `0.0053` n `764`
- 1h: commodity avg `0.0596` n `12`; crypto_alt avg `0.3622` n `228`; crypto_major avg `0.2349` n `8`; equity avg `0.0213` n `88`; fx avg `0.0011` n `6`; index avg `0.0115` n `23`; metal avg `0.0125` n `20`; unknown avg `0.0754` n `764`
- 4h: commodity avg `0.1376` n `12`; crypto_alt avg `0.1422` n `228`; crypto_major avg `-0.1421` n `8`; equity avg `-0.0111` n `88`; fx avg `0.0065` n `6`; index avg `-0.0103` n `23`; metal avg `-0.0186` n `20`; unknown avg `-0.0856` n `764`
- 24h: commodity avg `0.1574` n `12`; crypto_alt avg `1.8248` n `228`; crypto_major avg `1.7929` n `8`; equity avg `1.9792` n `87`; fx avg `0.0421` n `6`; index avg `0.0833` n `23`; metal avg `0.3786` n `20`; unknown avg `0.197` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
