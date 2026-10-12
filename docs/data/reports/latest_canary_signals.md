# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T11:37:27.162751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `13`; crypto_alt avg `-0.187` n `235`; crypto_major avg `-0.116` n `8`; equity avg `-0.0569` n `151`; fx avg `0.0156` n `6`; index avg `-0.007` n `26`; metal avg `0.0176` n `20`; unknown avg `0.3219` n `1133`
- 1h: commodity avg `0.1461` n `13`; crypto_alt avg `-0.5539` n `235`; crypto_major avg `-0.3983` n `8`; equity avg `-0.1961` n `151`; fx avg `-0.0025` n `6`; index avg `-0.0227` n `26`; metal avg `-0.0265` n `20`; unknown avg `0.1871` n `1115`
- 4h: commodity avg `0.4966` n `13`; crypto_alt avg `-1.2887` n `235`; crypto_major avg `-0.9642` n `8`; equity avg `-0.7205` n `151`; fx avg `-0.0265` n `6`; index avg `-0.1177` n `26`; metal avg `-0.0812` n `20`; unknown avg `0.4596` n `981`
- 24h: commodity avg `0.0624` n `13`; crypto_alt avg `1.3691` n `235`; crypto_major avg `0.8707` n `8`; equity avg `-1.3022` n `151`; fx avg `-0.1301` n `6`; index avg `-0.1591` n `26`; metal avg `0.0326` n `20`; unknown avg `0.9205` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2403`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
