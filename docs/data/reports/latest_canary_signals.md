# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:07:23.874268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.0076` n `230`; crypto_major avg `-0.089` n `8`; equity avg `-0.0475` n `114`; fx avg `-0.0036` n `6`; index avg `-0.0094` n `25`; metal avg `0.0138` n `20`; unknown avg `0.0938` n `792`
- 1h: commodity avg `0.0883` n `12`; crypto_alt avg `0.132` n `230`; crypto_major avg `0.1146` n `8`; equity avg `0.0535` n `114`; fx avg `0.0181` n `6`; index avg `-0.0296` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.0313` n `792`
- 4h: commodity avg `0.1323` n `12`; crypto_alt avg `0.1706` n `230`; crypto_major avg `0.3219` n `8`; equity avg `0.6025` n `114`; fx avg `0.0264` n `6`; index avg `0.0641` n `25`; metal avg `0.1955` n `20`; unknown avg `0.0143` n `792`
- 24h: commodity avg `0.0056` n `12`; crypto_alt avg `-0.0841` n `230`; crypto_major avg `0.9309` n `8`; equity avg `1.6933` n `114`; fx avg `0.0091` n `6`; index avg `0.2027` n `25`; metal avg `0.3292` n `20`; unknown avg `0.0873` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
