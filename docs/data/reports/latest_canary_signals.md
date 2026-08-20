# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T03:37:27.608242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.0436` n `230`; crypto_major avg `0.0675` n `8`; equity avg `-0.0566` n `121`; fx avg `0.0066` n `6`; index avg `-0.0349` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.1733` n `792`
- 1h: commodity avg `0.0284` n `12`; crypto_alt avg `-0.3639` n `230`; crypto_major avg `-0.5412` n `8`; equity avg `-0.1162` n `121`; fx avg `0.0317` n `6`; index avg `-0.0453` n `25`; metal avg `0.0241` n `20`; unknown avg `-0.1795` n `792`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `-0.1466` n `230`; crypto_major avg `-0.7636` n `8`; equity avg `-0.1056` n `121`; fx avg `0.1039` n `6`; index avg `0.038` n `25`; metal avg `-0.1279` n `20`; unknown avg `-0.1665` n `792`
- 24h: commodity avg `-0.0629` n `12`; crypto_alt avg `5.0095` n `230`; crypto_major avg `9.2209` n `8`; equity avg `0.7937` n `120`; fx avg `0.0604` n `6`; index avg `0.2383` n `25`; metal avg `0.9937` n `20`; unknown avg `1.6024` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
