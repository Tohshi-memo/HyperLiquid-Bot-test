# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T08:37:33.558207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.054` n `12`; crypto_alt avg `0.0269` n `233`; crypto_major avg `-0.0053` n `8`; equity avg `-0.0325` n `134`; fx avg `0.0126` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0487` n `20`; unknown avg `0.0092` n `791`
- 1h: commodity avg `0.084` n `12`; crypto_alt avg `0.1249` n `233`; crypto_major avg `0.2929` n `8`; equity avg `-0.1015` n `134`; fx avg `0.0407` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0503` n `20`; unknown avg `1.3573` n `789`
- 4h: commodity avg `0.1105` n `12`; crypto_alt avg `-0.5442` n `233`; crypto_major avg `-0.5102` n `8`; equity avg `-0.1747` n `134`; fx avg `0.0823` n `6`; index avg `0.0025` n `26`; metal avg `-0.1434` n `20`; unknown avg `0.3943` n `765`
- 24h: commodity avg `-0.0035` n `12`; crypto_alt avg `-4.7592` n `233`; crypto_major avg `-3.2355` n `8`; equity avg `-1.4699` n `134`; fx avg `0.0785` n `6`; index avg `-0.1521` n `26`; metal avg `0.0886` n `20`; unknown avg `0.3387` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
