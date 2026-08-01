# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T16:22:27.763722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0801` n `12`; crypto_alt avg `0.1068` n `230`; crypto_major avg `0.0174` n `8`; equity avg `-0.0302` n `102`; fx avg `0.0094` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0125` n `782`
- 1h: commodity avg `0.0929` n `12`; crypto_alt avg `0.1332` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0776` n `102`; fx avg `-0.0037` n `6`; index avg `0.009` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.0477` n `782`
- 4h: commodity avg `0.0735` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `0.0004` n `8`; equity avg `-0.1931` n `102`; fx avg `0.0266` n `6`; index avg `0.014` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.1741` n `782`
- 24h: commodity avg `0.7197` n `12`; crypto_alt avg `0.3467` n `230`; crypto_major avg `-0.4732` n `8`; equity avg `-0.332` n `102`; fx avg `-0.0625` n `6`; index avg `-0.0066` n `25`; metal avg `0.04` n `20`; unknown avg `4.2078` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
