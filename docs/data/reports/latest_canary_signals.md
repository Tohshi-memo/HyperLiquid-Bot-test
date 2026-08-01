# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T00:52:31.899430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0383` n `12`; crypto_alt avg `0.1277` n `230`; crypto_major avg `0.0831` n `8`; equity avg `0.0538` n `102`; fx avg `0.0007` n `6`; index avg `-0.0102` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0772` n `781`
- 1h: commodity avg `-0.0771` n `12`; crypto_alt avg `0.452` n `230`; crypto_major avg `0.1453` n `8`; equity avg `0.0725` n `102`; fx avg `0.0114` n `6`; index avg `0.0048` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0964` n `781`
- 4h: commodity avg `0.528` n `12`; crypto_alt avg `0.4769` n `230`; crypto_major avg `0.0539` n `8`; equity avg `-0.3024` n `102`; fx avg `-0.0082` n `6`; index avg `-0.0727` n `25`; metal avg `-0.0661` n `20`; unknown avg `2.7416` n `781`
- 24h: commodity avg `0.8753` n `12`; crypto_alt avg `-0.2539` n `230`; crypto_major avg `-1.9591` n `8`; equity avg `-2.6988` n `102`; fx avg `-0.1055` n `6`; index avg `-0.3637` n `25`; metal avg `-0.3475` n `20`; unknown avg `2.6769` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
