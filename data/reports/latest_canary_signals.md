# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T07:52:32.461433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0281` n `230`; crypto_major avg `-0.0083` n `8`; equity avg `0.0861` n `102`; fx avg `-0.0041` n `6`; index avg `0.0062` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.0139` n `782`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.0987` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `0.0698` n `102`; fx avg `-0.0325` n `6`; index avg `0.0165` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.025` n `782`
- 4h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.3283` n `230`; crypto_major avg `0.0725` n `8`; equity avg `0.1245` n `102`; fx avg `-0.0607` n `6`; index avg `0.034` n `25`; metal avg `0.0379` n `20`; unknown avg `0.3746` n `766`
- 24h: commodity avg `-1.1379` n `12`; crypto_alt avg `0.4935` n `230`; crypto_major avg `0.4837` n `8`; equity avg `0.8597` n `102`; fx avg `-0.1831` n `6`; index avg `0.2413` n `25`; metal avg `0.2448` n `20`; unknown avg `0.3375` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
