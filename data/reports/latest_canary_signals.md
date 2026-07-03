# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T11:21:11.275345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0581` n `12`; crypto_alt avg `0.01` n `229`; crypto_major avg `0.0406` n `8`; equity avg `0.0341` n `88`; fx avg `0.0004` n `6`; index avg `0.0082` n `25`; metal avg `0.0422` n `20`; unknown avg `0.3644` n `765`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `0.5806` n `229`; crypto_major avg `0.6852` n `8`; equity avg `0.1415` n `88`; fx avg `0.0082` n `6`; index avg `0.0159` n `25`; metal avg `-0.038` n `20`; unknown avg `1.0521` n `765`
- 4h: commodity avg `-0.1042` n `12`; crypto_alt avg `1.0956` n `229`; crypto_major avg `1.0424` n `8`; equity avg `0.3387` n `88`; fx avg `0.0651` n `6`; index avg `0.0242` n `25`; metal avg `0.0508` n `20`; unknown avg `1.3055` n `755`
- 24h: commodity avg `0.4882` n `12`; crypto_alt avg `2.0217` n `229`; crypto_major avg `2.4457` n `8`; equity avg `0.2552` n `88`; fx avg `-0.0707` n `6`; index avg `0.2427` n `25`; metal avg `1.2046` n `20`; unknown avg `6.031` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
