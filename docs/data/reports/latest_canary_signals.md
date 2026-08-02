# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T14:04:17.094741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.099` n `12`; crypto_alt avg `-0.006` n `230`; crypto_major avg `-0.0313` n `8`; equity avg `0.0111` n `102`; fx avg `-0.0119` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0107` n `782`
- 1h: commodity avg `-0.1121` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `0.058` n `8`; equity avg `-0.0051` n `102`; fx avg `-0.0396` n `6`; index avg `0.0104` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0489` n `782`
- 4h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.3494` n `230`; crypto_major avg `-0.3181` n `8`; equity avg `-0.2498` n `102`; fx avg `-0.0555` n `6`; index avg `-0.0407` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.1405` n `782`
- 24h: commodity avg `-1.1061` n `12`; crypto_alt avg `0.0457` n `230`; crypto_major avg `-0.0204` n `8`; equity avg `0.8383` n `102`; fx avg `-0.147` n `6`; index avg `0.2261` n `25`; metal avg `0.2452` n `20`; unknown avg `0.2113` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
