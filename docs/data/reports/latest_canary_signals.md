# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T13:52:28.327714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0307` n `12`; crypto_alt avg `0.542` n `228`; crypto_major avg `0.5916` n `8`; equity avg `0.6442` n `88`; fx avg `0.023` n `6`; index avg `0.0798` n `23`; metal avg `0.4048` n `20`; unknown avg `0.3728` n `765`
- 1h: commodity avg `0.069` n `12`; crypto_alt avg `1.1181` n `228`; crypto_major avg `1.4918` n `8`; equity avg `0.5291` n `88`; fx avg `0.0103` n `6`; index avg `-0.0297` n `23`; metal avg `0.7291` n `20`; unknown avg `0.6656` n `765`
- 4h: commodity avg `-0.0324` n `12`; crypto_alt avg `0.7664` n `228`; crypto_major avg `0.5173` n `8`; equity avg `-0.2991` n `88`; fx avg `-0.0201` n `6`; index avg `-0.0849` n `23`; metal avg `1.1456` n `20`; unknown avg `0.0126` n `765`
- 24h: commodity avg `-0.5576` n `12`; crypto_alt avg `1.5221` n `228`; crypto_major avg `1.0931` n `8`; equity avg `0.2064` n `88`; fx avg `0.1023` n `6`; index avg `-0.216` n `23`; metal avg `0.5147` n `20`; unknown avg `-0.1023` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
