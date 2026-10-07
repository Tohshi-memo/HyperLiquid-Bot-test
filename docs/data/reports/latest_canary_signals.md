# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T17:07:35.595996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1227` n `13`; crypto_alt avg `-0.1269` n `235`; crypto_major avg `-0.0491` n `8`; equity avg `0.1165` n `150`; fx avg `-0.021` n `6`; index avg `0.0325` n `26`; metal avg `0.0453` n `20`; unknown avg `-0.1107` n `1074`
- 1h: commodity avg `-0.0369` n `13`; crypto_alt avg `-0.3146` n `235`; crypto_major avg `-0.2621` n `8`; equity avg `-0.0343` n `150`; fx avg `-0.0341` n `6`; index avg `0.0176` n `26`; metal avg `0.0242` n `20`; unknown avg `-0.0456` n `1074`
- 4h: commodity avg `-0.2885` n `13`; crypto_alt avg `0.1328` n `235`; crypto_major avg `-0.1174` n `8`; equity avg `0.2162` n `150`; fx avg `-0.0172` n `6`; index avg `0.0658` n `26`; metal avg `0.1775` n `20`; unknown avg `0.0708` n `1022`
- 24h: commodity avg `0.5499` n `13`; crypto_alt avg `-4.7257` n `235`; crypto_major avg `-3.3417` n `8`; equity avg `-1.5503` n `150`; fx avg `-0.1941` n `6`; index avg `-0.2619` n `26`; metal avg `-0.5484` n `20`; unknown avg `15.2524` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1354`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1346`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0876`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0762`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `669`, weak_sample_signal
