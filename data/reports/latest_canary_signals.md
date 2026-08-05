# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T19:22:35.830410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0132` n `230`; crypto_major avg `0.0052` n `8`; equity avg `-0.0041` n `108`; fx avg `-0.0019` n `6`; index avg `-0.0087` n `25`; metal avg `-0.04` n `20`; unknown avg `-0.0653` n `782`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.0339` n `230`; crypto_major avg `-0.0702` n `8`; equity avg `0.035` n `108`; fx avg `-0.0145` n `6`; index avg `0.0079` n `25`; metal avg `-0.0561` n `20`; unknown avg `-0.07` n `782`
- 4h: commodity avg `0.038` n `12`; crypto_alt avg `0.2771` n `230`; crypto_major avg `0.6021` n `8`; equity avg `-0.0619` n `108`; fx avg `-0.0091` n `6`; index avg `-0.0378` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0671` n `782`
- 24h: commodity avg `-0.0636` n `12`; crypto_alt avg `0.5831` n `230`; crypto_major avg `0.9445` n `8`; equity avg `-0.3309` n `108`; fx avg `-0.0613` n `6`; index avg `-0.0888` n `25`; metal avg `0.7857` n `20`; unknown avg `0.7819` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
