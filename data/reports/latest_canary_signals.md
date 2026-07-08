# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T21:37:42.696433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.2284` n `229`; crypto_major avg `0.1571` n `8`; equity avg `0.1152` n `91`; fx avg `0.015` n `6`; index avg `0.003` n `25`; metal avg `-0.0232` n `20`; unknown avg `0.0517` n `764`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0852` n `229`; crypto_major avg `-0.0856` n `8`; equity avg `0.2431` n `91`; fx avg `0.0294` n `6`; index avg `0.0192` n `25`; metal avg `0.0331` n `20`; unknown avg `-0.1399` n `764`
- 4h: commodity avg `0.241` n `12`; crypto_alt avg `-0.5527` n `229`; crypto_major avg `-0.5737` n `8`; equity avg `0.4579` n `91`; fx avg `-0.0087` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.9277` n `764`
- 24h: commodity avg `0.4499` n `12`; crypto_alt avg `-1.9849` n `229`; crypto_major avg `-2.3637` n `8`; equity avg `1.2915` n `91`; fx avg `0.0254` n `6`; index avg `-0.0324` n `25`; metal avg `-0.8597` n `20`; unknown avg `0.0653` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
