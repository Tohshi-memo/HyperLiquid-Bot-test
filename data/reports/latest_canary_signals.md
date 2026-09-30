# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T15:37:32.932797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.098` n `12`; crypto_alt avg `0.2757` n `234`; crypto_major avg `0.2491` n `8`; equity avg `0.1072` n `142`; fx avg `-0.0101` n `6`; index avg `0.0216` n `26`; metal avg `0.0154` n `20`; unknown avg `0.0166` n `969`
- 1h: commodity avg `0.0864` n `12`; crypto_alt avg `0.2454` n `234`; crypto_major avg `0.3732` n `8`; equity avg `0.0939` n `142`; fx avg `0.0143` n `6`; index avg `0.0192` n `26`; metal avg `-0.0253` n `20`; unknown avg `0.174` n `909`
- 4h: commodity avg `0.0858` n `12`; crypto_alt avg `-0.0887` n `234`; crypto_major avg `-0.268` n `8`; equity avg `0.1111` n `142`; fx avg `-0.0041` n `6`; index avg `0.1157` n `26`; metal avg `-0.2013` n `20`; unknown avg `5.185` n `875`
- 24h: commodity avg `0.0428` n `12`; crypto_alt avg `0.5018` n `234`; crypto_major avg `0.4412` n `8`; equity avg `-0.1233` n `142`; fx avg `0.056` n `6`; index avg `0.1655` n `26`; metal avg `-0.0031` n `20`; unknown avg `17.7966` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
