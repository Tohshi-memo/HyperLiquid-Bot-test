# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T18:37:28.737199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0479` n `13`; crypto_alt avg `-0.2074` n `237`; crypto_major avg `-0.0964` n `8`; equity avg `-0.049` n `154`; fx avg `-0.0058` n `6`; index avg `-0.0117` n `27`; metal avg `-0.0312` n `20`; unknown avg `0.2095` n `1238`
- 1h: commodity avg `-0.1503` n `13`; crypto_alt avg `-0.5342` n `237`; crypto_major avg `-0.2031` n `8`; equity avg `0.0032` n `154`; fx avg `-0.0148` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0567` n `20`; unknown avg `0.0372` n `1238`
- 4h: commodity avg `0.2031` n `13`; crypto_alt avg `-0.1231` n `237`; crypto_major avg `0.4092` n `8`; equity avg `1.3386` n `154`; fx avg `-0.005` n `6`; index avg `0.0954` n `27`; metal avg `0.0024` n `20`; unknown avg `1.2716` n `1206`
- 24h: commodity avg `-0.2878` n `13`; crypto_alt avg `-0.695` n `237`; crypto_major avg `0.0162` n `8`; equity avg `0.757` n `153`; fx avg `0.0516` n `6`; index avg `-0.0728` n `27`; metal avg `0.0473` n `20`; unknown avg `779.1566` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
