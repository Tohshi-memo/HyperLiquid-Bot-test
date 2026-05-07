# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T04:52:10.871202+00:00`
- Correlation status: `ready`
- Asset price records: `519`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0891` n `12`; crypto_alt avg `0.1259` n `228`; crypto_major avg `0.0441` n `8`; equity avg `0.0245` n `65`; fx avg `0.001` n `4`; index avg `0.0191` n `23`; metal avg `0.036` n `18`; unknown avg `0.0738` n `358`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.6296` n `228`; crypto_major avg `0.1652` n `8`; equity avg `0.0747` n `65`; fx avg `-0.0409` n `4`; index avg `0.0043` n `23`; metal avg `-0.0603` n `18`; unknown avg `0.1257` n `358`
- 4h: commodity avg `-0.2935` n `12`; crypto_alt avg `0.1878` n `228`; crypto_major avg `-0.3682` n `8`; equity avg `0.4088` n `65`; fx avg `0.0248` n `4`; index avg `0.1367` n `23`; metal avg `0.1611` n `18`; unknown avg `-0.2871` n `357`
- 24h: commodity avg `-1.7345` n `7`; crypto_alt avg `0.811` n `223`; crypto_major avg `-1.0375` n `7`; equity avg `1.2172` n `47`; fx avg `0.0725` n `4`; index avg `1.0143` n `6`; metal avg `1.4725` n `7`; unknown avg `1.8645` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `515`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `515`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `515`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `515`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `511`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `511`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0708`, n `511`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0698`, n `511`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.068`, n `511`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `515`, weak_sample_signal
