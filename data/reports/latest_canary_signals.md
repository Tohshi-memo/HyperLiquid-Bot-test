# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T12:52:31.811356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0921` n `12`; crypto_alt avg `-0.0525` n `230`; crypto_major avg `-0.01` n `8`; equity avg `-0.0775` n `107`; fx avg `-0.0145` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.0001` n `781`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.0636` n `230`; crypto_major avg `0.0384` n `8`; equity avg `-0.271` n `107`; fx avg `-0.0195` n `6`; index avg `-0.0497` n `25`; metal avg `0.1543` n `20`; unknown avg `-0.1039` n `781`
- 4h: commodity avg `-1.1069` n `12`; crypto_alt avg `-0.0981` n `230`; crypto_major avg `0.5755` n `8`; equity avg `0.6222` n `107`; fx avg `-0.086` n `6`; index avg `0.1264` n `25`; metal avg `0.5583` n `20`; unknown avg `0.1047` n `781`
- 24h: commodity avg `-0.6224` n `12`; crypto_alt avg `0.9549` n `230`; crypto_major avg `1.7538` n `8`; equity avg `4.9952` n `107`; fx avg `0.0341` n `6`; index avg `0.6129` n `25`; metal avg `1.0231` n `20`; unknown avg `0.907` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
