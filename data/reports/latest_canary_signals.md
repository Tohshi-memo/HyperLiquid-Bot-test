# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T08:52:29.009511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0184` n `229`; crypto_major avg `0.0505` n `8`; equity avg `-0.0201` n `88`; fx avg `0.0` n `6`; index avg `0.0095` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0133` n `765`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0754` n `229`; crypto_major avg `0.0422` n `8`; equity avg `0.0119` n `88`; fx avg `0.0022` n `6`; index avg `0.0028` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0266` n `765`
- 4h: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0702` n `229`; crypto_major avg `0.1101` n `8`; equity avg `0.0593` n `88`; fx avg `0.0115` n `6`; index avg `0.0425` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.109` n `731`
- 24h: commodity avg `0.096` n `12`; crypto_alt avg `-0.5469` n `229`; crypto_major avg `-0.732` n `8`; equity avg `0.2432` n `88`; fx avg `0.0236` n `6`; index avg `0.0514` n `25`; metal avg `0.0786` n `20`; unknown avg `-1.3505` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
