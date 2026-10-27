# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T07:52:24.775840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0733` n `13`; crypto_alt avg `0.2068` n `238`; crypto_major avg `0.3014` n `8`; equity avg `0.0478` n `154`; fx avg `0.0185` n `6`; index avg `0.0152` n `27`; metal avg `0.032` n `20`; unknown avg `-0.1109` n `1220`
- 1h: commodity avg `0.1717` n `13`; crypto_alt avg `0.6722` n `238`; crypto_major avg `0.5117` n `8`; equity avg `-0.0295` n `154`; fx avg `0.0109` n `6`; index avg `0.005` n `27`; metal avg `0.0187` n `20`; unknown avg `64.2182` n `1206`
- 4h: commodity avg `0.3228` n `13`; crypto_alt avg `0.5935` n `237`; crypto_major avg `0.1434` n `8`; equity avg `-1.212` n `154`; fx avg `-0.018` n `6`; index avg `-0.0625` n `27`; metal avg `-0.2584` n `20`; unknown avg `-0.0323` n `1176`
- 24h: commodity avg `0.2428` n `13`; crypto_alt avg `0.8852` n `237`; crypto_major avg `0.5816` n `8`; equity avg `0.5993` n `153`; fx avg `-0.0017` n `6`; index avg `0.3308` n `27`; metal avg `-0.2996` n `20`; unknown avg `1105.5854` n `968`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
