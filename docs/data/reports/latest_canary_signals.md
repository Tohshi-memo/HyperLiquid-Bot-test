# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T18:56:06.660975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.0667` n `233`; crypto_major avg `0.0262` n `8`; equity avg `-0.0089` n `136`; fx avg `-0.0036` n `6`; index avg `-0.0051` n `27`; metal avg `0.0066` n `20`; unknown avg `-0.5106` n `832`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0534` n `233`; crypto_major avg `0.0461` n `8`; equity avg `0.0195` n `136`; fx avg `0.0013` n `6`; index avg `0.0032` n `27`; metal avg `0.0053` n `20`; unknown avg `-0.6111` n `830`
- 4h: commodity avg `0.1034` n `12`; crypto_alt avg `0.0958` n `233`; crypto_major avg `0.4213` n `8`; equity avg `0.2202` n `136`; fx avg `0.0033` n `6`; index avg `-0.0121` n `27`; metal avg `0.0185` n `20`; unknown avg `1.6943` n `766`
- 24h: commodity avg `0.2388` n `12`; crypto_alt avg `0.2001` n `233`; crypto_major avg `-0.5814` n `8`; equity avg `-1.3576` n `136`; fx avg `0.0127` n `6`; index avg `-0.2648` n `26`; metal avg `-0.0699` n `20`; unknown avg `1.296` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
