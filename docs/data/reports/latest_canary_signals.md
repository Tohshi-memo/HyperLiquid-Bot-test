# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T00:52:29.379805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `0.0929` n `233`; crypto_major avg `0.0182` n `8`; equity avg `0.0651` n `136`; fx avg `-0.0185` n `6`; index avg `0.0348` n `27`; metal avg `0.0881` n `20`; unknown avg `-0.1111` n `826`
- 1h: commodity avg `0.0741` n `12`; crypto_alt avg `0.3024` n `233`; crypto_major avg `0.2679` n `8`; equity avg `0.0412` n `136`; fx avg `0.006` n `6`; index avg `-0.0033` n `27`; metal avg `0.1242` n `20`; unknown avg `13.2118` n `818`
- 4h: commodity avg `0.3496` n `12`; crypto_alt avg `-1.5271` n `233`; crypto_major avg `-1.027` n `8`; equity avg `-0.6124` n `136`; fx avg `0.0285` n `6`; index avg `-0.148` n `27`; metal avg `0.0089` n `20`; unknown avg `3.2837` n `798`
- 24h: commodity avg `0.6984` n `12`; crypto_alt avg `-1.5569` n `233`; crypto_major avg `-1.3956` n `8`; equity avg `-1.7336` n `136`; fx avg `0.044` n `6`; index avg `-0.3752` n `26`; metal avg `-0.0617` n `20`; unknown avg `1.5222` n `682`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
