# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T14:22:33.364627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2929` n `12`; crypto_alt avg `0.047` n `230`; crypto_major avg `0.0651` n `8`; equity avg `0.11` n `92`; fx avg `-0.0135` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0668` n `20`; unknown avg `0.1426` n `766`
- 1h: commodity avg `0.318` n `12`; crypto_alt avg `0.1591` n `230`; crypto_major avg `0.0886` n `8`; equity avg `-0.4322` n `92`; fx avg `-0.0095` n `6`; index avg `-0.051` n `25`; metal avg `-0.2642` n `20`; unknown avg `0.1181` n `766`
- 4h: commodity avg `0.247` n `12`; crypto_alt avg `-0.3483` n `230`; crypto_major avg `-0.6469` n `8`; equity avg `-0.6474` n `92`; fx avg `0.0141` n `6`; index avg `-0.0594` n `25`; metal avg `-0.218` n `20`; unknown avg `0.2236` n `766`
- 24h: commodity avg `0.0661` n `12`; crypto_alt avg `-1.2568` n `230`; crypto_major avg `-2.0897` n `8`; equity avg `-2.6463` n `92`; fx avg `-0.076` n `6`; index avg `-0.486` n `25`; metal avg `-0.4098` n `20`; unknown avg `-0.1058` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
