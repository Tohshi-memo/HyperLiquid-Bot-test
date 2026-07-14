# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T02:37:24.655849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.1035` n `230`; crypto_major avg `-0.0705` n `8`; equity avg `-0.1535` n `92`; fx avg `0.0008` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.0175` n `766`
- 1h: commodity avg `-0.1081` n `12`; crypto_alt avg `-0.38` n `230`; crypto_major avg `-0.2189` n `8`; equity avg `-0.6089` n `92`; fx avg `0.0361` n `6`; index avg `-0.1919` n `25`; metal avg `0.1807` n `20`; unknown avg `-0.0862` n `766`
- 4h: commodity avg `0.0733` n `12`; crypto_alt avg `0.4086` n `230`; crypto_major avg `0.4107` n `8`; equity avg `-0.5197` n `92`; fx avg `0.0086` n `6`; index avg `-0.2007` n `25`; metal avg `0.0339` n `20`; unknown avg `0.1075` n `766`
- 24h: commodity avg `0.8363` n `12`; crypto_alt avg `-1.4357` n `230`; crypto_major avg `-1.9404` n `8`; equity avg `-2.3104` n `92`; fx avg `-0.1301` n `6`; index avg `-0.4938` n `25`; metal avg `-0.2186` n `20`; unknown avg `-0.4391` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
