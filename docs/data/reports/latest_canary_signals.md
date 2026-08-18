# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T09:28:21.764506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.004` n `230`; crypto_major avg `-0.1207` n `8`; equity avg `-0.1245` n `114`; fx avg `-0.0206` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0414` n `795`
- 1h: commodity avg `-0.0674` n `12`; crypto_alt avg `0.0905` n `230`; crypto_major avg `0.0305` n `8`; equity avg `-0.1612` n `114`; fx avg `-0.0282` n `6`; index avg `-0.0328` n `25`; metal avg `-0.019` n `20`; unknown avg `0.0331` n `795`
- 4h: commodity avg `-0.091` n `12`; crypto_alt avg `0.3468` n `230`; crypto_major avg `-0.0255` n `8`; equity avg `-1.056` n `114`; fx avg `0.001` n `6`; index avg `-0.1738` n `25`; metal avg `-0.1093` n `20`; unknown avg `0.0284` n `761`
- 24h: commodity avg `0.5789` n `12`; crypto_alt avg `-0.6892` n `230`; crypto_major avg `0.1908` n `8`; equity avg `-2.6375` n `114`; fx avg `-0.0094` n `6`; index avg `-0.542` n `25`; metal avg `-0.2714` n `20`; unknown avg `0.075` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
