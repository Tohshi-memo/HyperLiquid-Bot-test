# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T20:22:27.518147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0713` n `12`; crypto_alt avg `-0.0754` n `230`; crypto_major avg `-0.0266` n `8`; equity avg `0.0113` n `102`; fx avg `-0.0176` n `6`; index avg `0.0003` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0476` n `783`
- 1h: commodity avg `0.0798` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `0.0487` n `8`; equity avg `0.0805` n `102`; fx avg `0.0429` n `6`; index avg `0.0283` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.1098` n `783`
- 4h: commodity avg `0.0661` n `12`; crypto_alt avg `0.1743` n `230`; crypto_major avg `0.7878` n `8`; equity avg `0.4933` n `102`; fx avg `0.085` n `6`; index avg `0.0708` n `25`; metal avg `0.0927` n `20`; unknown avg `0.4467` n `782`
- 24h: commodity avg `-1.2573` n `12`; crypto_alt avg `1.3142` n `230`; crypto_major avg `1.9191` n `8`; equity avg `1.723` n `102`; fx avg `-0.065` n `6`; index avg `0.3567` n `25`; metal avg `0.3622` n `20`; unknown avg `1.6307` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
