# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T10:04:35.938984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0567` n `12`; crypto_alt avg `0.1161` n `230`; crypto_major avg `0.2016` n `8`; equity avg `0.1171` n `98`; fx avg `-0.014` n `6`; index avg `0.0397` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0266` n `773`
- 1h: commodity avg `0.1211` n `12`; crypto_alt avg `0.0802` n `230`; crypto_major avg `0.0495` n `8`; equity avg `-0.0392` n `98`; fx avg `0.01` n `6`; index avg `-0.0045` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.0242` n `773`
- 4h: commodity avg `0.4265` n `12`; crypto_alt avg `0.2718` n `230`; crypto_major avg `0.2131` n `8`; equity avg `0.061` n `98`; fx avg `-0.0278` n `6`; index avg `-0.0198` n `25`; metal avg `-0.1058` n `20`; unknown avg `0.0742` n `772`
- 24h: commodity avg `0.7496` n `12`; crypto_alt avg `-0.759` n `230`; crypto_major avg `-1.5066` n `8`; equity avg `0.4935` n `98`; fx avg `-0.01` n `6`; index avg `0.0009` n `25`; metal avg `0.3519` n `20`; unknown avg `0.0958` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.104`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0784`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0689`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0678`, n `666`, weak_sample_signal
