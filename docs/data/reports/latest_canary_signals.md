# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T23:07:27.909528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `0.0699` n `235`; crypto_major avg `0.0519` n `8`; equity avg `0.0518` n `150`; fx avg `0.0007` n `6`; index avg `0.0065` n `26`; metal avg `-0.0152` n `20`; unknown avg `0.0674` n `1124`
- 1h: commodity avg `0.0894` n `13`; crypto_alt avg `0.3971` n `235`; crypto_major avg `0.1939` n `8`; equity avg `0.0961` n `150`; fx avg `0.0096` n `6`; index avg `-0.0038` n `26`; metal avg `-0.048` n `20`; unknown avg `-0.0436` n `1124`
- 4h: commodity avg `0.099` n `13`; crypto_alt avg `0.2881` n `235`; crypto_major avg `0.0438` n `8`; equity avg `0.1059` n `150`; fx avg `-0.0172` n `6`; index avg `0.0086` n `26`; metal avg `-0.0523` n `20`; unknown avg `-0.2214` n `1090`
- 24h: commodity avg `0.2181` n `13`; crypto_alt avg `2.0019` n `235`; crypto_major avg `0.6821` n `8`; equity avg `0.3274` n `150`; fx avg `0.0057` n `6`; index avg `0.0376` n `26`; metal avg `0.0045` n `20`; unknown avg `0.5498` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
