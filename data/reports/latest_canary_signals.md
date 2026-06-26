# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T09:52:31.183525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.071` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.642` n `228`; crypto_major avg `-0.725` n `8`; equity avg `0.0372` n `86`; fx avg `-0.0096` n `6`; index avg `0.0192` n `23`; metal avg `-0.0335` n `20`; unknown avg `0.0783` n `765`
- 1h: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.6402` n `228`; crypto_major avg `-1.0653` n `8`; equity avg `0.0076` n `86`; fx avg `-0.013` n `6`; index avg `0.0057` n `23`; metal avg `0.2003` n `20`; unknown avg `-0.022` n `765`
- 4h: commodity avg `-0.3556` n `12`; crypto_alt avg `0.207` n `228`; crypto_major avg `0.0813` n `8`; equity avg `0.1916` n `86`; fx avg `-0.0215` n `6`; index avg `0.0631` n `23`; metal avg `0.7033` n `20`; unknown avg `0.1755` n `733`
- 24h: commodity avg `-0.0015` n `12`; crypto_alt avg `-2.2097` n `228`; crypto_major avg `-2.5543` n `8`; equity avg `-4.0313` n `86`; fx avg `0.0066` n `6`; index avg `-0.5806` n `23`; metal avg `0.5554` n `20`; unknown avg `0.7991` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.267`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
