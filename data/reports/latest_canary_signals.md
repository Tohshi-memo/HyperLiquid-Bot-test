# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T17:52:26.388341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `0.1481` n `8`; equity avg `0.0611` n `102`; fx avg `-0.0157` n `6`; index avg `0.0205` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.025` n `779`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.1276` n `230`; crypto_major avg `0.1658` n `8`; equity avg `0.2709` n `102`; fx avg `-0.0754` n `6`; index avg `0.0499` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0882` n `779`
- 4h: commodity avg `0.1931` n `12`; crypto_alt avg `-0.2063` n `230`; crypto_major avg `0.5811` n `8`; equity avg `1.0724` n `102`; fx avg `-0.0551` n `6`; index avg `0.1501` n `25`; metal avg `0.1357` n `20`; unknown avg `0.0945` n `779`
- 24h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.3575` n `230`; crypto_major avg `1.1483` n `8`; equity avg `4.2454` n `102`; fx avg `-0.3666` n `6`; index avg `0.4276` n `25`; metal avg `0.741` n `18`; unknown avg `-0.0948` n `723`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
