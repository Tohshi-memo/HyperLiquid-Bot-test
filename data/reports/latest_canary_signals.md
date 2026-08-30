# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T16:07:22.213481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.2127` n `231`; crypto_major avg `0.143` n `8`; equity avg `0.0096` n `128`; fx avg `-0.0023` n `6`; index avg `-0.0059` n `26`; metal avg `0.0098` n `20`; unknown avg `-0.0491` n `793`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `-0.0506` n `231`; crypto_major avg `0.0207` n `8`; equity avg `0.0006` n `128`; fx avg `0.0022` n `6`; index avg `-0.0045` n `26`; metal avg `0.0223` n `20`; unknown avg `0.528` n `793`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `0.0636` n `231`; crypto_major avg `0.4241` n `8`; equity avg `-0.0068` n `128`; fx avg `-0.001` n `6`; index avg `0.0161` n `26`; metal avg `0.097` n `20`; unknown avg `0.23` n `793`
- 24h: commodity avg `0.0131` n `12`; crypto_alt avg `0.9778` n `231`; crypto_major avg `0.7788` n `8`; equity avg `0.3068` n `128`; fx avg `0.0149` n `6`; index avg `0.0714` n `26`; metal avg `0.1172` n `20`; unknown avg `-0.0727` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
