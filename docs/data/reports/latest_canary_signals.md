# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T05:22:36.617807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `0.0705` n `239`; crypto_major avg `0.092` n `8`; equity avg `-0.048` n `168`; fx avg `-0.0019` n `6`; index avg `-0.01` n `27`; metal avg `0.0189` n `20`; unknown avg `1.2305` n `1265`
- 1h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.1377` n `239`; crypto_major avg `0.0039` n `8`; equity avg `-0.0169` n `168`; fx avg `-0.002` n `6`; index avg `0.0019` n `27`; metal avg `0.0855` n `20`; unknown avg `267.0498` n `1261`
- 4h: commodity avg `0.0102` n `13`; crypto_alt avg `0.0369` n `239`; crypto_major avg `0.3778` n `8`; equity avg `-0.0261` n `168`; fx avg `-0.0303` n `6`; index avg `-0.014` n `27`; metal avg `0.1847` n `20`; unknown avg `391.9088` n `1245`
- 24h: commodity avg `0.7755` n `13`; crypto_alt avg `3.2036` n `239`; crypto_major avg `3.4015` n `8`; equity avg `2.8843` n `168`; fx avg `0.017` n `6`; index avg `0.2303` n `27`; metal avg `0.7569` n `20`; unknown avg `768.6487` n `1021`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
