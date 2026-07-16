# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T19:07:32.704366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0999` n `230`; crypto_major avg `-0.0408` n `8`; equity avg `-0.1643` n `94`; fx avg `0.0046` n `6`; index avg `-0.0337` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0357` n `768`
- 1h: commodity avg `0.1078` n `12`; crypto_alt avg `-0.1229` n `230`; crypto_major avg `0.0067` n `8`; equity avg `-0.1344` n `94`; fx avg `0.007` n `6`; index avg `-0.0393` n `25`; metal avg `-0.0385` n `20`; unknown avg `-0.0904` n `768`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.4086` n `230`; crypto_major avg `-0.9301` n `8`; equity avg `-0.9797` n `94`; fx avg `-0.0218` n `6`; index avg `-0.2048` n `25`; metal avg `-0.2124` n `20`; unknown avg `-0.2533` n `768`
- 24h: commodity avg `-0.2423` n `12`; crypto_alt avg `-1.032` n `230`; crypto_major avg `-2.0806` n `8`; equity avg `-3.6372` n `94`; fx avg `-0.1512` n `6`; index avg `-0.5302` n `25`; metal avg `-0.8289` n `20`; unknown avg `-0.3706` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
