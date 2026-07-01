# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T20:47:15.720395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.1686` n `228`; crypto_major avg `0.1229` n `8`; equity avg `0.0988` n `88`; fx avg `-0.0042` n `6`; index avg `0.0077` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.55` n `763`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.1765` n `228`; crypto_major avg `-0.1897` n `8`; equity avg `-0.2612` n `88`; fx avg `0.0019` n `6`; index avg `-0.0537` n `25`; metal avg `-0.0749` n `20`; unknown avg `1.3191` n `763`
- 4h: commodity avg `-0.1221` n `12`; crypto_alt avg `-0.5737` n `228`; crypto_major avg `-0.4682` n `8`; equity avg `-0.9149` n `88`; fx avg `0.0014` n `6`; index avg `-0.1507` n `25`; metal avg `-0.3609` n `20`; unknown avg `0.6793` n `761`
- 24h: commodity avg `-0.5983` n `12`; crypto_alt avg `1.6736` n `228`; crypto_major avg `1.1534` n `8`; equity avg `-1.6784` n `88`; fx avg `-0.0022` n `6`; index avg `-0.531` n `25`; metal avg `0.1592` n `20`; unknown avg `0.7286` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
