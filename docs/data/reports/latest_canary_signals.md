# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T15:52:25.898130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.0683` n `230`; crypto_major avg `0.1332` n `8`; equity avg `0.0892` n `114`; fx avg `0.0125` n `6`; index avg `-0.0067` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.096` n `792`
- 1h: commodity avg `0.1252` n `12`; crypto_alt avg `0.1553` n `230`; crypto_major avg `0.2299` n `8`; equity avg `0.2564` n `114`; fx avg `0.0178` n `6`; index avg `-0.0026` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0982` n `792`
- 4h: commodity avg `0.1499` n `12`; crypto_alt avg `0.0577` n `230`; crypto_major avg `0.3558` n `8`; equity avg `0.586` n `114`; fx avg `0.0314` n `6`; index avg `0.0598` n `25`; metal avg `0.1473` n `20`; unknown avg `-0.0686` n `792`
- 24h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.0384` n `230`; crypto_major avg `1.0489` n `8`; equity avg `1.7279` n `114`; fx avg `0.0176` n `6`; index avg `0.2155` n `25`; metal avg `0.3147` n `20`; unknown avg `0.0433` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
