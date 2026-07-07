# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T00:07:27.449200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.0585` n `229`; crypto_major avg `0.0123` n `8`; equity avg `0.1149` n `91`; fx avg `-0.0018` n `6`; index avg `-0.004` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.2553` n `763`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `-0.2889` n `229`; crypto_major avg `-0.4042` n `8`; equity avg `-0.3406` n `91`; fx avg `-0.0121` n `6`; index avg `-0.0922` n `25`; metal avg `-0.0584` n `20`; unknown avg `2.0125` n `763`
- 4h: commodity avg `0.0735` n `12`; crypto_alt avg `0.2113` n `229`; crypto_major avg `0.1455` n `8`; equity avg `-0.4849` n `91`; fx avg `0.0127` n `6`; index avg `-0.1215` n `25`; metal avg `-0.0418` n `20`; unknown avg `1.4577` n `763`
- 24h: commodity avg `0.3076` n `12`; crypto_alt avg `0.4531` n `229`; crypto_major avg `-0.2181` n `8`; equity avg `-1.0382` n `90`; fx avg `0.0402` n `6`; index avg `-0.1741` n `25`; metal avg `-0.2135` n `20`; unknown avg `-0.2425` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
