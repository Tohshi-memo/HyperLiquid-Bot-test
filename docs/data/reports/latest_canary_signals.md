# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T15:02:51.347884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0665` n `12`; crypto_alt avg `0.0381` n `232`; crypto_major avg `0.0252` n `8`; equity avg `-0.0251` n `128`; fx avg `0.0058` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.0411` n `792`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.6719` n `232`; crypto_major avg `0.7254` n `8`; equity avg `-0.0258` n `128`; fx avg `0.0378` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.4817` n `790`
- 4h: commodity avg `-0.1611` n `12`; crypto_alt avg `-0.077` n `232`; crypto_major avg `-0.1061` n `8`; equity avg `-0.1538` n `128`; fx avg `0.0602` n `6`; index avg `-0.0814` n `26`; metal avg `-0.3005` n `20`; unknown avg `0.1413` n `790`
- 24h: commodity avg `0.4692` n `12`; crypto_alt avg `-0.952` n `231`; crypto_major avg `-1.5061` n `8`; equity avg `-0.6136` n `128`; fx avg `-0.0746` n `6`; index avg `-0.1846` n `26`; metal avg `-0.4991` n `20`; unknown avg `0.8271` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
