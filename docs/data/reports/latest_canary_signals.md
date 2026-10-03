# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T11:22:25.010311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0563` n `13`; crypto_alt avg `-0.137` n `235`; crypto_major avg `-0.0769` n `8`; equity avg `-0.0189` n `143`; fx avg `-0.0036` n `6`; index avg `-0.0177` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0492` n `984`
- 1h: commodity avg `-0.0489` n `13`; crypto_alt avg `-0.1132` n `235`; crypto_major avg `-0.0242` n `8`; equity avg `-0.0154` n `143`; fx avg `-0.0059` n `6`; index avg `-0.0057` n `26`; metal avg `0.0071` n `20`; unknown avg `-0.0597` n `982`
- 4h: commodity avg `-0.0285` n `13`; crypto_alt avg `0.2745` n `235`; crypto_major avg `0.0017` n `8`; equity avg `-0.0023` n `143`; fx avg `-0.0154` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0077` n `20`; unknown avg `1.2895` n `966`
- 24h: commodity avg `0.6826` n `13`; crypto_alt avg `-1.9744` n `235`; crypto_major avg `-2.5094` n `8`; equity avg `0.2099` n `142`; fx avg `0.0036` n `6`; index avg `0.1043` n `26`; metal avg `-0.3028` n `20`; unknown avg `-0.3324` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
