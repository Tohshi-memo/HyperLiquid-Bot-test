# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T17:39:55.991145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.1195` n `229`; crypto_major avg `0.2718` n `8`; equity avg `0.0229` n `88`; fx avg `0.0` n `6`; index avg `0.0142` n `25`; metal avg `0.0046` n `20`; unknown avg `0.1877` n `765`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.1306` n `229`; crypto_major avg `0.2043` n `8`; equity avg `0.0044` n `88`; fx avg `0.0022` n `6`; index avg `-0.0256` n `25`; metal avg `0.0032` n `20`; unknown avg `0.202` n `765`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `1.0854` n `229`; crypto_major avg `1.066` n `8`; equity avg `0.0726` n `88`; fx avg `0.0213` n `6`; index avg `-0.0201` n `25`; metal avg `0.0124` n `20`; unknown avg `0.5516` n `765`
- 24h: commodity avg `-0.0197` n `12`; crypto_alt avg `1.4022` n `229`; crypto_major avg `1.8264` n `8`; equity avg `0.211` n `88`; fx avg `-0.0066` n `6`; index avg `-0.0931` n `25`; metal avg `0.0296` n `20`; unknown avg `2.0246` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
