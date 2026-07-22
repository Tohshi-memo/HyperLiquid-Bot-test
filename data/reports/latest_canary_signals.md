# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T13:07:27.540181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0764` n `12`; crypto_alt avg `0.0514` n `230`; crypto_major avg `-0.0402` n `8`; equity avg `-0.0158` n `98`; fx avg `0.0057` n `6`; index avg `0.003` n `25`; metal avg `-0.0308` n `20`; unknown avg `4.0075` n `773`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0793` n `230`; crypto_major avg `-0.0625` n `8`; equity avg `0.0192` n `98`; fx avg `0.0036` n `6`; index avg `0.01` n `25`; metal avg `-0.0747` n `20`; unknown avg `3.9705` n `773`
- 4h: commodity avg `0.0875` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `-0.2273` n `8`; equity avg `-0.5013` n `98`; fx avg `0.009` n `6`; index avg `-0.0972` n `25`; metal avg `-0.0396` n `20`; unknown avg `4.5536` n `773`
- 24h: commodity avg `0.5475` n `12`; crypto_alt avg `-0.8532` n `230`; crypto_major avg `-1.8616` n `8`; equity avg `0.0702` n `98`; fx avg `-0.0013` n `6`; index avg `-0.0962` n `25`; metal avg `0.3462` n `20`; unknown avg `4.7803` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1036`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0907`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
