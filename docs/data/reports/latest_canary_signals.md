# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T14:37:27.901355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0738` n `12`; crypto_alt avg `0.2554` n `230`; crypto_major avg `0.5633` n `8`; equity avg `0.6171` n `102`; fx avg `-0.0033` n `6`; index avg `0.0814` n `25`; metal avg `0.0246` n `20`; unknown avg `-0.108` n `785`
- 1h: commodity avg `0.1009` n `12`; crypto_alt avg `0.5539` n `230`; crypto_major avg `0.9554` n `8`; equity avg `1.8331` n `102`; fx avg `-0.0157` n `6`; index avg `0.1317` n `25`; metal avg `0.1334` n `20`; unknown avg `0.0274` n `785`
- 4h: commodity avg `-0.0366` n `12`; crypto_alt avg `0.9261` n `230`; crypto_major avg `1.1941` n `8`; equity avg `1.6352` n `102`; fx avg `-0.0675` n `6`; index avg `0.0677` n `25`; metal avg `-0.2729` n `20`; unknown avg `0.383` n `785`
- 24h: commodity avg `-0.2925` n `12`; crypto_alt avg `0.157` n `230`; crypto_major avg `0.9716` n `8`; equity avg `1.1456` n `102`; fx avg `-0.206` n `6`; index avg `-0.0571` n `25`; metal avg `-0.4706` n `20`; unknown avg `1.4189` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
