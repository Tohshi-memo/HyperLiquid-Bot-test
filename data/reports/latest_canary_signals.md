# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T04:52:27.218487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.1163` n `230`; crypto_major avg `-0.1796` n `8`; equity avg `0.0499` n `98`; fx avg `-0.0082` n `6`; index avg `0.0447` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.0785` n `769`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.3163` n `230`; crypto_major avg `-0.3324` n `8`; equity avg `0.129` n `98`; fx avg `-0.0148` n `6`; index avg `0.0511` n `25`; metal avg `-0.0524` n `20`; unknown avg `0.1136` n `769`
- 4h: commodity avg `0.0085` n `12`; crypto_alt avg `-0.2321` n `230`; crypto_major avg `-0.1139` n `8`; equity avg `0.0302` n `98`; fx avg `-0.0373` n `6`; index avg `0.0456` n `25`; metal avg `0.0716` n `20`; unknown avg `-0.3313` n `769`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.1338` n `230`; crypto_major avg `-0.0348` n `8`; equity avg `0.5136` n `97`; fx avg `-0.0154` n `6`; index avg `0.1395` n `25`; metal avg `0.0914` n `20`; unknown avg `-0.0118` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0971`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
