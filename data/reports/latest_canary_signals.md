# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T10:11:35.616188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0704` n `12`; crypto_alt avg `0.1561` n `229`; crypto_major avg `0.1941` n `8`; equity avg `0.0125` n `91`; fx avg `-0.0067` n `6`; index avg `-0.0027` n `25`; metal avg `-0.036` n `20`; unknown avg `0.0638` n `764`
- 1h: commodity avg `0.1044` n `12`; crypto_alt avg `0.0708` n `229`; crypto_major avg `0.1055` n `8`; equity avg `0.0438` n `91`; fx avg `0.0003` n `6`; index avg `-0.0114` n `25`; metal avg `-0.03` n `20`; unknown avg `0.0334` n `764`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.2083` n `229`; crypto_major avg `0.1214` n `8`; equity avg `0.5316` n `91`; fx avg `0.0789` n `6`; index avg `0.0475` n `25`; metal avg `0.3272` n `20`; unknown avg `0.0769` n `764`
- 24h: commodity avg `-0.5747` n `12`; crypto_alt avg `2.1772` n `229`; crypto_major avg `1.2759` n `8`; equity avg `3.9046` n `91`; fx avg `0.1541` n `6`; index avg `0.603` n `25`; metal avg `0.7112` n `20`; unknown avg `0.8975` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0981`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0671`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0656`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0578`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0558`, n `670`, weak_sample_signal
