# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T11:52:26.283136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.0131` n `230`; crypto_major avg `-0.0067` n `8`; equity avg `0.0061` n `92`; fx avg `0.0037` n `6`; index avg `0.0023` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0006` n `765`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `0.1466` n `230`; crypto_major avg `0.0366` n `8`; equity avg `-0.031` n `92`; fx avg `0.0031` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0152` n `20`; unknown avg `-0.1317` n `765`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `0.234` n `230`; crypto_major avg `0.2061` n `8`; equity avg `0.0504` n `92`; fx avg `-0.0077` n `6`; index avg `0.0058` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.194` n `761`
- 24h: commodity avg `-0.3424` n `12`; crypto_alt avg `0.1429` n `229`; crypto_major avg `-0.5916` n `8`; equity avg `-0.3315` n `92`; fx avg `-0.1075` n `6`; index avg `0.1294` n `25`; metal avg `0.0996` n `20`; unknown avg `2.8037` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
