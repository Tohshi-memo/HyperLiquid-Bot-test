# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T10:22:34.975147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `0.1764` n `230`; crypto_major avg `0.1797` n `8`; equity avg `0.1628` n `102`; fx avg `0.0267` n `6`; index avg `0.068` n `25`; metal avg `0.0073` n `20`; unknown avg `0.0844` n `780`
- 1h: commodity avg `0.1459` n `12`; crypto_alt avg `0.1839` n `230`; crypto_major avg `0.1043` n `8`; equity avg `-0.1013` n `102`; fx avg `0.0868` n `6`; index avg `-0.0195` n `25`; metal avg `0.0107` n `20`; unknown avg `0.0885` n `780`
- 4h: commodity avg `0.3524` n `12`; crypto_alt avg `-0.3198` n `230`; crypto_major avg `-0.7921` n `8`; equity avg `-0.1883` n `102`; fx avg `0.0315` n `6`; index avg `-0.0768` n `25`; metal avg `-0.228` n `20`; unknown avg `-0.0013` n `779`
- 24h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.4086` n `230`; crypto_major avg `-0.3261` n `8`; equity avg `7.9776` n `102`; fx avg `-0.0913` n `6`; index avg `1.1631` n `25`; metal avg `0.0477` n `20`; unknown avg `0.0263` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
