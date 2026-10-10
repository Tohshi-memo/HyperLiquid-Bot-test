# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T14:37:27.911604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `0.4049` n `235`; crypto_major avg `0.466` n `8`; equity avg `0.0466` n `150`; fx avg `0.003` n `6`; index avg `0.0037` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.0894` n `1117`
- 1h: commodity avg `0.0155` n `13`; crypto_alt avg `0.5888` n `235`; crypto_major avg `0.6853` n `8`; equity avg `0.0445` n `150`; fx avg `0.0013` n `6`; index avg `0.0102` n `26`; metal avg `0.0008` n `20`; unknown avg `0.2389` n `1115`
- 4h: commodity avg `0.1013` n `13`; crypto_alt avg `0.9275` n `235`; crypto_major avg `0.8615` n `8`; equity avg `0.1013` n `150`; fx avg `-0.0077` n `6`; index avg `-0.0006` n `26`; metal avg `0.006` n `20`; unknown avg `0.9541` n `1109`
- 24h: commodity avg `-0.5072` n `13`; crypto_alt avg `2.635` n `235`; crypto_major avg `0.8758` n `8`; equity avg `0.332` n `150`; fx avg `0.0056` n `6`; index avg `0.0571` n `26`; metal avg `0.0158` n `20`; unknown avg `0.6805` n `936`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
