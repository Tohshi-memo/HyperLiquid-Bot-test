# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T09:37:28.684122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `-0.3748` n `229`; crypto_major avg `-0.3195` n `8`; equity avg `-0.0195` n `88`; fx avg `-0.0036` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0309` n `765`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `-0.4354` n `229`; crypto_major avg `-0.472` n `8`; equity avg `-0.0648` n `88`; fx avg `-0.0038` n `6`; index avg `-0.0098` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.0943` n `765`
- 4h: commodity avg `0.0567` n `12`; crypto_alt avg `-0.6516` n `229`; crypto_major avg `-0.4938` n `8`; equity avg `-0.0595` n `88`; fx avg `-0.0171` n `6`; index avg `-0.0008` n `25`; metal avg `0.0247` n `20`; unknown avg `0.673` n `745`
- 24h: commodity avg `0.016` n `12`; crypto_alt avg `1.063` n `229`; crypto_major avg `2.0814` n `8`; equity avg `0.3157` n `88`; fx avg `-0.07` n `6`; index avg `-0.014` n `25`; metal avg `-0.0738` n `20`; unknown avg `5.6209` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
