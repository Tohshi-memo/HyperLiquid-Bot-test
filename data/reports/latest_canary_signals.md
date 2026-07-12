# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T13:37:27.760693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0596` n `230`; crypto_major avg `0.0405` n `8`; equity avg `-0.02` n `92`; fx avg `-0.0008` n `6`; index avg `0.0383` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.0025` n `765`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `0.0519` n `230`; crypto_major avg `0.1477` n `8`; equity avg `0.0092` n `92`; fx avg `0.0006` n `6`; index avg `0.035` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.0446` n `765`
- 4h: commodity avg `-0.0799` n `12`; crypto_alt avg `0.1912` n `230`; crypto_major avg `0.5055` n `8`; equity avg `0.0924` n `92`; fx avg `0.0037` n `6`; index avg `0.0379` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.1969` n `763`
- 24h: commodity avg `0.4217` n `12`; crypto_alt avg `-1.0073` n `230`; crypto_major avg `-0.4047` n `8`; equity avg `-0.0567` n `92`; fx avg `0.0106` n `6`; index avg `-0.0861` n `25`; metal avg `-0.1141` n `20`; unknown avg `0.1124` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
