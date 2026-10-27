# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T13:22:27.893134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0661` n `13`; crypto_alt avg `0.0414` n `238`; crypto_major avg `0.116` n `8`; equity avg `-0.0675` n `154`; fx avg `-0.0048` n `6`; index avg `-0.007` n `27`; metal avg `-0.0131` n `20`; unknown avg `1.3608` n `1242`
- 1h: commodity avg `-0.0266` n `13`; crypto_alt avg `0.0529` n `238`; crypto_major avg `0.1643` n `8`; equity avg `-0.1204` n `154`; fx avg `0.0095` n `6`; index avg `-0.0423` n `27`; metal avg `0.0523` n `20`; unknown avg `2.31` n `1232`
- 4h: commodity avg `-0.3235` n `13`; crypto_alt avg `0.38` n `238`; crypto_major avg `0.7697` n `8`; equity avg `0.7187` n `154`; fx avg `0.0452` n `6`; index avg `0.076` n `27`; metal avg `0.1857` n `20`; unknown avg `16.8705` n `1182`
- 24h: commodity avg `-0.2881` n `13`; crypto_alt avg `0.0006` n `237`; crypto_major avg `0.5837` n `8`; equity avg `1.2673` n `153`; fx avg `-0.0165` n `6`; index avg `0.3967` n `27`; metal avg `-0.1022` n `20`; unknown avg `1010.2445` n `1050`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
