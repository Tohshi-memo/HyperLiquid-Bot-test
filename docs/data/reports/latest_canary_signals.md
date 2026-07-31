# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T03:52:25.198353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.006` n `230`; crypto_major avg `0.0822` n `8`; equity avg `-0.025` n `102`; fx avg `-0.0141` n `6`; index avg `-0.0266` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.1204` n `779`
- 1h: commodity avg `0.0407` n `12`; crypto_alt avg `0.0666` n `230`; crypto_major avg `0.1453` n `8`; equity avg `0.0653` n `102`; fx avg `0.0089` n `6`; index avg `-0.0118` n `25`; metal avg `0.0299` n `20`; unknown avg `5.2051` n `779`
- 4h: commodity avg `-0.2148` n `12`; crypto_alt avg `-0.2203` n `230`; crypto_major avg `-0.5621` n `8`; equity avg `0.1892` n `102`; fx avg `0.1823` n `6`; index avg `0.1718` n `25`; metal avg `-0.266` n `20`; unknown avg `0.0109` n `779`
- 24h: commodity avg `-0.154` n `12`; crypto_alt avg `-0.1607` n `230`; crypto_major avg `0.6831` n `8`; equity avg `7.7741` n `102`; fx avg `-0.1503` n `6`; index avg `0.9928` n `25`; metal avg `0.4707` n `20`; unknown avg `0.0498` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
