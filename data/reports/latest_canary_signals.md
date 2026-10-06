# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T08:07:29.004784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `0.1795` n `235`; crypto_major avg `0.2325` n `8`; equity avg `0.1165` n `149`; fx avg `0.0065` n `6`; index avg `0.0204` n `26`; metal avg `0.0367` n `20`; unknown avg `0.3592` n `1056`
- 1h: commodity avg `0.0084` n `13`; crypto_alt avg `0.543` n `235`; crypto_major avg `0.4043` n `8`; equity avg `0.2103` n `149`; fx avg `0.0162` n `6`; index avg `0.0547` n `26`; metal avg `0.0982` n `20`; unknown avg `0.4333` n `1048`
- 4h: commodity avg `-0.2286` n `13`; crypto_alt avg `0.5841` n `235`; crypto_major avg `0.0717` n `8`; equity avg `0.228` n `149`; fx avg `-0.0037` n `6`; index avg `0.0563` n `26`; metal avg `0.0226` n `20`; unknown avg `-0.0704` n `976`
- 24h: commodity avg `-0.2604` n `13`; crypto_alt avg `-1.2691` n `235`; crypto_major avg `-0.8722` n `8`; equity avg `0.2532` n `149`; fx avg `0.0562` n `6`; index avg `0.1593` n `26`; metal avg `-0.2027` n `20`; unknown avg `-0.0779` n `858`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
