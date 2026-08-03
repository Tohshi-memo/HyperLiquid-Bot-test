# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T00:07:29.820045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `-0.1029` n `230`; crypto_major avg `-0.1407` n `8`; equity avg `-0.3968` n `102`; fx avg `-0.0434` n `6`; index avg `-0.1092` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0119` n `784`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0171` n `230`; crypto_major avg `-0.0551` n `8`; equity avg `-0.3555` n `102`; fx avg `-0.0338` n `6`; index avg `-0.1144` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0714` n `784`
- 4h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.1951` n `230`; crypto_major avg `-0.1122` n `8`; equity avg `-0.121` n `102`; fx avg `-0.0189` n `6`; index avg `-0.0682` n `25`; metal avg `-0.1155` n `20`; unknown avg `1.8113` n `783`
- 24h: commodity avg `-1.116` n `12`; crypto_alt avg `0.8726` n `230`; crypto_major avg `1.3404` n `8`; equity avg `1.1848` n `102`; fx avg `-0.0475` n `6`; index avg `0.2087` n `25`; metal avg `0.1997` n `20`; unknown avg `1.5585` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
