# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T07:00:03.161693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0559` n `12`; crypto_alt avg `0.0547` n `232`; crypto_major avg `-0.0248` n `8`; equity avg `-0.0339` n `128`; fx avg `-0.0033` n `6`; index avg `-0.008` n `26`; metal avg `-0.0241` n `20`; unknown avg `0.0117` n `791`
- 1h: commodity avg `-0.1813` n `12`; crypto_alt avg `0.2418` n `232`; crypto_major avg `0.1686` n `8`; equity avg `0.3258` n `128`; fx avg `-0.0268` n `6`; index avg `0.0647` n `26`; metal avg `0.1113` n `20`; unknown avg `0.2167` n `789`
- 4h: commodity avg `-0.0291` n `12`; crypto_alt avg `1.0495` n `231`; crypto_major avg `0.8323` n `8`; equity avg `1.1338` n `128`; fx avg `-0.0525` n `6`; index avg `0.1901` n `26`; metal avg `0.1682` n `20`; unknown avg `0.3866` n `773`
- 24h: commodity avg `0.3182` n `12`; crypto_alt avg `0.017` n `231`; crypto_major avg `-1.5464` n `8`; equity avg `-0.1744` n `128`; fx avg `-0.1045` n `6`; index avg `-0.0459` n `26`; metal avg `-0.225` n `20`; unknown avg `-0.4374` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
