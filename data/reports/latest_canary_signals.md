# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T17:52:33.335555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6476` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0807` n `12`; crypto_alt avg `0.1422` n `228`; crypto_major avg `0.1776` n `8`; equity avg `0.0354` n `86`; fx avg `0.0001` n `6`; index avg `-0.0027` n `23`; metal avg `0.0137` n `20`; unknown avg `-0.091` n `765`
- 1h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.355` n `228`; crypto_major avg `0.1187` n `8`; equity avg `0.0705` n `86`; fx avg `-0.0064` n `6`; index avg `-0.0074` n `23`; metal avg `-0.034` n `20`; unknown avg `-0.0115` n `765`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `2.18` n `228`; crypto_major avg `1.9179` n `8`; equity avg `1.4561` n `86`; fx avg `-0.0556` n `6`; index avg `0.2726` n `23`; metal avg `0.2703` n `20`; unknown avg `0.3034` n `765`
- 24h: commodity avg `-0.5046` n `12`; crypto_alt avg `2.3919` n `228`; crypto_major avg `2.2063` n `8`; equity avg `-0.1231` n `86`; fx avg `-0.0708` n `6`; index avg `-0.1848` n `23`; metal avg `0.5852` n `20`; unknown avg `0.2575` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
