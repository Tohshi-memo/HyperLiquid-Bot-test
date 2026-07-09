# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T11:12:33.267252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1494` n `12`; crypto_alt avg `0.1156` n `229`; crypto_major avg `0.0536` n `8`; equity avg `0.0007` n `91`; fx avg `-0.0016` n `6`; index avg `0.0323` n `25`; metal avg `0.0862` n `20`; unknown avg `0.0164` n `764`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `-0.2229` n `229`; crypto_major avg `-0.4399` n `8`; equity avg `-0.2861` n `91`; fx avg `-0.0073` n `6`; index avg `-0.0253` n `25`; metal avg `-0.0764` n `20`; unknown avg `-0.0069` n `764`
- 4h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.3389` n `229`; crypto_major avg `-0.5746` n `8`; equity avg `-0.1015` n `91`; fx avg `-0.0007` n `6`; index avg `-0.0259` n `25`; metal avg `0.0349` n `20`; unknown avg `-0.1559` n `764`
- 24h: commodity avg `-0.3202` n `12`; crypto_alt avg `1.5778` n `229`; crypto_major avg `0.5056` n `8`; equity avg `3.0661` n `91`; fx avg `0.1372` n `6`; index avg `0.4721` n `25`; metal avg `0.6536` n `20`; unknown avg `0.7594` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
