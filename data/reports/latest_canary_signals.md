# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T19:07:29.683510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.2316` n `236`; crypto_major avg `-0.1821` n `8`; equity avg `-0.1509` n `151`; fx avg `0.0049` n `6`; index avg `-0.031` n `26`; metal avg `-0.0149` n `20`; unknown avg `-0.3423` n `1134`
- 1h: commodity avg `-0.1414` n `13`; crypto_alt avg `-0.0502` n `236`; crypto_major avg `-0.0234` n `8`; equity avg `-0.256` n `151`; fx avg `-0.0016` n `6`; index avg `-0.0478` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.4034` n `1130`
- 4h: commodity avg `-0.015` n `13`; crypto_alt avg `0.3026` n `236`; crypto_major avg `-0.0805` n `8`; equity avg `-1.35` n `151`; fx avg `-0.001` n `6`; index avg `-0.2325` n `26`; metal avg `-0.1268` n `20`; unknown avg `-0.1657` n `1100`
- 24h: commodity avg `-0.0948` n `13`; crypto_alt avg `-2.8123` n `236`; crypto_major avg `-2.436` n `8`; equity avg `-3.9808` n `151`; fx avg `-0.1754` n `6`; index avg `-0.5756` n `26`; metal avg `-0.8953` n `20`; unknown avg `1268.8987` n `976`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0629`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0605`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
