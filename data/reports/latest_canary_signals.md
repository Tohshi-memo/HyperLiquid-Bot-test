# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:50:15.944074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0368` n `12`; crypto_alt avg `0.0179` n `230`; crypto_major avg `-0.0439` n `8`; equity avg `0.1411` n `120`; fx avg `-0.009` n `6`; index avg `0.0183` n `25`; metal avg `-0.0504` n `20`; unknown avg `0.0233` n `789`
- 1h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.0517` n `230`; crypto_major avg `0.0429` n `8`; equity avg `0.7721` n `120`; fx avg `-0.0025` n `6`; index avg `0.0639` n `25`; metal avg `0.0065` n `20`; unknown avg `0.0131` n `789`
- 4h: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.0118` n `230`; crypto_major avg `0.0494` n `8`; equity avg `0.7154` n `120`; fx avg `-0.0099` n `6`; index avg `0.1255` n `25`; metal avg `-0.0549` n `20`; unknown avg `-0.0228` n `757`
- 24h: commodity avg `0.3084` n `12`; crypto_alt avg `0.4038` n `230`; crypto_major avg `0.1879` n `8`; equity avg `-2.1779` n `120`; fx avg `-0.1593` n `6`; index avg `-0.2849` n `25`; metal avg `-0.5631` n `20`; unknown avg `-0.2467` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
