# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T17:40:11.762157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `0.0726` n `230`; crypto_major avg `0.1674` n `8`; equity avg `0.0428` n `113`; fx avg `0.0045` n `6`; index avg `-0.0224` n `25`; metal avg `0.0067` n `20`; unknown avg `0.0645` n `785`
- 1h: commodity avg `0.1056` n `12`; crypto_alt avg `0.1476` n `230`; crypto_major avg `0.2237` n `8`; equity avg `-0.009` n `113`; fx avg `0.0007` n `6`; index avg `-0.0127` n `25`; metal avg `0.0097` n `20`; unknown avg `0.0883` n `785`
- 4h: commodity avg `0.3754` n `12`; crypto_alt avg `-0.426` n `230`; crypto_major avg `-0.4039` n `8`; equity avg `-0.1439` n `113`; fx avg `0.0136` n `6`; index avg `0.0001` n `25`; metal avg `0.2281` n `20`; unknown avg `1.9277` n `784`
- 24h: commodity avg `1.2605` n `12`; crypto_alt avg `-0.6629` n `230`; crypto_major avg `-1.2565` n `8`; equity avg `-1.2927` n `113`; fx avg `0.2525` n `6`; index avg `-0.0585` n `25`; metal avg `0.0236` n `20`; unknown avg `103.4137` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
