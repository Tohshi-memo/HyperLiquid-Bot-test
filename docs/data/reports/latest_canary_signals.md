# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T17:22:32.178729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1887` n `231`; crypto_major avg `-0.1381` n `8`; equity avg `-0.0109` n `128`; fx avg `0.0` n `6`; index avg `0.0011` n `26`; metal avg `0.0047` n `20`; unknown avg `0.0239` n `792`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.1756` n `231`; crypto_major avg `-0.0029` n `8`; equity avg `-0.0014` n `128`; fx avg `-0.0062` n `6`; index avg `-0.0061` n `26`; metal avg `0.012` n `20`; unknown avg `0.0194` n `792`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.4671` n `231`; crypto_major avg `0.6064` n `8`; equity avg `0.0298` n `128`; fx avg `-0.0036` n `6`; index avg `-0.0011` n `26`; metal avg `0.0479` n `20`; unknown avg `0.1847` n `778`
- 24h: commodity avg `0.0191` n `12`; crypto_alt avg `0.106` n `231`; crypto_major avg `0.0366` n `8`; equity avg `0.1938` n `128`; fx avg `-0.0539` n `6`; index avg `0.0348` n `26`; metal avg `-0.0537` n `20`; unknown avg `-0.0245` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
