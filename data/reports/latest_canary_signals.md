# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T17:07:29.767427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1144` n `13`; crypto_alt avg `-0.1281` n `238`; crypto_major avg `-0.1651` n `8`; equity avg `-0.1406` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0053` n `27`; metal avg `0.0625` n `20`; unknown avg `6.1914` n `1232`
- 1h: commodity avg `0.1838` n `13`; crypto_alt avg `-0.8226` n `238`; crypto_major avg `-0.6395` n `8`; equity avg `-0.5266` n `156`; fx avg `-0.0062` n `6`; index avg `-0.0351` n `27`; metal avg `0.0179` n `20`; unknown avg `8.2787` n `1232`
- 4h: commodity avg `0.3278` n `13`; crypto_alt avg `1.3162` n `238`; crypto_major avg `1.4437` n `8`; equity avg `0.2557` n `156`; fx avg `0.1244` n `6`; index avg `-0.0368` n `27`; metal avg `0.0037` n `20`; unknown avg `1.4782` n `1132`
- 24h: commodity avg `-0.5987` n `13`; crypto_alt avg `1.3156` n `238`; crypto_major avg `2.7495` n `8`; equity avg `-0.7266` n `155`; fx avg `0.0112` n `6`; index avg `-0.1538` n `27`; metal avg `-0.4143` n `20`; unknown avg `13.4152` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
