# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T05:22:27.825243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `12`; crypto_alt avg `-0.0466` n `228`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0643` n `88`; fx avg `0.0051` n `6`; index avg `-0.0204` n `23`; metal avg `-0.1006` n `20`; unknown avg `3.6077` n `765`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.0786` n `228`; crypto_major avg `0.0135` n `8`; equity avg `0.1069` n `88`; fx avg `-0.013` n `6`; index avg `0.0419` n `23`; metal avg `-0.0182` n `20`; unknown avg `5.3869` n `765`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.0638` n `228`; crypto_major avg `-0.359` n `8`; equity avg `0.7885` n `88`; fx avg `-0.0545` n `6`; index avg `0.2392` n `23`; metal avg `0.1282` n `20`; unknown avg `9.7659` n `763`
- 24h: commodity avg `-0.1855` n `12`; crypto_alt avg `0.4229` n `228`; crypto_major avg `1.4661` n `8`; equity avg `2.6009` n `88`; fx avg `0.099` n `6`; index avg `0.4144` n `23`; metal avg `-0.5158` n `20`; unknown avg `12.2632` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
