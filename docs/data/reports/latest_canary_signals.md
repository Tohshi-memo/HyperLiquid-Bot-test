# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T17:40:12.181938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.033` n `12`; crypto_alt avg `0.0527` n `230`; crypto_major avg `0.1298` n `8`; equity avg `-0.0596` n `102`; fx avg `-0.0043` n `6`; index avg `0.0013` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0297` n `782`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0572` n `230`; crypto_major avg `0.2426` n `8`; equity avg `0.2082` n `102`; fx avg `-0.0024` n `6`; index avg `0.0346` n `25`; metal avg `0.0104` n `20`; unknown avg `0.1062` n `782`
- 4h: commodity avg `-0.2248` n `12`; crypto_alt avg `0.2437` n `230`; crypto_major avg `0.6397` n `8`; equity avg `0.3117` n `102`; fx avg `-0.0289` n `6`; index avg `0.064` n `25`; metal avg `0.048` n `20`; unknown avg `1.2351` n `782`
- 24h: commodity avg `-1.3371` n `12`; crypto_alt avg `0.8258` n `230`; crypto_major avg `1.2006` n `8`; equity avg `1.291` n `102`; fx avg `-0.146` n `6`; index avg `0.2848` n `25`; metal avg `0.3014` n `20`; unknown avg `1.5746` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
