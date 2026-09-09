# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T01:07:26.115652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.0854` n `233`; crypto_major avg `-0.072` n `8`; equity avg `0.1495` n `134`; fx avg `0.0067` n `6`; index avg `0.0195` n `26`; metal avg `0.0304` n `20`; unknown avg `0.0901` n `795`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.3914` n `233`; crypto_major avg `0.0248` n `8`; equity avg `0.2323` n `134`; fx avg `0.0621` n `6`; index avg `0.0403` n `26`; metal avg `0.1175` n `20`; unknown avg `0.0711` n `789`
- 4h: commodity avg `0.0278` n `12`; crypto_alt avg `-0.0695` n `233`; crypto_major avg `0.448` n `8`; equity avg `0.3702` n `134`; fx avg `-0.0209` n `6`; index avg `0.09` n `26`; metal avg `0.0799` n `20`; unknown avg `0.7767` n `741`
- 24h: commodity avg `0.1484` n `12`; crypto_alt avg `-0.8565` n `232`; crypto_major avg `0.2333` n `8`; equity avg `0.4534` n `134`; fx avg `-0.0062` n `6`; index avg `-0.112` n `26`; metal avg `-0.3197` n `20`; unknown avg `0.7644` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
