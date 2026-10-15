# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T22:29:39.971755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `-0.0564` n `236`; crypto_major avg `-0.0521` n `8`; equity avg `-0.0528` n `151`; fx avg `-0.0107` n `6`; index avg `-0.0065` n `26`; metal avg `-0.014` n `20`; unknown avg `-0.0486` n `1120`
- 1h: commodity avg `0.0175` n `13`; crypto_alt avg `0.0174` n `236`; crypto_major avg `0.0776` n `8`; equity avg `0.2538` n `151`; fx avg `0.0139` n `6`; index avg `0.0174` n `26`; metal avg `-0.0128` n `20`; unknown avg `-0.006` n `1102`
- 4h: commodity avg `-0.1852` n `13`; crypto_alt avg `0.4759` n `236`; crypto_major avg `0.5131` n `8`; equity avg `1.4586` n `151`; fx avg `-0.0196` n `6`; index avg `0.1485` n `26`; metal avg `0.0903` n `20`; unknown avg `0.2289` n `1020`
- 24h: commodity avg `-0.2477` n `13`; crypto_alt avg `0.7834` n `236`; crypto_major avg `0.903` n `8`; equity avg `1.1632` n `151`; fx avg `0.1953` n `6`; index avg `0.0275` n `26`; metal avg `0.4785` n `20`; unknown avg `24.8547` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0978`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.086`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0754`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0753`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0487`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `666`, weak_sample_signal
