# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T22:52:33.648307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.0522` n `228`; crypto_major avg `0.0255` n `8`; equity avg `-0.0171` n `88`; fx avg `-0.0028` n `6`; index avg `-0.0069` n `23`; metal avg `-0.0462` n `20`; unknown avg `-0.0549` n `765`
- 1h: commodity avg `-0.0577` n `12`; crypto_alt avg `-0.0837` n `228`; crypto_major avg `-0.0586` n `8`; equity avg `-0.0005` n `88`; fx avg `-0.0099` n `6`; index avg `0.0129` n `23`; metal avg `0.0367` n `20`; unknown avg `-0.3097` n `765`
- 4h: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.5506` n `228`; crypto_major avg `-0.4026` n `8`; equity avg `0.2689` n `88`; fx avg `-0.0139` n `6`; index avg `-0.0373` n `23`; metal avg `-0.3095` n `20`; unknown avg `5.0267` n `763`
- 24h: commodity avg `0.1417` n `12`; crypto_alt avg `-2.2608` n `228`; crypto_major avg `-2.3739` n `8`; equity avg `1.1906` n `88`; fx avg `0.0992` n `6`; index avg `0.26` n `23`; metal avg `-0.0076` n `20`; unknown avg `11.6757` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
