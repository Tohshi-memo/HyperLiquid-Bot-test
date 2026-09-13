# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T14:07:35.614882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `0.2012` n `233`; crypto_major avg `0.0229` n `8`; equity avg `0.0301` n `136`; fx avg `0.0043` n `6`; index avg `0.0159` n `27`; metal avg `0.0037` n `20`; unknown avg `0.4533` n `836`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.6609` n `233`; crypto_major avg `0.3081` n `8`; equity avg `0.2436` n `136`; fx avg `0.0066` n `6`; index avg `0.0626` n `27`; metal avg `0.0015` n `20`; unknown avg `0.622` n `836`
- 4h: commodity avg `0.1505` n `12`; crypto_alt avg `0.5236` n `233`; crypto_major avg `0.1035` n `8`; equity avg `-0.0681` n `136`; fx avg `0.0049` n `6`; index avg `0.0012` n `27`; metal avg `-0.0222` n `20`; unknown avg `0.3202` n `826`
- 24h: commodity avg `0.261` n `12`; crypto_alt avg `0.1111` n `233`; crypto_major avg `-1.6788` n `8`; equity avg `-1.6713` n `136`; fx avg `0.0053` n `6`; index avg `-0.2481` n `26`; metal avg `-0.0838` n `20`; unknown avg `0.0449` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
