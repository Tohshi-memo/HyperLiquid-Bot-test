# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T10:22:23.468587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0271` n `12`; crypto_alt avg `-0.1501` n `230`; crypto_major avg `-0.1817` n `8`; equity avg `0.0077` n `102`; fx avg `0.0004` n `6`; index avg `-0.0042` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.0418` n `782`
- 1h: commodity avg `0.203` n `12`; crypto_alt avg `-0.1018` n `230`; crypto_major avg `-0.1975` n `8`; equity avg `0.1254` n `102`; fx avg `0.0026` n `6`; index avg `0.0036` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0466` n `782`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `-0.1615` n `230`; crypto_major avg `-0.4042` n `8`; equity avg `0.1258` n `102`; fx avg `-0.0201` n `6`; index avg `-0.0081` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.1025` n `782`
- 24h: commodity avg `-1.0665` n `12`; crypto_alt avg `0.4077` n `230`; crypto_major avg `0.2016` n `8`; equity avg `1.0293` n `102`; fx avg `-0.136` n `6`; index avg `0.2307` n `25`; metal avg `0.2631` n `20`; unknown avg `0.2722` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
