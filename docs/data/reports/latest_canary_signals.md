# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T03:07:33.915276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0376` n `229`; crypto_major avg `-0.0191` n `8`; equity avg `-0.0285` n `88`; fx avg `0.0294` n `6`; index avg `-0.0124` n `25`; metal avg `-0.039` n `20`; unknown avg `0.0515` n `765`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `-0.0896` n `229`; crypto_major avg `-0.3041` n `8`; equity avg `-0.1351` n `88`; fx avg `0.0463` n `6`; index avg `-0.0491` n `25`; metal avg `0.0096` n `20`; unknown avg `0.2137` n `761`
- 4h: commodity avg `0.1379` n `12`; crypto_alt avg `0.7139` n `229`; crypto_major avg `0.564` n `8`; equity avg `1.1307` n `88`; fx avg `0.0849` n `6`; index avg `0.2346` n `25`; metal avg `0.6498` n `20`; unknown avg `0.5161` n `761`
- 24h: commodity avg `0.3439` n `12`; crypto_alt avg `2.0392` n `228`; crypto_major avg `2.7421` n `8`; equity avg `-1.2778` n `88`; fx avg `-0.0581` n `6`; index avg `-0.2637` n `25`; metal avg `1.2337` n `20`; unknown avg `6.2864` n `735`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
