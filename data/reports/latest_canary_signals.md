# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T08:37:27.458739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.0589` n `230`; crypto_major avg `-0.0676` n `8`; equity avg `0.0573` n `98`; fx avg `-0.0128` n `6`; index avg `-0.0009` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0406` n `773`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.3622` n `230`; crypto_major avg `0.4205` n `8`; equity avg `0.1087` n `98`; fx avg `0.0013` n `6`; index avg `0.0218` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.1062` n `772`
- 4h: commodity avg `0.2541` n `12`; crypto_alt avg `-0.5294` n `230`; crypto_major avg `-0.9102` n `8`; equity avg `-1.0501` n `98`; fx avg `-0.0483` n `6`; index avg `-0.2321` n `25`; metal avg `-0.1025` n `20`; unknown avg `-0.1166` n `739`
- 24h: commodity avg `0.8782` n `12`; crypto_alt avg `-0.9153` n `230`; crypto_major avg `-1.6032` n `8`; equity avg `0.3475` n `98`; fx avg `-0.0239` n `6`; index avg `-0.0192` n `25`; metal avg `0.3187` n `20`; unknown avg `0.097` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1058`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
