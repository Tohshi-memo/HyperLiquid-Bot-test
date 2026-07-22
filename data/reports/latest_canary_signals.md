# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T09:07:25.840538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `12`; crypto_alt avg `0.1395` n `230`; crypto_major avg `0.1058` n `8`; equity avg `0.1688` n `98`; fx avg `-0.004` n `6`; index avg `0.0375` n `25`; metal avg `0.1083` n `20`; unknown avg `0.0339` n `773`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.0815` n `230`; crypto_major avg `0.1414` n `8`; equity avg `0.1377` n `98`; fx avg `-0.0066` n `6`; index avg `0.0399` n `25`; metal avg `0.0675` n `20`; unknown avg `0.0779` n `773`
- 4h: commodity avg `0.286` n `12`; crypto_alt avg `-0.3324` n `230`; crypto_major avg `-0.6586` n `8`; equity avg `-0.5684` n `98`; fx avg `-0.0671` n `6`; index avg `-0.121` n `25`; metal avg `-0.0912` n `20`; unknown avg `-0.0811` n `739`
- 24h: commodity avg `0.8731` n `12`; crypto_alt avg `-0.6853` n `230`; crypto_major avg `-1.3279` n `8`; equity avg `0.4172` n `98`; fx avg `-0.0135` n `6`; index avg `0.0033` n `25`; metal avg `0.3092` n `20`; unknown avg `0.1159` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1065`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0794`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0702`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.069`, n `666`, weak_sample_signal
