# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T13:37:27.310564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.0137` n `230`; crypto_major avg `0.0544` n `8`; equity avg `0.0061` n `102`; fx avg `0.0047` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.006` n `782`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0724` n `230`; crypto_major avg `0.1084` n `8`; equity avg `-0.0641` n `102`; fx avg `0.0316` n `6`; index avg `-0.0141` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0175` n `782`
- 4h: commodity avg `0.1028` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.0438` n `8`; equity avg `-0.0892` n `102`; fx avg `-0.0506` n `6`; index avg `-0.0112` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0811` n `781`
- 24h: commodity avg `0.4314` n `12`; crypto_alt avg `0.1293` n `230`; crypto_major avg `-1.1981` n `8`; equity avg `-2.5986` n `102`; fx avg `0.0429` n `6`; index avg `-0.3242` n `25`; metal avg `0.1876` n `20`; unknown avg `4.204` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
