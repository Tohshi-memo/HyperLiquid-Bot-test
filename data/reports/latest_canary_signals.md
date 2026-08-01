# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T14:02:45.320897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0854` n `12`; crypto_alt avg `0.0642` n `230`; crypto_major avg `0.0423` n `8`; equity avg `0.0089` n `102`; fx avg `0.0095` n `6`; index avg `0.0016` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0259` n `782`
- 1h: commodity avg `-0.092` n `12`; crypto_alt avg `-0.0299` n `230`; crypto_major avg `0.0571` n `8`; equity avg `-0.0169` n `102`; fx avg `0.0213` n `6`; index avg `-0.0142` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0968` n `782`
- 4h: commodity avg `-0.0355` n `12`; crypto_alt avg `0.2762` n `230`; crypto_major avg `0.1674` n `8`; equity avg `-0.0619` n `102`; fx avg `-0.0476` n `6`; index avg `-0.0218` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.1275` n `781`
- 24h: commodity avg `0.4162` n `12`; crypto_alt avg `1.1179` n `230`; crypto_major avg `-0.2766` n `8`; equity avg `-0.1311` n `102`; fx avg `0.074` n `6`; index avg `0.1029` n `25`; metal avg `0.2918` n `20`; unknown avg `4.4575` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
