# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T10:52:25.883450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `-0.045` n `228`; crypto_major avg `-0.2186` n `8`; equity avg `-0.0026` n `88`; fx avg `0.003` n `6`; index avg `0.0019` n `23`; metal avg `-0.0298` n `20`; unknown avg `-0.0393` n `765`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.0588` n `228`; crypto_major avg `-0.6034` n `8`; equity avg `0.1134` n `88`; fx avg `0.0227` n `6`; index avg `0.0241` n `23`; metal avg `-0.0026` n `20`; unknown avg `-0.1179` n `765`
- 4h: commodity avg `-0.1033` n `12`; crypto_alt avg `0.2806` n `228`; crypto_major avg `-0.4868` n `8`; equity avg `0.1025` n `88`; fx avg `0.0304` n `6`; index avg `0.0269` n `23`; metal avg `0.1652` n `20`; unknown avg `0.0577` n `763`
- 24h: commodity avg `-0.3782` n `12`; crypto_alt avg `-0.2566` n `228`; crypto_major avg `-1.0069` n `8`; equity avg `0.6165` n `88`; fx avg `0.1289` n `6`; index avg `0.027` n `23`; metal avg `-0.7819` n `20`; unknown avg `-0.0287` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
