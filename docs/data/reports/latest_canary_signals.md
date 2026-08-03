# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T00:22:29.998828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.061` n `230`; crypto_major avg `-0.0782` n `8`; equity avg `0.3921` n `102`; fx avg `-0.0024` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0522` n `20`; unknown avg `-0.0059` n `784`
- 1h: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.147` n `230`; crypto_major avg `-0.2138` n `8`; equity avg `0.0564` n `102`; fx avg `-0.0959` n `6`; index avg `-0.1102` n `25`; metal avg `-0.0674` n `20`; unknown avg `-0.0487` n `784`
- 4h: commodity avg `-0.1039` n `12`; crypto_alt avg `-0.1808` n `230`; crypto_major avg `-0.1639` n `8`; equity avg `0.256` n `102`; fx avg `-0.0036` n `6`; index avg `-0.0794` n `25`; metal avg `-0.1715` n `20`; unknown avg `1.8165` n `783`
- 24h: commodity avg `-1.0871` n `12`; crypto_alt avg `0.7086` n `230`; crypto_major avg `1.2498` n `8`; equity avg `1.4169` n `102`; fx avg `-0.0424` n `6`; index avg `0.1938` n `25`; metal avg `0.1456` n `20`; unknown avg `1.5478` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
