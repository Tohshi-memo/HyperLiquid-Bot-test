# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T15:37:43.982275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `0.3347` n `232`; crypto_major avg `0.2219` n `8`; equity avg `0.2394` n `131`; fx avg `-0.0093` n `6`; index avg `0.0334` n `26`; metal avg `0.0388` n `20`; unknown avg `0.3606` n `792`
- 1h: commodity avg `0.1436` n `12`; crypto_alt avg `-0.2285` n `232`; crypto_major avg `-0.3476` n `8`; equity avg `0.1743` n `131`; fx avg `-0.0179` n `6`; index avg `0.0085` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.1647` n `790`
- 4h: commodity avg `0.131` n `12`; crypto_alt avg `0.0056` n `232`; crypto_major avg `-0.3377` n `8`; equity avg `-0.3027` n `130`; fx avg `-0.036` n `6`; index avg `0.0216` n `26`; metal avg `-0.0174` n `20`; unknown avg `0.1357` n `790`
- 24h: commodity avg `0.3559` n `12`; crypto_alt avg `1.2722` n `232`; crypto_major avg `-0.2524` n `8`; equity avg `-0.8882` n `130`; fx avg `-0.0016` n `6`; index avg `-0.1146` n `26`; metal avg `-0.4813` n `20`; unknown avg `-0.0947` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0357`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0321`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0315`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0311`, n `668`, weak_sample_signal
