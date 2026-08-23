# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:22:42.224164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.1924` n `231`; crypto_major avg `0.137` n `8`; equity avg `0.016` n `122`; fx avg `0.0007` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0205` n `793`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `0.6227` n `231`; crypto_major avg `0.57` n `8`; equity avg `0.0831` n `122`; fx avg `0.0038` n `6`; index avg `0.0148` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.0348` n `793`
- 4h: commodity avg `-0.0159` n `12`; crypto_alt avg `1.3216` n `231`; crypto_major avg `0.0683` n `8`; equity avg `0.1443` n `122`; fx avg `-0.0012` n `6`; index avg `0.0403` n `25`; metal avg `0.0141` n `20`; unknown avg `0.8881` n `793`
- 24h: commodity avg `0.0381` n `12`; crypto_alt avg `2.1934` n `231`; crypto_major avg `1.1562` n `8`; equity avg `0.6798` n `122`; fx avg `0.0265` n `6`; index avg `0.0843` n `25`; metal avg `0.0666` n `20`; unknown avg `7.3438` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
