# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T19:07:26.997983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `0.0468` n `228`; crypto_major avg `0.0485` n `8`; equity avg `-0.0603` n `88`; fx avg `-0.0013` n `6`; index avg `0.0032` n `23`; metal avg `-0.062` n `20`; unknown avg `-0.2405` n `765`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.3135` n `228`; crypto_major avg `0.5198` n `8`; equity avg `0.0874` n `88`; fx avg `-0.0072` n `6`; index avg `0.0112` n `23`; metal avg `-0.0053` n `20`; unknown avg `-0.2949` n `765`
- 4h: commodity avg `-0.2264` n `12`; crypto_alt avg `0.4879` n `228`; crypto_major avg `0.9351` n `8`; equity avg `0.7049` n `88`; fx avg `-0.0303` n `6`; index avg `0.0801` n `23`; metal avg `-0.0785` n `20`; unknown avg `-0.0853` n `765`
- 24h: commodity avg `0.1081` n `12`; crypto_alt avg `-2.0887` n `228`; crypto_major avg `-1.8075` n `8`; equity avg `1.1981` n `88`; fx avg `0.142` n `6`; index avg `0.3182` n `23`; metal avg `0.282` n `20`; unknown avg `7.5932` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
