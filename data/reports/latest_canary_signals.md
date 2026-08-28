# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T00:00:23.323939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.0545` n `231`; crypto_major avg `-0.0824` n `8`; equity avg `0.0475` n `127`; fx avg `-0.0054` n `6`; index avg `0.0209` n `26`; metal avg `0.0001` n `20`; unknown avg `0.0076` n `792`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.0971` n `231`; crypto_major avg `-0.0332` n `8`; equity avg `-0.0429` n `127`; fx avg `-0.0124` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0628` n `20`; unknown avg `-0.0064` n `792`
- 4h: commodity avg `-0.0506` n `12`; crypto_alt avg `0.3024` n `231`; crypto_major avg `0.233` n `8`; equity avg `-0.5079` n `127`; fx avg `-0.0114` n `6`; index avg `-0.0452` n `26`; metal avg `-0.0464` n `20`; unknown avg `-0.1677` n `792`
- 24h: commodity avg `0.3608` n `12`; crypto_alt avg `0.8464` n `231`; crypto_major avg `2.2187` n `8`; equity avg `-0.5274` n `127`; fx avg `-0.0208` n `6`; index avg `-0.1138` n `26`; metal avg `0.0289` n `20`; unknown avg `0.9003` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
