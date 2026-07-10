# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T10:52:28.628580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1086` n `12`; crypto_alt avg `-0.0407` n `229`; crypto_major avg `-0.0199` n `8`; equity avg `-0.0105` n `91`; fx avg `0.0052` n `6`; index avg `0.0001` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.0031` n `766`
- 1h: commodity avg `0.0973` n `12`; crypto_alt avg `0.1936` n `229`; crypto_major avg `0.0577` n `8`; equity avg `0.255` n `91`; fx avg `0.0076` n `6`; index avg `0.0387` n `25`; metal avg `0.0235` n `20`; unknown avg `0.158` n `766`
- 4h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.6973` n `229`; crypto_major avg `0.7396` n `8`; equity avg `0.1571` n `91`; fx avg `0.0252` n `6`; index avg `0.0589` n `25`; metal avg `-0.1233` n `20`; unknown avg `0.1445` n `765`
- 24h: commodity avg `-1.0726` n `12`; crypto_alt avg `1.5579` n `229`; crypto_major avg `2.0683` n `8`; equity avg `0.8815` n `91`; fx avg `-0.1167` n `6`; index avg `0.3358` n `25`; metal avg `0.2976` n `20`; unknown avg `0.0942` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
