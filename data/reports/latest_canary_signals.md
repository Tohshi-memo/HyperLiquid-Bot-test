# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T08:52:24.785706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1041` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `-0.0363` n `8`; equity avg `-0.0063` n `98`; fx avg `-0.0125` n `6`; index avg `-0.0147` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0291` n `771`
- 1h: commodity avg `0.054` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.1093` n `8`; equity avg `0.4164` n `98`; fx avg `0.0125` n `6`; index avg `0.0306` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0317` n `771`
- 4h: commodity avg `0.1115` n `12`; crypto_alt avg `0.3919` n `230`; crypto_major avg `0.6567` n `8`; equity avg `0.8585` n `98`; fx avg `0.0438` n `6`; index avg `0.0583` n `25`; metal avg `0.3338` n `20`; unknown avg `0.0646` n `755`
- 24h: commodity avg `0.2541` n `12`; crypto_alt avg `2.7201` n `230`; crypto_major avg `2.9701` n `8`; equity avg `2.0749` n `98`; fx avg `-0.0922` n `6`; index avg `0.3126` n `25`; metal avg `0.625` n `20`; unknown avg `0.2054` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
