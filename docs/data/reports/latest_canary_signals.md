# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T01:52:27.979745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0598` n `12`; crypto_alt avg `0.0091` n `230`; crypto_major avg `0.0188` n `8`; equity avg `0.0267` n `92`; fx avg `0.0216` n `6`; index avg `0.0185` n `25`; metal avg `0.0859` n `20`; unknown avg `-0.059` n `766`
- 1h: commodity avg `-0.1762` n `12`; crypto_alt avg `0.1294` n `230`; crypto_major avg `0.0572` n `8`; equity avg `-0.0597` n `92`; fx avg `-0.0294` n `6`; index avg `0.0442` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.197` n `766`
- 4h: commodity avg `0.1608` n `12`; crypto_alt avg `1.1045` n `230`; crypto_major avg `0.9156` n `8`; equity avg `0.1246` n `92`; fx avg `-0.038` n `6`; index avg `0.0286` n `25`; metal avg `-0.0481` n `20`; unknown avg `0.2176` n `766`
- 24h: commodity avg `0.8866` n `12`; crypto_alt avg `-1.1574` n `230`; crypto_major avg `-1.7713` n `8`; equity avg `-1.5919` n `92`; fx avg `-0.1427` n `6`; index avg `-0.2345` n `25`; metal avg `-0.4062` n `20`; unknown avg `-0.3592` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
