# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T14:58:19.203002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.149` n `230`; crypto_major avg `0.0746` n `8`; equity avg `-0.0622` n `109`; fx avg `-0.0301` n `6`; index avg `-0.0108` n `25`; metal avg `0.002` n `20`; unknown avg `0.1612` n `781`
- 1h: commodity avg `0.0578` n `12`; crypto_alt avg `0.1855` n `230`; crypto_major avg `0.3406` n `8`; equity avg `1.0956` n `109`; fx avg `0.0119` n `6`; index avg `0.1192` n `25`; metal avg `0.148` n `20`; unknown avg `0.3772` n `781`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.63` n `230`; crypto_major avg `0.217` n `8`; equity avg `1.5634` n `109`; fx avg `0.0203` n `6`; index avg `0.1782` n `25`; metal avg `-0.1068` n `20`; unknown avg `0.5767` n `781`
- 24h: commodity avg `0.2334` n `12`; crypto_alt avg `0.6145` n `230`; crypto_major avg `-0.5044` n `8`; equity avg `0.1542` n `109`; fx avg `0.017` n `6`; index avg `-0.1777` n `25`; metal avg `0.1947` n `20`; unknown avg `113.3756` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
