# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T00:07:26.654824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.1012` n `230`; crypto_major avg `0.0531` n `8`; equity avg `0.112` n `108`; fx avg `0.0152` n `6`; index avg `0.04` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.0527` n `782`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.1463` n `230`; crypto_major avg `0.1895` n `8`; equity avg `-0.0652` n `108`; fx avg `0.0184` n `6`; index avg `-0.0071` n `25`; metal avg `0.108` n `20`; unknown avg `0.4283` n `782`
- 4h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.0895` n `230`; crypto_major avg `-0.3419` n `8`; equity avg `0.0138` n `108`; fx avg `0.0086` n `6`; index avg `0.0206` n `25`; metal avg `0.1357` n `20`; unknown avg `0.3108` n `782`
- 24h: commodity avg `-0.0089` n `12`; crypto_alt avg `0.8913` n `230`; crypto_major avg `0.8407` n `8`; equity avg `-1.1024` n `108`; fx avg `0.0009` n `6`; index avg `-0.1712` n `25`; metal avg `0.9246` n `20`; unknown avg `1.2754` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
