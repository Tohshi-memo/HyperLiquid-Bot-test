# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T23:37:25.902483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.058` n `229`; crypto_major avg `0.1209` n `8`; equity avg `0.0003` n `88`; fx avg `-0.0046` n `6`; index avg `-0.0128` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.1061` n `765`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.02` n `229`; crypto_major avg `0.1242` n `8`; equity avg `0.049` n `88`; fx avg `-0.0118` n `6`; index avg `-0.0097` n `25`; metal avg `0.0344` n `20`; unknown avg `0.9014` n `765`
- 4h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.3009` n `229`; crypto_major avg `0.4104` n `8`; equity avg `-0.0488` n `88`; fx avg `-0.0219` n `6`; index avg `-0.0452` n `25`; metal avg `0.0298` n `20`; unknown avg `0.0376` n `765`
- 24h: commodity avg `0.1333` n `12`; crypto_alt avg `3.0024` n `229`; crypto_major avg `3.2465` n `8`; equity avg `1.8237` n `88`; fx avg `-0.0791` n `6`; index avg `0.4001` n `25`; metal avg `0.5376` n `20`; unknown avg `5.7497` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
