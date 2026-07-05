# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T00:07:30.975249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.1308` n `229`; crypto_major avg `-0.172` n `8`; equity avg `-0.0209` n `88`; fx avg `0.001` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.4044` n `765`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `-0.2844` n `229`; crypto_major avg `-0.3719` n `8`; equity avg `-0.0766` n `88`; fx avg `0.0035` n `6`; index avg `-0.0059` n `25`; metal avg `0.0108` n `20`; unknown avg `0.2344` n `765`
- 4h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.8235` n `229`; crypto_major avg `-0.6282` n `8`; equity avg `-0.0279` n `88`; fx avg `0.034` n `6`; index avg `0.0098` n `25`; metal avg `0.0265` n `20`; unknown avg `-0.0223` n `765`
- 24h: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.49` n `229`; crypto_major avg `-0.0739` n `8`; equity avg `0.2599` n `88`; fx avg `0.0018` n `6`; index avg `0.0153` n `25`; metal avg `0.0729` n `20`; unknown avg `-0.7661` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
