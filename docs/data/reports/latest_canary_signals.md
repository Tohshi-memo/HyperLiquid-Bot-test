# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T10:07:30.214048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.1299` n `230`; crypto_major avg `0.1482` n `8`; equity avg `0.0151` n `102`; fx avg `0.0049` n `6`; index avg `0.005` n `25`; metal avg `0.0387` n `20`; unknown avg `0.0905` n `779`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0955` n `230`; crypto_major avg `0.266` n `8`; equity avg `0.2793` n `102`; fx avg `0.0028` n `6`; index avg `0.0578` n `25`; metal avg `0.0983` n `20`; unknown avg `0.0357` n `779`
- 4h: commodity avg `-0.1688` n `12`; crypto_alt avg `0.2772` n `230`; crypto_major avg `0.5822` n `8`; equity avg `0.3418` n `102`; fx avg `0.0233` n `6`; index avg `0.0295` n `25`; metal avg `0.4071` n `20`; unknown avg `0.0935` n `771`
- 24h: commodity avg `0.5544` n `12`; crypto_alt avg `-0.2679` n `230`; crypto_major avg `-0.1801` n `8`; equity avg `-3.2581` n `102`; fx avg `0.0103` n `6`; index avg `-0.4787` n `25`; metal avg `0.3907` n `20`; unknown avg `-0.0724` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
