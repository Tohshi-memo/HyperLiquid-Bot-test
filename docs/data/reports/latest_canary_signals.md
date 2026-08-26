# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T23:07:27.090721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0311` n `231`; crypto_major avg `0.027` n `8`; equity avg `-0.0589` n `124`; fx avg `0.0002` n `6`; index avg `-0.0125` n `25`; metal avg `0.0125` n `20`; unknown avg `0.1155` n `795`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `0.1961` n `231`; crypto_major avg `-0.032` n `8`; equity avg `0.09` n `124`; fx avg `-0.0049` n `6`; index avg `0.0225` n `25`; metal avg `0.0584` n `20`; unknown avg `0.0971` n `795`
- 4h: commodity avg `0.0113` n `12`; crypto_alt avg `1.569` n `231`; crypto_major avg `1.2292` n `8`; equity avg `1.5721` n `124`; fx avg `-0.0196` n `6`; index avg `0.2642` n `25`; metal avg `0.1396` n `20`; unknown avg `0.4623` n `795`
- 24h: commodity avg `0.32` n `12`; crypto_alt avg `0.8293` n `231`; crypto_major avg `0.4133` n `8`; equity avg `1.3727` n `124`; fx avg `-0.0744` n `6`; index avg `0.2983` n `25`; metal avg `-0.311` n `20`; unknown avg `0.925` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
