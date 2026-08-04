# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T17:37:39.586976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.009` n `230`; crypto_major avg `0.0819` n `8`; equity avg `0.2734` n `107`; fx avg `0.0071` n `6`; index avg `0.0538` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.0916` n `782`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `0.1932` n `230`; crypto_major avg `0.3025` n `8`; equity avg `0.4331` n `107`; fx avg `0.0034` n `6`; index avg `0.1035` n `25`; metal avg `0.0357` n `20`; unknown avg `-0.1302` n `782`
- 4h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.0024` n `230`; crypto_major avg `0.0949` n `8`; equity avg `1.5291` n `107`; fx avg `0.0602` n `6`; index avg `0.3894` n `25`; metal avg `0.2197` n `20`; unknown avg `-0.3937` n `782`
- 24h: commodity avg `-1.135` n `12`; crypto_alt avg `-0.1991` n `230`; crypto_major avg `0.3078` n `8`; equity avg `4.2261` n `107`; fx avg `0.0893` n `6`; index avg `0.8192` n `25`; metal avg `1.2102` n `20`; unknown avg `0.4038` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
