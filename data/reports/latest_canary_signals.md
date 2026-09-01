# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T01:52:26.760810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0598` n `12`; crypto_alt avg `0.1501` n `232`; crypto_major avg `0.0379` n `8`; equity avg `-0.0057` n `130`; fx avg `-0.0037` n `6`; index avg `0.0007` n `26`; metal avg `-0.054` n `20`; unknown avg `0.111` n `792`
- 1h: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.0016` n `232`; crypto_major avg `-0.254` n `8`; equity avg `0.0459` n `130`; fx avg `0.0057` n `6`; index avg `0.0276` n `26`; metal avg `-0.1202` n `20`; unknown avg `0.1025` n `790`
- 4h: commodity avg `0.0391` n `12`; crypto_alt avg `0.3021` n `232`; crypto_major avg `-0.5614` n `8`; equity avg `0.0162` n `130`; fx avg `0.0282` n `6`; index avg `0.0492` n `26`; metal avg `0.0084` n `20`; unknown avg `1.3229` n `790`
- 24h: commodity avg `0.3621` n `12`; crypto_alt avg `2.3303` n `231`; crypto_major avg `1.8334` n `8`; equity avg `1.4928` n `130`; fx avg `-0.018` n `6`; index avg `0.2323` n `26`; metal avg `-0.0398` n `20`; unknown avg `0.3155` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
