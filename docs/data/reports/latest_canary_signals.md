# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T13:00:39.165588+00:00`
- Correlation status: `ready`
- Asset price records: `267`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4635` n `7`; crypto_alt avg `-0.2481` n `223`; crypto_major avg `-0.4432` n `7`; equity avg `-0.2375` n `42`; fx avg `0.0047` n `4`; index avg `-0.1435` n `9`; metal avg `-0.2088` n `7`; unknown avg `-0.0807` n `314`
- 1h: commodity avg `0.0071` n `7`; crypto_alt avg `-0.1935` n `223`; crypto_major avg `-0.2549` n `7`; equity avg `-0.2158` n `42`; fx avg `0.0179` n `4`; index avg `-0.0473` n `9`; metal avg `0.2898` n `7`; unknown avg `0.1637` n `314`
- 4h: commodity avg `0.1634` n `7`; crypto_alt avg `-1.0073` n `223`; crypto_major avg `-1.3113` n `7`; equity avg `-0.5931` n `42`; fx avg `-0.0023` n `4`; index avg `-0.3149` n `9`; metal avg `-0.3737` n `7`; unknown avg `-0.2394` n `314`
- 24h: commodity avg `0.8571` n `7`; crypto_alt avg `0.6978` n `223`; crypto_major avg `0.1553` n `7`; equity avg `0.1367` n `42`; fx avg `-0.0607` n `4`; index avg `0.3583` n `9`; metal avg `-1.4681` n `7`; unknown avg `0.0283` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2688`, n `263`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2607`, n `263`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1813`, n `259`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1703`, n `259`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1678`, n `263`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1672`, n `259`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1662`, n `259`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `263`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1613`, n `259`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.159`, n `263`, weak_sample_signal
