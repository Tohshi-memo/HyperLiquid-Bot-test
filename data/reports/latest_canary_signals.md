# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T01:52:34.193498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `-0.0003` n `230`; crypto_major avg `-0.0171` n `8`; equity avg `-0.0525` n `102`; fx avg `-0.0091` n `6`; index avg `-0.0093` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0173` n `782`
- 1h: commodity avg `-0.2186` n `12`; crypto_alt avg `0.4245` n `230`; crypto_major avg `0.452` n `8`; equity avg `-0.0521` n `102`; fx avg `-0.0047` n `6`; index avg `0.0119` n `25`; metal avg `0.0365` n `20`; unknown avg `2.144` n `782`
- 4h: commodity avg `-0.3184` n `12`; crypto_alt avg `0.5001` n `230`; crypto_major avg `0.5048` n `8`; equity avg `0.1293` n `102`; fx avg `-0.0287` n `6`; index avg `0.0477` n `25`; metal avg `0.0284` n `20`; unknown avg `0.719` n `782`
- 24h: commodity avg `-0.3896` n `12`; crypto_alt avg `-0.3583` n `230`; crypto_major avg `-0.4494` n `8`; equity avg `0.0903` n `102`; fx avg `-0.0478` n `6`; index avg `-0.0049` n `25`; metal avg `0.0911` n `20`; unknown avg `-0.0103` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
