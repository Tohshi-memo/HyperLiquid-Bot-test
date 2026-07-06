# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T02:48:18.289938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0445` n `12`; crypto_alt avg `-0.1225` n `229`; crypto_major avg `-0.1386` n `8`; equity avg `-0.1608` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0515` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0875` n `765`
- 1h: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.114` n `229`; crypto_major avg `-0.2275` n `8`; equity avg `-0.4436` n `88`; fx avg `0.0076` n `6`; index avg `-0.112` n `25`; metal avg `-0.2703` n `20`; unknown avg `-0.1902` n `765`
- 4h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.4009` n `229`; crypto_major avg `-0.3492` n `8`; equity avg `-1.5467` n `88`; fx avg `0.0512` n `6`; index avg `-0.2308` n `25`; metal avg `-0.3352` n `20`; unknown avg `-0.5722` n `765`
- 24h: commodity avg `-0.2206` n `12`; crypto_alt avg `0.8562` n `229`; crypto_major avg `1.921` n `8`; equity avg `-1.1092` n `88`; fx avg `0.0703` n `6`; index avg `-0.183` n `25`; metal avg `-0.1378` n `20`; unknown avg `1.2264` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
