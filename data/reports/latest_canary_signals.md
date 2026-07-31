# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T06:37:26.321643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0473` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.0129` n `8`; equity avg `-0.6972` n `102`; fx avg `-0.0592` n `6`; index avg `-0.1473` n `25`; metal avg `-0.0691` n `20`; unknown avg `-0.003` n `779`
- 1h: commodity avg `0.119` n `12`; crypto_alt avg `0.1294` n `230`; crypto_major avg `0.1786` n `8`; equity avg `-0.5576` n `102`; fx avg `-0.1134` n `6`; index avg `-0.0933` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.0015` n `747`
- 4h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.2199` n `230`; crypto_major avg `0.3267` n `8`; equity avg `0.4718` n `102`; fx avg `-0.0785` n `6`; index avg `0.1175` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0315` n `747`
- 24h: commodity avg `-0.6043` n `12`; crypto_alt avg `0.1288` n `230`; crypto_major avg `1.1384` n `8`; equity avg `8.3185` n `102`; fx avg `-0.1819` n `6`; index avg `1.2491` n `25`; metal avg `0.6864` n `20`; unknown avg `0.0757` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
