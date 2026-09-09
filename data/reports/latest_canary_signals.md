# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T14:37:32.323055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.2792` n `233`; crypto_major avg `0.3591` n `8`; equity avg `0.2544` n `134`; fx avg `-0.0071` n `6`; index avg `0.018` n `26`; metal avg `0.1429` n `20`; unknown avg `0.9097` n `797`
- 1h: commodity avg `0.0608` n `12`; crypto_alt avg `0.0606` n `233`; crypto_major avg `-0.0513` n `8`; equity avg `-0.0179` n `134`; fx avg `-0.0144` n `6`; index avg `0.018` n `26`; metal avg `0.0591` n `20`; unknown avg `11.4472` n `773`
- 4h: commodity avg `0.0407` n `12`; crypto_alt avg `0.1635` n `233`; crypto_major avg `0.083` n `8`; equity avg `0.4089` n `134`; fx avg `0.0093` n `6`; index avg `0.0414` n `26`; metal avg `0.4725` n `20`; unknown avg `17.546` n `766`
- 24h: commodity avg `0.3935` n `12`; crypto_alt avg `0.1989` n `232`; crypto_major avg `1.117` n `8`; equity avg `0.3815` n `134`; fx avg `-0.0994` n `6`; index avg `-0.0719` n `26`; metal avg `0.4584` n `20`; unknown avg `9.2399` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
