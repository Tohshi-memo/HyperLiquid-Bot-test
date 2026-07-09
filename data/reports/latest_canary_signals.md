# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T00:07:33.753157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `0.0914` n `229`; crypto_major avg `-0.1349` n `8`; equity avg `0.0896` n `91`; fx avg `0.0085` n `6`; index avg `0.0102` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.131` n `764`
- 1h: commodity avg `-0.0494` n `12`; crypto_alt avg `0.1147` n `229`; crypto_major avg `-0.0034` n `8`; equity avg `0.3137` n `91`; fx avg `-0.0073` n `6`; index avg `0.0399` n `25`; metal avg `0.0512` n `20`; unknown avg `-0.0472` n `764`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.2449` n `229`; crypto_major avg `0.0275` n `8`; equity avg `0.4327` n `91`; fx avg `-0.002` n `6`; index avg `0.0269` n `25`; metal avg `0.0294` n `20`; unknown avg `-0.273` n `764`
- 24h: commodity avg `0.2704` n `12`; crypto_alt avg `-1.2959` n `229`; crypto_major avg `-2.057` n `8`; equity avg `1.8273` n `91`; fx avg `-0.0685` n `6`; index avg `0.0448` n `25`; metal avg `-0.6065` n `20`; unknown avg `-0.0888` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
