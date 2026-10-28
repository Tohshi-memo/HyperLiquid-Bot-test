# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T20:52:32.884477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `0.053` n `238`; crypto_major avg `0.0114` n `8`; equity avg `-0.1697` n `155`; fx avg `-0.0` n `6`; index avg `-0.0331` n `27`; metal avg `0.0102` n `20`; unknown avg `0.3093` n `1228`
- 1h: commodity avg `-0.1699` n `13`; crypto_alt avg `-0.2047` n `238`; crypto_major avg `-0.245` n `8`; equity avg `-1.1678` n `155`; fx avg `-0.0057` n `6`; index avg `-0.1574` n `27`; metal avg `-0.0376` n `20`; unknown avg `5.5263` n `1120`
- 4h: commodity avg `-0.2936` n `13`; crypto_alt avg `1.0437` n `238`; crypto_major avg `0.6664` n `8`; equity avg `-0.5973` n `155`; fx avg `-0.0254` n `6`; index avg `-0.1312` n `27`; metal avg `0.0584` n `20`; unknown avg `7.3401` n `1120`
- 24h: commodity avg `0.1226` n `13`; crypto_alt avg `0.8786` n `238`; crypto_major avg `0.6603` n `8`; equity avg `0.9048` n `154`; fx avg `0.2545` n `6`; index avg `0.1717` n `27`; metal avg `-0.0951` n `20`; unknown avg `26.4489` n `1062`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
