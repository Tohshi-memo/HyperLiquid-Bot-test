# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T13:54:59.605819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.0383` n `229`; crypto_major avg `-0.0757` n `8`; equity avg `-0.0088` n `88`; fx avg `-0.0055` n `6`; index avg `0.0044` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.047` n `765`
- 1h: commodity avg `-0.0718` n `12`; crypto_alt avg `-0.1468` n `229`; crypto_major avg `-0.0208` n `8`; equity avg `-0.0473` n `88`; fx avg `-0.0081` n `6`; index avg `0.0127` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0148` n `759`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.6543` n `229`; crypto_major avg `0.0838` n `8`; equity avg `-0.1054` n `88`; fx avg `-0.0098` n `6`; index avg `0.0042` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.1064` n `759`
- 24h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.4581` n `229`; crypto_major avg `0.9294` n `8`; equity avg `0.2035` n `88`; fx avg `-0.0666` n `6`; index avg `-0.0751` n `25`; metal avg `0.0403` n `20`; unknown avg `2.3704` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
