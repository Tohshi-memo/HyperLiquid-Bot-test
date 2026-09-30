# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T12:07:28.138558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0848` n `12`; crypto_alt avg `-0.0714` n `234`; crypto_major avg `-0.1048` n `8`; equity avg `-0.0307` n `142`; fx avg `-0.0087` n `6`; index avg `0.0077` n `26`; metal avg `0.0375` n `20`; unknown avg `0.4404` n `955`
- 1h: commodity avg `-0.0659` n `12`; crypto_alt avg `0.3653` n `234`; crypto_major avg `0.1633` n `8`; equity avg `0.0527` n `142`; fx avg `-0.0073` n `6`; index avg `0.0089` n `26`; metal avg `0.0094` n `20`; unknown avg `0.497` n `955`
- 4h: commodity avg `0.2687` n `12`; crypto_alt avg `1.0565` n `234`; crypto_major avg `1.0066` n `8`; equity avg `-0.3433` n `142`; fx avg `0.0765` n `6`; index avg `-0.1124` n `26`; metal avg `-0.1625` n `20`; unknown avg `1.7897` n `955`
- 24h: commodity avg `-0.1466` n `12`; crypto_alt avg `-0.5289` n `234`; crypto_major avg `-0.6332` n `8`; equity avg `-0.3588` n `142`; fx avg `0.0536` n `6`; index avg `-0.0761` n `26`; metal avg `-0.0052` n `20`; unknown avg `2683.1358` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
