# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T06:37:34.414872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0763` n `12`; crypto_alt avg `0.2205` n `229`; crypto_major avg `0.1477` n `8`; equity avg `0.1649` n `91`; fx avg `0.0358` n `6`; index avg `0.0289` n `25`; metal avg `0.0695` n `20`; unknown avg `-0.0371` n `764`
- 1h: commodity avg `-0.0564` n `12`; crypto_alt avg `0.5602` n `229`; crypto_major avg `0.5818` n `8`; equity avg `0.6558` n `91`; fx avg `0.0844` n `6`; index avg `0.1224` n `25`; metal avg `0.3557` n `20`; unknown avg `0.1689` n `748`
- 4h: commodity avg `-0.2026` n `12`; crypto_alt avg `1.1236` n `229`; crypto_major avg `1.1399` n `8`; equity avg `0.3634` n `91`; fx avg `0.07` n `6`; index avg `0.0667` n `25`; metal avg `0.389` n `20`; unknown avg `0.1012` n `748`
- 24h: commodity avg `0.0289` n `12`; crypto_alt avg `1.1024` n `229`; crypto_major avg `0.6996` n `8`; equity avg `1.6975` n `91`; fx avg `0.195` n `6`; index avg `0.1846` n `25`; metal avg `-0.6309` n `20`; unknown avg `0.4059` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
