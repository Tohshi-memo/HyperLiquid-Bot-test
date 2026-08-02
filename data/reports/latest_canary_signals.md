# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T16:26:51.901947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.131` n `12`; crypto_alt avg `-0.0054` n `230`; crypto_major avg `0.0007` n `8`; equity avg `-0.0322` n `102`; fx avg `0.0051` n `6`; index avg `-0.0034` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0037` n `782`
- 1h: commodity avg `-0.0884` n `12`; crypto_alt avg `-0.1013` n `230`; crypto_major avg `-0.103` n `8`; equity avg `-0.03` n `102`; fx avg `-0.002` n `6`; index avg `0.0084` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.1123` n `782`
- 4h: commodity avg `-0.1379` n `12`; crypto_alt avg `-0.1183` n `230`; crypto_major avg `0.0174` n `8`; equity avg `0.05` n `102`; fx avg `-0.0528` n `6`; index avg `0.0256` n `25`; metal avg `0.0475` n `20`; unknown avg `1.0691` n `782`
- 24h: commodity avg `-1.2837` n `12`; crypto_alt avg `0.0644` n `230`; crypto_major avg `0.0832` n `8`; equity avg `0.9603` n `102`; fx avg `-0.1492` n `6`; index avg `0.2422` n `25`; metal avg `0.2688` n `20`; unknown avg `1.4437` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
