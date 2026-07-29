# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T18:37:29.379052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.3077` n `230`; crypto_major avg `-0.1924` n `8`; equity avg `0.0836` n `102`; fx avg `0.0112` n `6`; index avg `0.0655` n `25`; metal avg `-0.046` n `20`; unknown avg `-0.2311` n `778`
- 1h: commodity avg `0.1034` n `12`; crypto_alt avg `0.2733` n `230`; crypto_major avg `0.3736` n `8`; equity avg `0.5379` n `102`; fx avg `0.0122` n `6`; index avg `0.1337` n `25`; metal avg `0.2397` n `20`; unknown avg `-0.2584` n `778`
- 4h: commodity avg `0.0563` n `12`; crypto_alt avg `0.2265` n `230`; crypto_major avg `0.3149` n `8`; equity avg `0.5415` n `102`; fx avg `-0.0198` n `6`; index avg `0.1616` n `25`; metal avg `0.4543` n `20`; unknown avg `-0.2795` n `778`
- 24h: commodity avg `1.2944` n `12`; crypto_alt avg `-1.7069` n `230`; crypto_major avg `0.1884` n `8`; equity avg `-0.9023` n `102`; fx avg `-0.0223` n `6`; index avg `-0.167` n `25`; metal avg `0.2341` n `20`; unknown avg `-0.6665` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
