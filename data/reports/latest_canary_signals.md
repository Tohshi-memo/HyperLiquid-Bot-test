# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T02:07:25.299787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.1508` n `237`; crypto_major avg `0.1639` n `8`; equity avg `0.0024` n `152`; fx avg `0.0005` n `6`; index avg `0.0045` n `26`; metal avg `0.007` n `20`; unknown avg `0.3855` n `1229`
- 1h: commodity avg `-0.0195` n `13`; crypto_alt avg `-0.0751` n `237`; crypto_major avg `0.2932` n `8`; equity avg `0.0003` n `152`; fx avg `-0.0064` n `6`; index avg `-0.0002` n `26`; metal avg `0.0061` n `20`; unknown avg `0.4525` n `1221`
- 4h: commodity avg `-0.0583` n `13`; crypto_alt avg `0.3734` n `237`; crypto_major avg `0.9412` n `8`; equity avg `0.223` n `152`; fx avg `-0.0039` n `6`; index avg `0.0144` n `26`; metal avg `0.0438` n `20`; unknown avg `158.4362` n `1215`
- 24h: commodity avg `-0.0161` n `13`; crypto_alt avg `-1.0335` n `237`; crypto_major avg `0.0068` n `8`; equity avg `0.0296` n `152`; fx avg `-0.0358` n `6`; index avg `0.007` n `26`; metal avg `-0.0727` n `20`; unknown avg `0.4312` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
