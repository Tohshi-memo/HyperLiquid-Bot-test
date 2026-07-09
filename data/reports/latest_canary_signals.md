# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T07:41:21.916667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1508` n `12`; crypto_alt avg `-0.0024` n `229`; crypto_major avg `-0.0436` n `8`; equity avg `0.0456` n `91`; fx avg `0.0041` n `6`; index avg `0.0042` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0953` n `764`
- 1h: commodity avg `-0.1432` n `12`; crypto_alt avg `-0.2231` n `229`; crypto_major avg `-0.236` n `8`; equity avg `0.1349` n `91`; fx avg `0.0098` n `6`; index avg `0.0255` n `25`; metal avg `0.0999` n `20`; unknown avg `0.0129` n `764`
- 4h: commodity avg `-0.3067` n `12`; crypto_alt avg `0.9285` n `229`; crypto_major avg `0.8119` n `8`; equity avg `0.7496` n `91`; fx avg `0.0784` n `6`; index avg `0.1165` n `25`; metal avg `0.6199` n `20`; unknown avg `0.0865` n `748`
- 24h: commodity avg `0.0079` n `12`; crypto_alt avg `0.5763` n `229`; crypto_major avg `0.1114` n `8`; equity avg `1.6628` n `91`; fx avg `0.1663` n `6`; index avg `0.1896` n `25`; metal avg `-0.3704` n `20`; unknown avg `0.2842` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1019`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0637`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0562`, n `669`, weak_sample_signal
