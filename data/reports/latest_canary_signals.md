# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T20:37:28.930275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.1606` n `232`; crypto_major avg `0.1199` n `8`; equity avg `-0.0018` n `134`; fx avg `0.0049` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0005` n `20`; unknown avg `7.1006` n `790`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `0.034` n `232`; crypto_major avg `-0.0956` n `8`; equity avg `-0.0143` n `134`; fx avg `0.0066` n `6`; index avg `0.0008` n `26`; metal avg `0.015` n `20`; unknown avg `1.2435` n `756`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `0.4` n `232`; crypto_major avg `0.2799` n `8`; equity avg `0.2115` n `134`; fx avg `-0.0095` n `6`; index avg `0.0472` n `26`; metal avg `0.0106` n `20`; unknown avg `-0.2618` n `738`
- 24h: commodity avg `0.2157` n `12`; crypto_alt avg `0.3279` n `232`; crypto_major avg `-0.9358` n `8`; equity avg `0.4347` n `134`; fx avg `-0.1264` n `6`; index avg `0.0841` n `26`; metal avg `0.003` n `20`; unknown avg `7956.5537` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
