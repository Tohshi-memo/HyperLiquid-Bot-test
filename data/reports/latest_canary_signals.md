# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T04:07:27.172743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.3402` n `234`; crypto_major avg `-0.1946` n `8`; equity avg `-0.1142` n `141`; fx avg `-0.001` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0627` n `20`; unknown avg `-0.0815` n `955`
- 1h: commodity avg `0.0284` n `12`; crypto_alt avg `0.3513` n `234`; crypto_major avg `0.2348` n `8`; equity avg `-0.0746` n `141`; fx avg `-0.02` n `6`; index avg `-0.0263` n `26`; metal avg `-0.0908` n `20`; unknown avg `-0.0445` n `955`
- 4h: commodity avg `0.1197` n `12`; crypto_alt avg `-2.0035` n `234`; crypto_major avg `-0.86` n `8`; equity avg `-0.6514` n `141`; fx avg `-0.027` n `6`; index avg `-0.1325` n `26`; metal avg `-0.1032` n `20`; unknown avg `0.8307` n `955`
- 24h: commodity avg `0.0848` n `12`; crypto_alt avg `-2.5829` n `234`; crypto_major avg `-1.0302` n `8`; equity avg `-2.1436` n `141`; fx avg `-0.0477` n `6`; index avg `-0.2249` n `26`; metal avg `-0.5338` n `20`; unknown avg `9.806` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
