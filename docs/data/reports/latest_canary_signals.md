# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T10:22:20.426340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `-0.2416` n `228`; crypto_major avg `-0.0944` n `8`; equity avg `-0.1097` n `66`; fx avg `0.0093` n `6`; index avg `-0.0395` n `23`; metal avg `-0.0641` n `18`; unknown avg `-0.1351` n `383`
- 1h: commodity avg `-0.0871` n `12`; crypto_alt avg `-0.1776` n `228`; crypto_major avg `-0.2344` n `8`; equity avg `-0.3` n `66`; fx avg `0.037` n `6`; index avg `-0.1632` n `23`; metal avg `-0.0876` n `18`; unknown avg `-0.2458` n `383`
- 4h: commodity avg `0.1026` n `12`; crypto_alt avg `-0.7874` n `228`; crypto_major avg `-0.4141` n `8`; equity avg `-0.4715` n `66`; fx avg `-0.0516` n `6`; index avg `-0.346` n `23`; metal avg `-0.5017` n `18`; unknown avg `-0.4834` n `383`
- 24h: commodity avg `0.4767` n `12`; crypto_alt avg `1.5436` n `228`; crypto_major avg `0.7469` n `8`; equity avg `-1.7192` n `66`; fx avg `0.2489` n `6`; index avg `-0.8412` n `23`; metal avg `-0.1344` n `18`; unknown avg `0.7022` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
