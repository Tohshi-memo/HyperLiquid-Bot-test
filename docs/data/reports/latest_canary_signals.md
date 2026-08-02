# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T01:07:24.360225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2055` n `12`; crypto_alt avg `0.3034` n `230`; crypto_major avg `0.3157` n `8`; equity avg `0.0295` n `102`; fx avg `-0.0027` n `6`; index avg `0.002` n `25`; metal avg `0.0294` n `20`; unknown avg `12.311` n `782`
- 1h: commodity avg `-0.2095` n `12`; crypto_alt avg `0.3312` n `230`; crypto_major avg `0.2267` n `8`; equity avg `0.1952` n `102`; fx avg `0.0076` n `6`; index avg `0.0128` n `25`; metal avg `0.0343` n `20`; unknown avg `12.3531` n `782`
- 4h: commodity avg `-0.3631` n `12`; crypto_alt avg `0.6223` n `230`; crypto_major avg `0.5266` n `8`; equity avg `0.5613` n `102`; fx avg `-0.0048` n `6`; index avg `0.0852` n `25`; metal avg `0.0525` n `20`; unknown avg `0.9471` n `782`
- 24h: commodity avg `-0.3691` n `12`; crypto_alt avg `-0.5252` n `230`; crypto_major avg `-0.5997` n `8`; equity avg `0.1275` n `102`; fx avg `-0.0442` n `6`; index avg `0.0596` n `25`; metal avg `0.097` n `20`; unknown avg `-0.0305` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
