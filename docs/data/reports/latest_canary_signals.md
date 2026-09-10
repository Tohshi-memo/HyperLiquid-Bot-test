# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T05:37:29.368648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0872` n `12`; crypto_alt avg `0.2187` n `233`; crypto_major avg `0.1682` n `8`; equity avg `0.1422` n `134`; fx avg `0.0081` n `6`; index avg `0.0315` n `26`; metal avg `0.052` n `20`; unknown avg `0.2156` n `797`
- 1h: commodity avg `-0.0858` n `12`; crypto_alt avg `0.2105` n `233`; crypto_major avg `0.0267` n `8`; equity avg `0.2155` n `134`; fx avg `0.0163` n `6`; index avg `0.0592` n `26`; metal avg `0.0956` n `20`; unknown avg `1.4188` n `795`
- 4h: commodity avg `-0.2166` n `12`; crypto_alt avg `1.0222` n `233`; crypto_major avg `0.8256` n `8`; equity avg `0.6735` n `134`; fx avg `-0.021` n `6`; index avg `0.1906` n `26`; metal avg `0.1476` n `20`; unknown avg `0.5054` n `789`
- 24h: commodity avg `-0.0163` n `12`; crypto_alt avg `-3.2208` n `233`; crypto_major avg `-2.1234` n `8`; equity avg `-0.7519` n `134`; fx avg `0.0542` n `6`; index avg `-0.082` n `26`; metal avg `0.4314` n `20`; unknown avg `0.5805` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
