# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T17:07:27.223951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `12`; crypto_alt avg `-0.5454` n `228`; crypto_major avg `-0.5961` n `8`; equity avg `-0.1085` n `88`; fx avg `0.0005` n `6`; index avg `-0.0163` n `23`; metal avg `-0.0117` n `20`; unknown avg `0.3842` n `764`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.6456` n `228`; crypto_major avg `-0.613` n `8`; equity avg `-0.135` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0403` n `23`; metal avg `-0.0072` n `20`; unknown avg `0.3161` n `764`
- 4h: commodity avg `-0.1199` n `12`; crypto_alt avg `0.3153` n `228`; crypto_major avg `0.2105` n `8`; equity avg `-0.0789` n `88`; fx avg `0.0006` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0057` n `20`; unknown avg `0.1055` n `764`
- 24h: commodity avg `0.1823` n `12`; crypto_alt avg `-0.1093` n `228`; crypto_major avg `-0.1684` n `8`; equity avg `0.15` n `87`; fx avg `0.074` n `6`; index avg `-0.1772` n `23`; metal avg `-0.0297` n `20`; unknown avg `0.0929` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
