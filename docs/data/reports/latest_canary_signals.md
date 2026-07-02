# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T23:37:25.461947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.0455` n `229`; crypto_major avg `0.0591` n `8`; equity avg `0.0997` n `88`; fx avg `-0.0013` n `6`; index avg `0.0237` n `25`; metal avg `0.034` n `20`; unknown avg `0.4803` n `765`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `0.2253` n `229`; crypto_major avg `0.2739` n `8`; equity avg `0.0077` n `88`; fx avg `-0.003` n `6`; index avg `0.0425` n `25`; metal avg `0.0325` n `20`; unknown avg `0.3651` n `765`
- 4h: commodity avg `0.0054` n `12`; crypto_alt avg `0.2713` n `229`; crypto_major avg `-0.0154` n `8`; equity avg `0.5082` n `88`; fx avg `-0.005` n `6`; index avg `0.1748` n `25`; metal avg `0.1869` n `20`; unknown avg `1.9457` n `765`
- 24h: commodity avg `0.1106` n `12`; crypto_alt avg `2.3376` n `228`; crypto_major avg `3.1296` n `8`; equity avg `-2.02` n `88`; fx avg `-0.1495` n `6`; index avg `-0.3753` n `25`; metal avg `0.9932` n `20`; unknown avg `3.3547` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
