# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T22:22:36.797674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0934` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.102` n `8`; equity avg `-0.0885` n `102`; fx avg `-0.0011` n `6`; index avg `-0.0277` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0142` n `782`
- 1h: commodity avg `-0.1465` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `0.119` n `8`; equity avg `0.2187` n `102`; fx avg `0.0164` n `6`; index avg `0.0076` n `25`; metal avg `0.0261` n `20`; unknown avg `0.1916` n `782`
- 4h: commodity avg `-0.0691` n `12`; crypto_alt avg `-0.1246` n `230`; crypto_major avg `-0.03` n `8`; equity avg `0.2119` n `102`; fx avg `0.0407` n `6`; index avg `-0.0079` n `25`; metal avg `0.0835` n `20`; unknown avg `-0.0373` n `782`
- 24h: commodity avg `-0.1333` n `12`; crypto_alt avg `-0.4141` n `230`; crypto_major avg `-0.8809` n `8`; equity avg `-0.0188` n `102`; fx avg `-0.0607` n `6`; index avg `-0.016` n `25`; metal avg `0.0518` n `20`; unknown avg `-0.0075` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
