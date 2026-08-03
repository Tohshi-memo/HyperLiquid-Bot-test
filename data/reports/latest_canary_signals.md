# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T09:22:29.188178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0866` n `12`; crypto_alt avg `0.1108` n `230`; crypto_major avg `0.1516` n `8`; equity avg `-0.0025` n `102`; fx avg `-0.0042` n `6`; index avg `-0.004` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.0193` n `784`
- 1h: commodity avg `-0.0536` n `12`; crypto_alt avg `0.3705` n `230`; crypto_major avg `0.4351` n `8`; equity avg `0.2883` n `102`; fx avg `0.0179` n `6`; index avg `0.0219` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0931` n `784`
- 4h: commodity avg `0.1055` n `12`; crypto_alt avg `-0.0393` n `230`; crypto_major avg `-0.1338` n `8`; equity avg `-0.5228` n `102`; fx avg `0.0194` n `6`; index avg `-0.063` n `25`; metal avg `-0.0185` n `20`; unknown avg `-0.0406` n `768`
- 24h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.9634` n `230`; crypto_major avg `-0.5103` n `8`; equity avg `0.1674` n `102`; fx avg `-0.1702` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0906` n `20`; unknown avg `1.0017` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
