# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T07:37:28.085249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.067` n `230`; crypto_major avg `-0.1356` n `8`; equity avg `-0.0877` n `114`; fx avg `0.0031` n `6`; index avg `-0.0294` n `25`; metal avg `-0.0378` n `20`; unknown avg `0.0537` n `795`
- 1h: commodity avg `-0.1464` n `12`; crypto_alt avg `-0.0943` n `230`; crypto_major avg `-0.1119` n `8`; equity avg `-0.1377` n `114`; fx avg `-0.0063` n `6`; index avg `-0.0091` n `25`; metal avg `-0.03` n `20`; unknown avg `0.007` n `793`
- 4h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.5509` n `230`; crypto_major avg `0.4437` n `8`; equity avg `0.0215` n `114`; fx avg `0.0112` n `6`; index avg `-0.059` n `25`; metal avg `0.0168` n `20`; unknown avg `0.0665` n `761`
- 24h: commodity avg `0.7187` n `12`; crypto_alt avg `-1.064` n `230`; crypto_major avg `0.059` n `8`; equity avg `-1.7663` n `114`; fx avg `-0.0213` n `6`; index avg `-0.4427` n `25`; metal avg `-0.3037` n `20`; unknown avg `0.0084` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
