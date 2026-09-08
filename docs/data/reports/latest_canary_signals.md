# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T04:07:29.009277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.1879` n `232`; crypto_major avg `-0.0948` n `8`; equity avg `0.077` n `134`; fx avg `0.0324` n `6`; index avg `0.0071` n `26`; metal avg `0.0442` n `20`; unknown avg `-0.1925` n `795`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `0.0697` n `232`; crypto_major avg `0.0491` n `8`; equity avg `0.3109` n `134`; fx avg `0.0258` n `6`; index avg `0.051` n `26`; metal avg `0.1415` n `20`; unknown avg `0.7487` n `795`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.1328` n `232`; crypto_major avg `-0.4875` n `8`; equity avg `0.6597` n `134`; fx avg `-0.0564` n `6`; index avg `0.159` n `26`; metal avg `0.1516` n `20`; unknown avg `4.7167` n `783`
- 24h: commodity avg `0.1199` n `12`; crypto_alt avg `0.7752` n `232`; crypto_major avg `-0.8326` n `8`; equity avg `0.7817` n `134`; fx avg `-0.3034` n `6`; index avg `0.2211` n `26`; metal avg `0.4328` n `20`; unknown avg `7374.111` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
