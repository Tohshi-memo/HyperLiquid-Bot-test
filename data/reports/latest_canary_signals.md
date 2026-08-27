# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T23:22:28.826033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.083` n `231`; crypto_major avg `0.149` n `8`; equity avg `-0.0511` n `127`; fx avg `-0.0008` n `6`; index avg `0.0056` n `26`; metal avg `-0.0308` n `20`; unknown avg `0.0008` n `792`
- 1h: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0527` n `231`; crypto_major avg `0.0816` n `8`; equity avg `-0.1416` n `127`; fx avg `0.0012` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0385` n `20`; unknown avg `0.001` n `792`
- 4h: commodity avg `-0.0605` n `12`; crypto_alt avg `0.2662` n `231`; crypto_major avg `0.1233` n `8`; equity avg `-0.241` n `127`; fx avg `0.0024` n `6`; index avg `0.028` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.0639` n `792`
- 24h: commodity avg `0.3804` n `12`; crypto_alt avg `1.4865` n `231`; crypto_major avg `2.7919` n `8`; equity avg `-0.4041` n `127`; fx avg `-0.0294` n `6`; index avg `-0.1138` n `26`; metal avg `0.0383` n `20`; unknown avg `0.928` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
