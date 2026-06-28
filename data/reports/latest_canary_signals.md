# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T23:07:29.051726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.2372` n `228`; crypto_major avg `0.3938` n `8`; equity avg `0.0008` n `88`; fx avg `0.0033` n `6`; index avg `-0.0402` n `23`; metal avg `0.098` n `20`; unknown avg `0.5337` n `762`
- 1h: commodity avg `0.0483` n `12`; crypto_alt avg `-0.7077` n `228`; crypto_major avg `-0.8023` n `8`; equity avg `-0.0727` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0472` n `23`; metal avg `-0.1187` n `20`; unknown avg `0.5543` n `762`
- 4h: commodity avg `-0.4153` n `12`; crypto_alt avg `-0.6508` n `228`; crypto_major avg `-0.5261` n `8`; equity avg `0.2363` n `88`; fx avg `-0.0585` n `6`; index avg `0.0947` n `23`; metal avg `-0.0604` n `20`; unknown avg `0.659` n `762`
- 24h: commodity avg `-0.0901` n `12`; crypto_alt avg `-0.976` n `228`; crypto_major avg `-1.4258` n `8`; equity avg `0.2771` n `88`; fx avg `-0.0982` n `6`; index avg `0.0815` n `23`; metal avg `-0.0718` n `20`; unknown avg `15.3632` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
