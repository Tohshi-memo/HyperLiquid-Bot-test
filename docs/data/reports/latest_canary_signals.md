# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:07:22.273380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `0.0781` n `230`; crypto_major avg `0.0096` n `8`; equity avg `0.0014` n `114`; fx avg `-0.0058` n `6`; index avg `-0.0023` n `25`; metal avg `0.0052` n `20`; unknown avg `0.007` n `792`
- 1h: commodity avg `0.0893` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `-0.0505` n `114`; fx avg `0.0247` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.056` n `792`
- 4h: commodity avg `0.2156` n `12`; crypto_alt avg `-0.2437` n `230`; crypto_major avg `-0.1249` n `8`; equity avg `0.1105` n `114`; fx avg `0.0019` n `6`; index avg `-0.0102` n `25`; metal avg `-0.1248` n `20`; unknown avg `0.201` n `792`
- 24h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.271` n `230`; crypto_major avg `0.5885` n `8`; equity avg `1.1615` n `114`; fx avg `-0.012` n `6`; index avg `0.1276` n `25`; metal avg `0.1395` n `20`; unknown avg `0.0672` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
