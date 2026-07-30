# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T05:22:26.303332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1311` n `12`; crypto_alt avg `0.0463` n `230`; crypto_major avg `0.0008` n `8`; equity avg `0.2583` n `102`; fx avg `0.0005` n `6`; index avg `0.0395` n `25`; metal avg `0.0378` n `20`; unknown avg `-0.1289` n `779`
- 1h: commodity avg `0.2146` n `12`; crypto_alt avg `-0.1257` n `230`; crypto_major avg `-0.1122` n `8`; equity avg `-0.0633` n `102`; fx avg `-0.0217` n `6`; index avg `-0.0152` n `25`; metal avg `-0.0529` n `20`; unknown avg `-0.2009` n `779`
- 4h: commodity avg `0.1694` n `12`; crypto_alt avg `0.0179` n `230`; crypto_major avg `-0.1729` n `8`; equity avg `-1.1151` n `102`; fx avg `-0.0626` n `6`; index avg `-0.1291` n `25`; metal avg `-0.3449` n `20`; unknown avg `-0.0255` n `779`
- 24h: commodity avg `0.775` n `12`; crypto_alt avg `-0.3975` n `230`; crypto_major avg `-0.4522` n `8`; equity avg `-2.4185` n `102`; fx avg `0.0681` n `6`; index avg `-0.1019` n `25`; metal avg `-0.035` n `20`; unknown avg `-0.5743` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
