# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T04:37:30.869782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `0.2952` n `237`; crypto_major avg `0.2311` n `8`; equity avg `0.092` n `152`; fx avg `-0.0024` n `6`; index avg `0.0081` n `26`; metal avg `0.0291` n `20`; unknown avg `1.5715` n `1238`
- 1h: commodity avg `0.0558` n `13`; crypto_alt avg `0.3277` n `237`; crypto_major avg `0.3538` n `8`; equity avg `0.1578` n `152`; fx avg `0.0118` n `6`; index avg `0.0333` n `26`; metal avg `-0.0099` n `20`; unknown avg `1.7099` n `1230`
- 4h: commodity avg `-0.16` n `13`; crypto_alt avg `-0.6643` n `237`; crypto_major avg `-0.4706` n `8`; equity avg `-0.5158` n `152`; fx avg `-0.0397` n `6`; index avg `-0.0368` n `26`; metal avg `0.0771` n `20`; unknown avg `2.6726` n `1164`
- 24h: commodity avg `-0.6084` n `13`; crypto_alt avg `-1.5121` n `237`; crypto_major avg `-1.3078` n `8`; equity avg `-0.627` n `152`; fx avg `0.0449` n `6`; index avg `0.0191` n `26`; metal avg `0.1727` n `20`; unknown avg `-0.3165` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2507`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
