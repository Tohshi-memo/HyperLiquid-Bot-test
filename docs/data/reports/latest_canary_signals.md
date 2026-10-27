# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T13:52:39.501755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0271` n `13`; crypto_alt avg `-0.1866` n `238`; crypto_major avg `-0.2371` n `8`; equity avg `-0.2228` n `154`; fx avg `0.005` n `6`; index avg `-0.068` n `27`; metal avg `-0.0632` n `20`; unknown avg `1.0051` n `1238`
- 1h: commodity avg `-0.0507` n `13`; crypto_alt avg `-0.5608` n `238`; crypto_major avg `-0.4489` n `8`; equity avg `-0.0502` n `154`; fx avg `-0.0219` n `6`; index avg `-0.0936` n `27`; metal avg `0.0109` n `20`; unknown avg `3.4395` n `1234`
- 4h: commodity avg `-0.2456` n `13`; crypto_alt avg `0.6511` n `238`; crypto_major avg `0.8084` n `8`; equity avg `0.8806` n `154`; fx avg `0.0265` n `6`; index avg `0.0524` n `27`; metal avg `0.1797` n `20`; unknown avg `10.744` n `1182`
- 24h: commodity avg `-0.275` n `13`; crypto_alt avg `0.0144` n `237`; crypto_major avg `0.7227` n `8`; equity avg `1.5343` n `154`; fx avg `-0.0175` n `6`; index avg `0.3003` n `27`; metal avg `0.031` n `20`; unknown avg `1039.3871` n `1050`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
