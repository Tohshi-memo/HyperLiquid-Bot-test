# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T01:22:25.909949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.0581` n `231`; crypto_major avg `-0.0701` n `8`; equity avg `0.0111` n `122`; fx avg `0.01` n `6`; index avg `0.0061` n `25`; metal avg `0.0486` n `20`; unknown avg `-0.0668` n `796`
- 1h: commodity avg `-0.063` n `12`; crypto_alt avg `0.8274` n `231`; crypto_major avg `0.6027` n `8`; equity avg `-0.3635` n `122`; fx avg `0.0031` n `6`; index avg `-0.0637` n `25`; metal avg `0.0336` n `20`; unknown avg `0.1526` n `796`
- 4h: commodity avg `-0.1156` n `12`; crypto_alt avg `1.3135` n `231`; crypto_major avg `0.9653` n `8`; equity avg `-0.3866` n `122`; fx avg `0.029` n `6`; index avg `-0.1294` n `25`; metal avg `0.06` n `20`; unknown avg `0.2488` n `795`
- 24h: commodity avg `-0.8247` n `12`; crypto_alt avg `-2.2265` n `231`; crypto_major avg `-2.1159` n `8`; equity avg `1.6318` n `122`; fx avg `0.059` n `6`; index avg `0.1986` n `25`; metal avg `-0.1647` n `20`; unknown avg `-0.4074` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
