# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T07:22:39.724424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.1068` n `230`; crypto_major avg `0.0664` n `8`; equity avg `0.0368` n `102`; fx avg `-0.0087` n `6`; index avg `0.0114` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0108` n `782`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `0.0721` n `8`; equity avg `-0.0199` n `102`; fx avg `-0.0243` n `6`; index avg `0.0034` n `25`; metal avg `0.0119` n `20`; unknown avg `0.0073` n `782`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `0.2279` n `230`; crypto_major avg `0.0582` n `8`; equity avg `0.0691` n `102`; fx avg `-0.0722` n `6`; index avg `0.0723` n `25`; metal avg `0.0559` n `20`; unknown avg `0.4011` n `766`
- 24h: commodity avg `-1.1181` n `12`; crypto_alt avg `0.3765` n `230`; crypto_major avg `0.493` n `8`; equity avg `0.8699` n `102`; fx avg `-0.1397` n `6`; index avg `0.2754` n `25`; metal avg `0.2566` n `20`; unknown avg `0.3642` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
