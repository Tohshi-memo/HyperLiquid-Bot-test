# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T20:52:28.537077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.2002` n `237`; crypto_major avg `-0.1526` n `8`; equity avg `-0.0191` n `151`; fx avg `0.0076` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0018` n `20`; unknown avg `2.6478` n `1196`
- 1h: commodity avg `-0.0167` n `13`; crypto_alt avg `-0.0283` n `237`; crypto_major avg `0.1999` n `8`; equity avg `-0.0001` n `151`; fx avg `0.0068` n `6`; index avg `0.0191` n `26`; metal avg `-0.0314` n `20`; unknown avg `2.0798` n `1128`
- 4h: commodity avg `-0.1393` n `13`; crypto_alt avg `-0.5558` n `237`; crypto_major avg `-0.1368` n `8`; equity avg `-0.3161` n `151`; fx avg `0.0119` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0186` n `20`; unknown avg `-0.0772` n `1128`
- 24h: commodity avg `-0.2982` n `13`; crypto_alt avg `2.9405` n `237`; crypto_major avg `2.31` n `8`; equity avg `2.9123` n `151`; fx avg `-0.0099` n `6`; index avg `0.5824` n `26`; metal avg `0.1064` n `20`; unknown avg `3.3615` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
