# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T02:37:24.360565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `0.2744` n `230`; crypto_major avg `0.328` n `8`; equity avg `-0.0147` n `121`; fx avg `-0.0091` n `6`; index avg `0.001` n `25`; metal avg `0.0012` n `20`; unknown avg `0.2073` n `794`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.9375` n `230`; crypto_major avg `-0.6652` n `8`; equity avg `0.0142` n `121`; fx avg `0.0119` n `6`; index avg `0.0132` n `25`; metal avg `-0.0009` n `20`; unknown avg `3.4742` n `794`
- 4h: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.7149` n `230`; crypto_major avg `0.2723` n `8`; equity avg `0.2158` n `121`; fx avg `0.0304` n `6`; index avg `0.0355` n `25`; metal avg `0.0107` n `20`; unknown avg `2.6932` n `794`
- 24h: commodity avg `0.0757` n `12`; crypto_alt avg `-4.8922` n `230`; crypto_major avg `-1.1909` n `8`; equity avg `-0.2272` n `121`; fx avg `0.1001` n `6`; index avg `-0.0345` n `25`; metal avg `-0.0252` n `20`; unknown avg `3.4139` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
