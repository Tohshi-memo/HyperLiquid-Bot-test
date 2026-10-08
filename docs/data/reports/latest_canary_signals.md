# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T05:37:34.391914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `13`; crypto_alt avg `0.1315` n `235`; crypto_major avg `0.0311` n `8`; equity avg `-0.085` n `150`; fx avg `-0.0004` n `6`; index avg `-0.0157` n `26`; metal avg `-0.016` n `20`; unknown avg `4.3171` n `1077`
- 1h: commodity avg `0.0607` n `13`; crypto_alt avg `0.6742` n `235`; crypto_major avg `0.4076` n `8`; equity avg `0.0022` n `150`; fx avg `0.0072` n `6`; index avg `0.0144` n `26`; metal avg `-0.0298` n `20`; unknown avg `1.3496` n `1075`
- 4h: commodity avg `0.2321` n `13`; crypto_alt avg `-0.5179` n `235`; crypto_major avg `-0.7408` n `8`; equity avg `-0.5787` n `150`; fx avg `0.0504` n `6`; index avg `-0.0503` n `26`; metal avg `-0.0706` n `20`; unknown avg `-0.2218` n `1069`
- 24h: commodity avg `0.4683` n `13`; crypto_alt avg `-0.6519` n `235`; crypto_major avg `-1.96` n `8`; equity avg `-1.3387` n `150`; fx avg `-0.1121` n `6`; index avg `-0.2137` n `26`; metal avg `-0.1828` n `20`; unknown avg `246.8206` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
