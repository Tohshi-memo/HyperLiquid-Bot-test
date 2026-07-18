# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T04:11:58.948784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.0275` n `230`; crypto_major avg `0.0563` n `8`; equity avg `-0.0156` n `96`; fx avg `0.0115` n `6`; index avg `0.0164` n `25`; metal avg `0.0026` n `20`; unknown avg `0.6453` n `769`
- 1h: commodity avg `-0.0777` n `12`; crypto_alt avg `-0.0765` n `230`; crypto_major avg `-0.0152` n `8`; equity avg `-0.0276` n `96`; fx avg `0.012` n `6`; index avg `0.0262` n `25`; metal avg `0.0024` n `20`; unknown avg `0.4533` n `769`
- 4h: commodity avg `-0.0956` n `12`; crypto_alt avg `-0.1479` n `230`; crypto_major avg `0.083` n `8`; equity avg `0.1633` n `96`; fx avg `0.0043` n `6`; index avg `0.1095` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.2412` n `769`
- 24h: commodity avg `0.6943` n `12`; crypto_alt avg `-0.4299` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `0.7418` n `96`; fx avg `0.0473` n `6`; index avg `0.0897` n `25`; metal avg `0.2001` n `20`; unknown avg `0.2203` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
