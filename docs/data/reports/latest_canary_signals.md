# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T02:52:24.282642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.0084` n `230`; crypto_major avg `-0.1971` n `8`; equity avg `-0.0249` n `121`; fx avg `0.0088` n `6`; index avg `0.0063` n `25`; metal avg `0.0859` n `20`; unknown avg `1.3355` n `793`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.0736` n `230`; crypto_major avg `-0.5174` n `8`; equity avg `0.3341` n `121`; fx avg `0.0122` n `6`; index avg `0.0641` n `25`; metal avg `0.1658` n `20`; unknown avg `1.2088` n `793`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `1.028` n `230`; crypto_major avg `1.6291` n `8`; equity avg `0.9335` n `121`; fx avg `-0.0926` n `6`; index avg `0.1329` n `25`; metal avg `0.2855` n `20`; unknown avg `-0.1188` n `793`
- 24h: commodity avg `0.3571` n `12`; crypto_alt avg `5.3965` n `230`; crypto_major avg `6.9407` n `8`; equity avg `-0.174` n `121`; fx avg `-0.0105` n `6`; index avg `-0.0484` n `25`; metal avg `0.6027` n `20`; unknown avg `2.6192` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
