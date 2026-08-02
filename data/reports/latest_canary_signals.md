# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T19:22:23.917923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0706` n `230`; crypto_major avg `-0.0223` n `8`; equity avg `0.0047` n `102`; fx avg `0.0194` n `6`; index avg `-0.0027` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0102` n `782`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `0.0083` n `230`; crypto_major avg `0.0885` n `8`; equity avg `0.0818` n `102`; fx avg `0.03` n `6`; index avg `0.0036` n `25`; metal avg `0.011` n `20`; unknown avg `0.1377` n `782`
- 4h: commodity avg `-0.1021` n `12`; crypto_alt avg `0.1262` n `230`; crypto_major avg `0.6343` n `8`; equity avg `0.3817` n `102`; fx avg `0.0401` n `6`; index avg `0.0508` n `25`; metal avg `0.0772` n `20`; unknown avg `0.2342` n `782`
- 24h: commodity avg `-1.3032` n `12`; crypto_alt avg `1.6031` n `230`; crypto_major avg `2.0443` n `8`; equity avg `1.6173` n `102`; fx avg `-0.0975` n `6`; index avg `0.2991` n `25`; metal avg `0.3149` n `20`; unknown avg `1.6315` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
