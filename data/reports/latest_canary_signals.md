# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T14:37:32.524598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.0335` n `230`; crypto_major avg `0.1155` n `8`; equity avg `0.0188` n `98`; fx avg `-0.0025` n `6`; index avg `-0.0243` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0912` n `773`
- 1h: commodity avg `0.0943` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `0.1008` n `8`; equity avg `0.4142` n `98`; fx avg `-0.0329` n `6`; index avg `0.0879` n `25`; metal avg `0.1044` n `20`; unknown avg `0.1156` n `773`
- 4h: commodity avg `0.1036` n `12`; crypto_alt avg `0.1327` n `230`; crypto_major avg `0.0144` n `8`; equity avg `0.6625` n `98`; fx avg `-0.0155` n `6`; index avg `0.0889` n `25`; metal avg `0.1652` n `20`; unknown avg `11.3539` n `773`
- 24h: commodity avg `0.3972` n `12`; crypto_alt avg `-0.2909` n `230`; crypto_major avg `-1.2275` n `8`; equity avg `0.4111` n `98`; fx avg `-0.0285` n `6`; index avg `-0.003` n `25`; metal avg `0.5453` n `20`; unknown avg `0.988` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1055`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0697`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0692`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
