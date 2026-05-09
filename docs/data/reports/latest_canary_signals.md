# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T10:37:14.782595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `0.0669` n `228`; crypto_major avg `0.0554` n `8`; equity avg `0.0451` n `65`; fx avg `0.0` n `5`; index avg `0.0024` n `23`; metal avg `0.0055` n `18`; unknown avg `0.3422` n `376`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.1234` n `228`; crypto_major avg `-0.2147` n `8`; equity avg `0.0693` n `65`; fx avg `0.0042` n `5`; index avg `-0.0045` n `23`; metal avg `-0.0357` n `18`; unknown avg `0.6243` n `376`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.8358` n `228`; crypto_major avg `-0.3091` n `8`; equity avg `0.0949` n `65`; fx avg `0.0051` n `5`; index avg `0.0276` n `23`; metal avg `-0.0408` n `18`; unknown avg `0.1732` n `376`
- 24h: commodity avg `-0.0532` n `12`; crypto_alt avg `2.9181` n `228`; crypto_major avg `1.8967` n `8`; equity avg `2.7934` n `65`; fx avg `-0.0357` n `5`; index avg `1.2206` n `23`; metal avg `-0.3247` n `18`; unknown avg `0.738` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
