# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T04:07:25.399474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `0.1918` n `230`; crypto_major avg `0.2127` n `8`; equity avg `0.0368` n `98`; fx avg `0.0003` n `6`; index avg `0.0167` n `25`; metal avg `0.0453` n `20`; unknown avg `0.0121` n `771`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.2379` n `230`; crypto_major avg `0.112` n `8`; equity avg `0.7406` n `98`; fx avg `-0.0162` n `6`; index avg `0.1197` n `25`; metal avg `0.0848` n `20`; unknown avg `-0.0393` n `771`
- 4h: commodity avg `-0.0549` n `12`; crypto_alt avg `0.8168` n `230`; crypto_major avg `0.9326` n `8`; equity avg `1.8444` n `98`; fx avg `-0.026` n `6`; index avg `0.4869` n `25`; metal avg `0.4468` n `20`; unknown avg `0.88` n `771`
- 24h: commodity avg `-0.3706` n `12`; crypto_alt avg `2.249` n `230`; crypto_major avg `1.9373` n `8`; equity avg `1.1481` n `98`; fx avg `-0.142` n `6`; index avg `0.3159` n `25`; metal avg `0.3542` n `20`; unknown avg `0.0824` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0803`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `666`, weak_sample_signal
