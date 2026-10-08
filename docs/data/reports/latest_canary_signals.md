# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T14:22:36.753510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1091` n `13`; crypto_alt avg `0.4848` n `235`; crypto_major avg `0.2715` n `8`; equity avg `0.1574` n `150`; fx avg `0.0014` n `6`; index avg `0.0254` n `26`; metal avg `0.0463` n `20`; unknown avg `0.2999` n `1077`
- 1h: commodity avg `0.211` n `13`; crypto_alt avg `0.7342` n `235`; crypto_major avg `0.0666` n `8`; equity avg `-0.1405` n `150`; fx avg `0.0404` n `6`; index avg `0.0119` n `26`; metal avg `0.062` n `20`; unknown avg `8.2556` n `1051`
- 4h: commodity avg `0.1283` n `13`; crypto_alt avg `-0.2811` n `235`; crypto_major avg `-0.8997` n `8`; equity avg `-0.1325` n `150`; fx avg `0.0378` n `6`; index avg `0.0705` n `26`; metal avg `-0.0276` n `20`; unknown avg `3.1378` n `1045`
- 24h: commodity avg `0.8716` n `13`; crypto_alt avg `1.43` n `235`; crypto_major avg `-1.4424` n `8`; equity avg `-1.1947` n `150`; fx avg `0.0821` n `6`; index avg `-0.0588` n `26`; metal avg `0.1011` n `20`; unknown avg `0.3216` n `968`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
