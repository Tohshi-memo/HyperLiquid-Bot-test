# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T21:07:25.417644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `0.2126` n `228`; crypto_major avg `0.2062` n `8`; equity avg `-0.0141` n `74`; fx avg `-0.0055` n `6`; index avg `0.0335` n `23`; metal avg `0.0162` n `18`; unknown avg `0.0282` n `515`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `0.5176` n `228`; crypto_major avg `0.5786` n `8`; equity avg `0.0824` n `74`; fx avg `-0.0061` n `6`; index avg `0.1302` n `23`; metal avg `0.0055` n `18`; unknown avg `-0.0727` n `515`
- 4h: commodity avg `0.1251` n `12`; crypto_alt avg `-0.195` n `228`; crypto_major avg `-0.2997` n `8`; equity avg `0.1513` n `74`; fx avg `0.0195` n `6`; index avg `-0.0162` n `23`; metal avg `0.0386` n `18`; unknown avg `0.3453` n `515`
- 24h: commodity avg `0.2569` n `12`; crypto_alt avg `-2.6219` n `228`; crypto_major avg `-2.355` n `8`; equity avg `-0.6622` n `74`; fx avg `0.0652` n `6`; index avg `0.333` n `23`; metal avg `-0.5193` n `18`; unknown avg `0.4121` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
