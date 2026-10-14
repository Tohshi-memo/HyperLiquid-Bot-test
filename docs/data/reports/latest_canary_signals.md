# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T18:37:28.703904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `13`; crypto_alt avg `-0.1274` n `236`; crypto_major avg `-0.0356` n `8`; equity avg `-0.1454` n `151`; fx avg `-0.0077` n `6`; index avg `-0.0264` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.2629` n `1134`
- 1h: commodity avg `-0.0529` n `13`; crypto_alt avg `-0.2503` n `236`; crypto_major avg `-0.356` n `8`; equity avg `-0.1949` n `151`; fx avg `-0.0264` n `6`; index avg `-0.0223` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.9046` n `1130`
- 4h: commodity avg `0.0838` n `13`; crypto_alt avg `0.2547` n `236`; crypto_major avg `-0.1106` n `8`; equity avg `-1.5588` n `151`; fx avg `-0.0172` n `6`; index avg `-0.251` n `26`; metal avg `-0.2057` n `20`; unknown avg `0.1405` n `1099`
- 24h: commodity avg `-0.0201` n `13`; crypto_alt avg `-2.2989` n `236`; crypto_major avg `-2.0942` n `8`; equity avg `-3.7903` n `151`; fx avg `-0.1726` n `6`; index avg `-0.5291` n `26`; metal avg `-0.8347` n `20`; unknown avg `1268.6461` n `976`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.062`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0604`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.059`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
