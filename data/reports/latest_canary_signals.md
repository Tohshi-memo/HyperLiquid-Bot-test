# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:49:49.636927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0962` n `230`; crypto_major avg `0.1507` n `8`; equity avg `0.0581` n `121`; fx avg `-0.0035` n `6`; index avg `0.0047` n `25`; metal avg `0.0275` n `20`; unknown avg `0.0226` n `792`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.16` n `230`; crypto_major avg `0.2003` n `8`; equity avg `0.0491` n `121`; fx avg `0.0154` n `6`; index avg `0.0125` n `25`; metal avg `-0.0387` n `20`; unknown avg `0.3333` n `792`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.2641` n `230`; crypto_major avg `-0.4505` n `8`; equity avg `0.0262` n `121`; fx avg `0.042` n `6`; index avg `0.0516` n `25`; metal avg `-0.0944` n `20`; unknown avg `-0.1021` n `792`
- 24h: commodity avg `-0.0766` n `12`; crypto_alt avg `5.4857` n `230`; crypto_major avg `9.6508` n `8`; equity avg `1.6207` n `120`; fx avg `0.0765` n `6`; index avg `0.4028` n `25`; metal avg `1.1133` n `20`; unknown avg `1.7986` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
