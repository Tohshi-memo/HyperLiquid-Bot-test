# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T12:52:30.893556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.0484` n `231`; crypto_major avg `0.0576` n `8`; equity avg `0.0596` n `127`; fx avg `-0.0073` n `6`; index avg `0.0219` n `26`; metal avg `-0.0109` n `20`; unknown avg `-0.0721` n `792`
- 1h: commodity avg `-0.1391` n `12`; crypto_alt avg `-0.3222` n `231`; crypto_major avg `-0.2724` n `8`; equity avg `0.1132` n `127`; fx avg `-0.0322` n `6`; index avg `0.0359` n `26`; metal avg `0.0324` n `20`; unknown avg `-0.1056` n `792`
- 4h: commodity avg `-0.2395` n `12`; crypto_alt avg `0.1558` n `231`; crypto_major avg `-0.4001` n `8`; equity avg `0.0045` n `127`; fx avg `0.0261` n `6`; index avg `0.0233` n `26`; metal avg `0.179` n `20`; unknown avg `0.0984` n `792`
- 24h: commodity avg `-0.2248` n `12`; crypto_alt avg `-0.4845` n `231`; crypto_major avg `-0.0396` n `8`; equity avg `-0.6771` n `127`; fx avg `-0.0609` n `6`; index avg `0.0362` n `26`; metal avg `0.848` n `20`; unknown avg `0.5045` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
