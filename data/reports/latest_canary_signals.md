# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T13:22:30.977417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.4535` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.3732` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0729` n `12`; crypto_alt avg `-0.9075` n `228`; crypto_major avg `-0.7828` n `8`; equity avg `-0.1084` n `86`; fx avg `0.0063` n `6`; index avg `-0.014` n `23`; metal avg `-0.1247` n `20`; unknown avg `-0.0559` n `764`
- 1h: commodity avg `-0.2339` n `12`; crypto_alt avg `-1.5979` n `228`; crypto_major avg `-1.5591` n `8`; equity avg `-0.6411` n `86`; fx avg `-0.0142` n `6`; index avg `-0.1056` n `23`; metal avg `-0.5586` n `20`; unknown avg `-0.0193` n `764`
- 4h: commodity avg `-0.3603` n `12`; crypto_alt avg `-1.4743` n `228`; crypto_major avg `-1.3871` n `8`; equity avg `-0.5879` n `86`; fx avg `-0.0836` n `6`; index avg `-0.0139` n `23`; metal avg `-1.2978` n `20`; unknown avg `-0.0152` n `764`
- 24h: commodity avg `-0.7586` n `12`; crypto_alt avg `-1.2443` n `228`; crypto_major avg `-1.1585` n `8`; equity avg `4.5001` n `86`; fx avg `-0.0235` n `6`; index avg `0.2029` n `23`; metal avg `-1.6108` n `20`; unknown avg `-0.2512` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
