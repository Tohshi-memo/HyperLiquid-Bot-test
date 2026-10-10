# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T11:52:26.248950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `0.0271` n `235`; crypto_major avg `0.0658` n `8`; equity avg `0.0124` n `150`; fx avg `0.0038` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0012` n `20`; unknown avg `1.1626` n `1117`
- 1h: commodity avg `0.0072` n `13`; crypto_alt avg `0.0202` n `235`; crypto_major avg `0.0558` n `8`; equity avg `0.0285` n `150`; fx avg `-0.0058` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.8546` n `1115`
- 4h: commodity avg `-0.2557` n `13`; crypto_alt avg `0.025` n `235`; crypto_major avg `-0.0256` n `8`; equity avg `0.0375` n `150`; fx avg `-0.0074` n `6`; index avg `0.0081` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.2837` n `1099`
- 24h: commodity avg `-0.1783` n `13`; crypto_alt avg `1.1839` n `235`; crypto_major avg `-0.3219` n `8`; equity avg `-0.3139` n `150`; fx avg `0.0048` n `6`; index avg `-0.0286` n `26`; metal avg `0.0254` n `20`; unknown avg `631.7622` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
