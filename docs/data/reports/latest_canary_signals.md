# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T11:37:25.092947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0524` n `12`; crypto_alt avg `0.0679` n `230`; crypto_major avg `0.0204` n `8`; equity avg `0.1859` n `102`; fx avg `0.0057` n `6`; index avg `0.0368` n `25`; metal avg `0.0048` n `20`; unknown avg `0.0065` n `779`
- 1h: commodity avg `-0.1526` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `-0.0926` n `8`; equity avg `0.5863` n `102`; fx avg `-0.0081` n `6`; index avg `0.0891` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.0122` n `779`
- 4h: commodity avg `-0.4847` n `12`; crypto_alt avg `0.1335` n `230`; crypto_major avg `0.5149` n `8`; equity avg `1.9015` n `102`; fx avg `-0.0369` n `6`; index avg `0.3586` n `25`; metal avg `0.4406` n `20`; unknown avg `0.0741` n `771`
- 24h: commodity avg `0.2881` n `12`; crypto_alt avg `-0.0797` n `230`; crypto_major avg `0.0965` n `8`; equity avg `-1.9172` n `102`; fx avg `-0.0797` n `6`; index avg `-0.2964` n `25`; metal avg `0.4512` n `20`; unknown avg `-0.0956` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
