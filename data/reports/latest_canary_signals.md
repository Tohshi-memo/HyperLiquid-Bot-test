# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T19:07:29.065844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `-0.3284` n `237`; crypto_major avg `-0.1681` n `8`; equity avg `-0.2472` n `152`; fx avg `0.0053` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0093` n `20`; unknown avg `155.6928` n `1228`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `-0.5191` n `237`; crypto_major avg `-0.3062` n `8`; equity avg `-0.3036` n `152`; fx avg `0.0053` n `6`; index avg `-0.0405` n `26`; metal avg `-0.029` n `20`; unknown avg `17.1842` n `1229`
- 4h: commodity avg `0.2274` n `13`; crypto_alt avg `-0.4826` n `237`; crypto_major avg `-0.4976` n `8`; equity avg `-0.4858` n `152`; fx avg `-0.0181` n `6`; index avg `-0.0735` n `26`; metal avg `-0.0407` n `20`; unknown avg `-0.2242` n `1197`
- 24h: commodity avg `0.3472` n `13`; crypto_alt avg `0.788` n `237`; crypto_major avg `0.572` n `8`; equity avg `1.4156` n `152`; fx avg `-0.0947` n `6`; index avg `0.0739` n `26`; metal avg `-0.1078` n `20`; unknown avg `-0.8344` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
