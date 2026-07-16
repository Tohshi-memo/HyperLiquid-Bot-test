# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T17:22:28.701237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.2586` n `230`; crypto_major avg `-0.3081` n `8`; equity avg `-0.1401` n `94`; fx avg `0.0081` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0286` n `20`; unknown avg `-0.1448` n `768`
- 1h: commodity avg `-0.1381` n `12`; crypto_alt avg `-0.4157` n `230`; crypto_major avg `-0.6812` n `8`; equity avg `-0.0635` n `94`; fx avg `0.0001` n `6`; index avg `-0.0512` n `25`; metal avg `-0.0573` n `20`; unknown avg `-0.0562` n `768`
- 4h: commodity avg `-0.5176` n `12`; crypto_alt avg `-0.2896` n `230`; crypto_major avg `-0.8575` n `8`; equity avg `-1.8354` n `94`; fx avg `-0.0452` n `6`; index avg `-0.1585` n `25`; metal avg `-0.2015` n `20`; unknown avg `-0.2994` n `768`
- 24h: commodity avg `-0.2424` n `12`; crypto_alt avg `-0.7885` n `230`; crypto_major avg `-2.0506` n `8`; equity avg `-3.1408` n `94`; fx avg `-0.1374` n `6`; index avg `-0.3535` n `25`; metal avg `-0.3459` n `20`; unknown avg `-0.3173` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
