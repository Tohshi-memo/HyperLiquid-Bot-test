# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T18:07:30.893683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0458` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `-0.0793` n `98`; fx avg `0.0001` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0199` n `20`; unknown avg `0.0265` n `773`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.2984` n `230`; crypto_major avg `-0.1732` n `8`; equity avg `-0.4702` n `98`; fx avg `0.0038` n `6`; index avg `-0.0602` n `25`; metal avg `-0.0492` n `20`; unknown avg `0.1212` n `773`
- 4h: commodity avg `0.0437` n `12`; crypto_alt avg `-0.2072` n `230`; crypto_major avg `-0.0373` n `8`; equity avg `-0.3855` n `98`; fx avg `-0.0047` n `6`; index avg `0.0337` n `25`; metal avg `-0.243` n `20`; unknown avg `-0.0596` n `773`
- 24h: commodity avg `0.6415` n `12`; crypto_alt avg `-0.113` n `230`; crypto_major avg `-0.4371` n `8`; equity avg `-0.611` n `98`; fx avg `-0.0393` n `6`; index avg `-0.1239` n `25`; metal avg `0.3504` n `20`; unknown avg `0.8396` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0964`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0775`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0761`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
