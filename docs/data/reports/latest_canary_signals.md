# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T20:37:26.253559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.0497` n `233`; crypto_major avg `0.0664` n `8`; equity avg `0.0294` n `136`; fx avg `0.0012` n `6`; index avg `0.0105` n `27`; metal avg `-0.0096` n `20`; unknown avg `0.4927` n `834`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.2111` n `233`; crypto_major avg `0.2714` n `8`; equity avg `0.0391` n `136`; fx avg `0.003` n `6`; index avg `0.0216` n `27`; metal avg `-0.0181` n `20`; unknown avg `3.6168` n `826`
- 4h: commodity avg `0.0872` n `12`; crypto_alt avg `0.3497` n `233`; crypto_major avg `0.4049` n `8`; equity avg `0.0751` n `136`; fx avg `0.0045` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0272` n `20`; unknown avg `6.6033` n `760`
- 24h: commodity avg `0.3172` n `12`; crypto_alt avg `0.0311` n `233`; crypto_major avg `-0.4779` n `8`; equity avg `-1.1573` n `136`; fx avg `0.019` n `6`; index avg `-0.2307` n `26`; metal avg `-0.0987` n `20`; unknown avg `4.0733` n `714`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
