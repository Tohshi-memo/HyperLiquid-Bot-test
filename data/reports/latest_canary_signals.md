# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T05:07:19.081493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `0.0838` n `228`; crypto_major avg `0.0783` n `8`; equity avg `0.0518` n `67`; fx avg `-0.0044` n `6`; index avg `0.0134` n `23`; metal avg `0.0076` n `18`; unknown avg `0.0316` n `386`
- 1h: commodity avg `0.0938` n `12`; crypto_alt avg `-0.1435` n `228`; crypto_major avg `-0.0778` n `8`; equity avg `0.0787` n `67`; fx avg `0.0183` n `6`; index avg `0.028` n `23`; metal avg `0.0296` n `18`; unknown avg `-0.6094` n `386`
- 4h: commodity avg `-0.1541` n `12`; crypto_alt avg `1.0143` n `228`; crypto_major avg `0.3597` n `8`; equity avg `0.4171` n `67`; fx avg `0.0791` n `6`; index avg `0.1559` n `23`; metal avg `0.2147` n `18`; unknown avg `-0.6143` n `386`
- 24h: commodity avg `-0.7415` n `12`; crypto_alt avg `1.5943` n `228`; crypto_major avg `0.3199` n `8`; equity avg `1.2743` n `66`; fx avg `0.1205` n `6`; index avg `0.6498` n `23`; metal avg `0.5643` n `18`; unknown avg `2.3136` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
