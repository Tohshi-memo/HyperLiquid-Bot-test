# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T06:37:27.635658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0572` n `12`; crypto_alt avg `0.1323` n `230`; crypto_major avg `0.0104` n `8`; equity avg `0.0247` n `108`; fx avg `0.0158` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0267` n `782`
- 1h: commodity avg `0.2024` n `12`; crypto_alt avg `0.181` n `230`; crypto_major avg `-0.1282` n `8`; equity avg `-0.164` n `108`; fx avg `0.096` n `6`; index avg `-0.0288` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0241` n `750`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `0.5847` n `230`; crypto_major avg `0.4685` n `8`; equity avg `-0.2405` n `108`; fx avg `0.0501` n `6`; index avg `-0.0567` n `25`; metal avg `-0.2162` n `20`; unknown avg `0.0114` n `750`
- 24h: commodity avg `0.0592` n `12`; crypto_alt avg `0.0584` n `230`; crypto_major avg `-0.2524` n `8`; equity avg `-2.1777` n `108`; fx avg `0.0342` n `6`; index avg `-0.4062` n `25`; metal avg `0.102` n `20`; unknown avg `0.8385` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
