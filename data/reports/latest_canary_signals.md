# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T20:22:30.127579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0315` n `233`; crypto_major avg `0.1048` n `8`; equity avg `-0.0032` n `136`; fx avg `0.0033` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0172` n `20`; unknown avg `3.7696` n `834`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `0.0405` n `233`; crypto_major avg `0.157` n `8`; equity avg `-0.054` n `136`; fx avg `0.0032` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0084` n `20`; unknown avg `3.3417` n `832`
- 4h: commodity avg `0.0738` n `12`; crypto_alt avg `0.2828` n `233`; crypto_major avg `0.2978` n `8`; equity avg `0.0357` n `136`; fx avg `0.0039` n `6`; index avg `-0.0306` n `27`; metal avg `-0.0138` n `20`; unknown avg `5.505` n `760`
- 24h: commodity avg `0.3013` n `12`; crypto_alt avg `0.018` n `233`; crypto_major avg `-0.5426` n `8`; equity avg `-1.2358` n `136`; fx avg `0.0152` n `6`; index avg `-0.2491` n `26`; metal avg `-0.0935` n `20`; unknown avg `3.5057` n `714`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
