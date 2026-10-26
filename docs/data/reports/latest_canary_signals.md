# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T09:52:34.280489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.1169` n `237`; crypto_major avg `0.0416` n `8`; equity avg `0.1415` n `152`; fx avg `-0.0025` n `6`; index avg `0.0227` n `26`; metal avg `0.0278` n `20`; unknown avg `-0.1516` n `1240`
- 1h: commodity avg `0.0229` n `13`; crypto_alt avg `-0.0613` n `237`; crypto_major avg `0.168` n `8`; equity avg `0.4237` n `152`; fx avg `0.0078` n `6`; index avg `0.0577` n `26`; metal avg `0.0591` n `20`; unknown avg `-0.2173` n `1240`
- 4h: commodity avg `0.0978` n `13`; crypto_alt avg `0.0433` n `237`; crypto_major avg `0.2125` n `8`; equity avg `0.1006` n `152`; fx avg `0.0103` n `6`; index avg `0.0528` n `26`; metal avg `0.0961` n `20`; unknown avg `-0.4246` n `1126`
- 24h: commodity avg `-0.4416` n `13`; crypto_alt avg `0.5156` n `237`; crypto_major avg `0.5564` n `8`; equity avg `0.1479` n `152`; fx avg `0.0623` n `6`; index avg `0.0919` n `26`; metal avg `0.2667` n `20`; unknown avg `-0.3859` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2611`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
