# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T08:37:15.631382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1553` n `12`; crypto_alt avg `0.0736` n `228`; crypto_major avg `-0.0956` n `8`; equity avg `-0.0014` n `66`; fx avg `-0.0001` n `6`; index avg `-0.0327` n `23`; metal avg `-0.0645` n `18`; unknown avg `0.1114` n `386`
- 1h: commodity avg `-0.1402` n `12`; crypto_alt avg `0.3136` n `228`; crypto_major avg `0.5064` n `8`; equity avg `0.4328` n `66`; fx avg `0.0373` n `6`; index avg `0.2576` n `23`; metal avg `0.3945` n `18`; unknown avg `1.0385` n `385`
- 4h: commodity avg `0.0124` n `12`; crypto_alt avg `0.2252` n `228`; crypto_major avg `0.534` n `8`; equity avg `0.0493` n `66`; fx avg `0.0058` n `6`; index avg `-0.0034` n `23`; metal avg `-0.196` n `18`; unknown avg `0.974` n `374`
- 24h: commodity avg `-1.8037` n `12`; crypto_alt avg `2.7679` n `228`; crypto_major avg `3.494` n `8`; equity avg `1.7542` n `66`; fx avg `0.0958` n `6`; index avg `1.3165` n `23`; metal avg `0.3551` n `18`; unknown avg `5.7672` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
