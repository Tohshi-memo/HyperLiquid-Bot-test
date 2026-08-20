# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T01:37:26.233641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2365` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.1916` n `230`; crypto_major avg `0.1422` n `8`; equity avg `-0.0596` n `121`; fx avg `0.0212` n `6`; index avg `0.0121` n `25`; metal avg `-0.0311` n `20`; unknown avg `0.0266` n `792`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.2584` n `230`; crypto_major avg `-0.4864` n `8`; equity avg `-0.0249` n `121`; fx avg `0.0899` n `6`; index avg `0.0371` n `25`; metal avg `-0.16` n `20`; unknown avg `-0.0319` n `792`
- 4h: commodity avg `0.0261` n `12`; crypto_alt avg `-0.1929` n `230`; crypto_major avg `-1.1214` n `8`; equity avg `0.3305` n `121`; fx avg `0.1207` n `6`; index avg `0.1151` n `25`; metal avg `-0.2018` n `20`; unknown avg `-0.0414` n `792`
- 24h: commodity avg `-0.0645` n `12`; crypto_alt avg `5.3816` n `230`; crypto_major avg `9.6217` n `8`; equity avg `0.5985` n `120`; fx avg `-0.0268` n `6`; index avg `0.2109` n `25`; metal avg `0.987` n `20`; unknown avg `1.5681` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
