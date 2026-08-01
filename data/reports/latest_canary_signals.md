# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T06:07:27.536958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.0855` n `230`; crypto_major avg `0.0526` n `8`; equity avg `-0.042` n `102`; fx avg `0.0073` n `6`; index avg `0.0037` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0039` n `765`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `-0.1977` n `230`; crypto_major avg `-0.272` n `8`; equity avg `-0.1087` n `102`; fx avg `0.0045` n `6`; index avg `-0.0375` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0665` n `765`
- 4h: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.0733` n `230`; crypto_major avg `-0.2263` n `8`; equity avg `-0.1298` n `102`; fx avg `0.0374` n `6`; index avg `-0.0333` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0028` n `765`
- 24h: commodity avg `0.9389` n `12`; crypto_alt avg `0.134` n `230`; crypto_major avg `-1.782` n `8`; equity avg `-3.0378` n `102`; fx avg `-0.0702` n `6`; index avg `-0.3958` n `25`; metal avg `-0.2415` n `20`; unknown avg `4.647` n `763`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
