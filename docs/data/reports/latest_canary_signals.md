# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T09:52:26.010376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.1098` n `230`; crypto_major avg `0.1178` n `8`; equity avg `-0.1169` n `102`; fx avg `-0.003` n `6`; index avg `-0.0284` n `25`; metal avg `0.0164` n `20`; unknown avg `0.0371` n `784`
- 1h: commodity avg `-0.1703` n `12`; crypto_alt avg `0.3027` n `230`; crypto_major avg `0.3899` n `8`; equity avg `-0.3287` n `102`; fx avg `0.0036` n `6`; index avg `-0.0563` n `25`; metal avg `-0.0536` n `20`; unknown avg `0.1095` n `784`
- 4h: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0914` n `230`; crypto_major avg `-0.1327` n `8`; equity avg `-0.9422` n `102`; fx avg `0.0429` n `6`; index avg `-0.1063` n `25`; metal avg `-0.057` n `20`; unknown avg `-0.0303` n `768`
- 24h: commodity avg `-0.1267` n `12`; crypto_alt avg `-0.8818` n `230`; crypto_major avg `-0.3901` n `8`; equity avg `-0.2775` n `102`; fx avg `-0.1593` n `6`; index avg `-0.1157` n `25`; metal avg `-0.1376` n `20`; unknown avg `1.0258` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
