# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:07:27.814990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.2931` n `230`; crypto_major avg `0.1854` n `8`; equity avg `0.017` n `121`; fx avg `0.0033` n `6`; index avg `0.0018` n `25`; metal avg `0.0005` n `20`; unknown avg `0.1936` n `794`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.262` n `230`; crypto_major avg `-0.0744` n `8`; equity avg `-0.0002` n `121`; fx avg `0.0151` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.4521` n `794`
- 4h: commodity avg `0.0304` n `12`; crypto_alt avg `0.8187` n `230`; crypto_major avg `1.3318` n `8`; equity avg `0.065` n `121`; fx avg `0.0327` n `6`; index avg `0.0036` n `25`; metal avg `0.0123` n `20`; unknown avg `1.3677` n `794`
- 24h: commodity avg `-0.0412` n `12`; crypto_alt avg `1.7312` n `230`; crypto_major avg `4.0998` n `8`; equity avg `-0.3736` n `121`; fx avg `0.0558` n `6`; index avg `-0.0526` n `25`; metal avg `-0.1138` n `20`; unknown avg `2.0088` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
