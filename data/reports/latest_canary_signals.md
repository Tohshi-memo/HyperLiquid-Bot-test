# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T22:22:31.187364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.1746` n `235`; crypto_major avg `0.0332` n `8`; equity avg `-0.0048` n `150`; fx avg `0.0079` n `6`; index avg `0.0005` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.1772` n `1077`
- 1h: commodity avg `0.1515` n `13`; crypto_alt avg `0.0139` n `235`; crypto_major avg `-0.1987` n `8`; equity avg `0.0219` n `150`; fx avg `0.0011` n `6`; index avg `0.0159` n `26`; metal avg `-0.0202` n `20`; unknown avg `-0.3735` n `1075`
- 4h: commodity avg `0.3096` n `13`; crypto_alt avg `0.4748` n `235`; crypto_major avg `0.0722` n `8`; equity avg `0.0491` n `150`; fx avg `0.0275` n `6`; index avg `0.0222` n `26`; metal avg `-0.0603` n `20`; unknown avg `-0.0402` n `999`
- 24h: commodity avg `0.4975` n `13`; crypto_alt avg `-4.0213` n `235`; crypto_major avg `-3.6251` n `8`; equity avg `-1.4128` n `150`; fx avg `-0.1436` n `6`; index avg `-0.2086` n `26`; metal avg `-0.7031` n `20`; unknown avg `246.9777` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
