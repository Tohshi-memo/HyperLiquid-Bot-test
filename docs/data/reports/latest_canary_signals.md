# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T18:52:32.445327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0695` n `13`; crypto_alt avg `-0.1596` n `237`; crypto_major avg `-0.0696` n `8`; equity avg `0.0217` n `152`; fx avg `-0.0037` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0195` n `20`; unknown avg `-0.1707` n `1230`
- 1h: commodity avg `0.0334` n `13`; crypto_alt avg `-0.1116` n `237`; crypto_major avg `-0.1669` n `8`; equity avg `-0.0209` n `152`; fx avg `-0.0076` n `6`; index avg `-0.0049` n `26`; metal avg `0.016` n `20`; unknown avg `-0.2078` n `1229`
- 4h: commodity avg `0.1669` n `13`; crypto_alt avg `-0.3874` n `237`; crypto_major avg `-0.5535` n `8`; equity avg `-0.4611` n `152`; fx avg `-0.035` n `6`; index avg `-0.0818` n `26`; metal avg `-0.0461` n `20`; unknown avg `-0.7294` n `1197`
- 24h: commodity avg `0.3375` n `13`; crypto_alt avg `0.9592` n `237`; crypto_major avg `0.5562` n `8`; equity avg `1.5117` n `152`; fx avg `-0.0995` n `6`; index avg `0.0791` n `26`; metal avg `-0.1468` n `20`; unknown avg `-0.7549` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
