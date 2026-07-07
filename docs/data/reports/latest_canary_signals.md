# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T00:22:25.955364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.1491` n `229`; crypto_major avg `0.1948` n `8`; equity avg `-0.1115` n `91`; fx avg `-0.0005` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.1408` n `763`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `0.0458` n `229`; crypto_major avg `0.0602` n `8`; equity avg `-0.2281` n `91`; fx avg `-0.001` n `6`; index avg `-0.0754` n `25`; metal avg `-0.0594` n `20`; unknown avg `1.6262` n `763`
- 4h: commodity avg `0.0884` n `12`; crypto_alt avg `0.346` n `229`; crypto_major avg `0.362` n `8`; equity avg `-0.5816` n `91`; fx avg `0.0131` n `6`; index avg `-0.1301` n `25`; metal avg `-0.0455` n `20`; unknown avg `1.5872` n `763`
- 24h: commodity avg `0.2993` n `12`; crypto_alt avg `0.8034` n `229`; crypto_major avg `0.1179` n `8`; equity avg `-1.2168` n `90`; fx avg `0.0871` n `6`; index avg `-0.2237` n `25`; metal avg `-0.285` n `20`; unknown avg `-0.3043` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
