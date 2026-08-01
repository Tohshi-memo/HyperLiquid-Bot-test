# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T17:52:24.236323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0917` n `230`; crypto_major avg `-0.0275` n `8`; equity avg `-0.0547` n `102`; fx avg `-0.0001` n `6`; index avg `-0.0191` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0341` n `782`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.5628` n `230`; crypto_major avg `-0.585` n `8`; equity avg `-0.074` n `102`; fx avg `-0.0117` n `6`; index avg `-0.0203` n `25`; metal avg `-0.02` n `20`; unknown avg `0.0109` n `782`
- 4h: commodity avg `0.0751` n `12`; crypto_alt avg `-0.5845` n `230`; crypto_major avg `-0.604` n `8`; equity avg `-0.1816` n `102`; fx avg `-0.0155` n `6`; index avg `-0.021` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.1133` n `782`
- 24h: commodity avg `0.6427` n `12`; crypto_alt avg `-0.8096` n `230`; crypto_major avg `-1.3804` n `8`; equity avg `-1.3218` n `102`; fx avg `-0.0706` n `6`; index avg `-0.1591` n `25`; metal avg `-0.082` n `20`; unknown avg `4.2303` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
