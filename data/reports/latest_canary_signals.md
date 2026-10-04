# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T10:52:24.884177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.1129` n `235`; crypto_major avg `0.0681` n `8`; equity avg `0.0099` n `143`; fx avg `0.0023` n `6`; index avg `0.0007` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.0099` n `1079`
- 1h: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.1016` n `235`; crypto_major avg `0.032` n `8`; equity avg `0.0171` n `143`; fx avg `0.0197` n `6`; index avg `0.0013` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.0266` n `1077`
- 4h: commodity avg `-0.0173` n `13`; crypto_alt avg `-0.1961` n `235`; crypto_major avg `0.357` n `8`; equity avg `0.0198` n `143`; fx avg `0.0254` n `6`; index avg `0.0041` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.0672` n `1061`
- 24h: commodity avg `0.1291` n `13`; crypto_alt avg `1.5764` n `235`; crypto_major avg `1.3686` n `8`; equity avg `0.2386` n `143`; fx avg `-0.0057` n `6`; index avg `0.0215` n `26`; metal avg `0.0002` n `20`; unknown avg `0.028` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
