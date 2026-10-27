# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T08:07:35.078162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `-0.1484` n `238`; crypto_major avg `-0.1147` n `8`; equity avg `0.1145` n `154`; fx avg `-0.0002` n `6`; index avg `-0.0104` n `27`; metal avg `-0.023` n `20`; unknown avg `0.0738` n `1214`
- 1h: commodity avg `0.1001` n `13`; crypto_alt avg `0.435` n `238`; crypto_major avg `0.3644` n `8`; equity avg `0.2526` n `154`; fx avg `0.0357` n `6`; index avg `0.0178` n `27`; metal avg `0.0104` n `20`; unknown avg `65.1523` n `1200`
- 4h: commodity avg `0.3333` n `13`; crypto_alt avg `0.4957` n `237`; crypto_major avg `0.0651` n `8`; equity avg `-0.5684` n `154`; fx avg `-0.0069` n `6`; index avg `-0.0712` n `27`; metal avg `-0.3094` n `20`; unknown avg `-0.0467` n `1168`
- 24h: commodity avg `0.2793` n `13`; crypto_alt avg `0.9393` n `237`; crypto_major avg `0.7854` n `8`; equity avg `0.9408` n `153`; fx avg `-0.0122` n `6`; index avg `0.3286` n `27`; metal avg `-0.3705` n `20`; unknown avg `1061.4883` n `1008`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
