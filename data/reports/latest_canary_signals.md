# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T15:06:14.673781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1219` n `12`; crypto_alt avg `0.0506` n `230`; crypto_major avg `-0.0131` n `8`; equity avg `0.3068` n `112`; fx avg `0.0003` n `6`; index avg `0.0408` n `25`; metal avg `0.0345` n `20`; unknown avg `0.0263` n `782`
- 1h: commodity avg `0.0905` n `12`; crypto_alt avg `-0.248` n `230`; crypto_major avg `-0.0769` n `8`; equity avg `0.3316` n `112`; fx avg `0.0082` n `6`; index avg `0.0195` n `25`; metal avg `0.0872` n `20`; unknown avg `-0.0709` n `782`
- 4h: commodity avg `0.434` n `12`; crypto_alt avg `-0.4059` n `230`; crypto_major avg `-0.2433` n `8`; equity avg `-0.0558` n `112`; fx avg `-0.0122` n `6`; index avg `0.0003` n `25`; metal avg `-0.1499` n `20`; unknown avg `0.0579` n `782`
- 24h: commodity avg `0.5537` n `12`; crypto_alt avg `-0.54` n `230`; crypto_major avg `-0.2266` n `8`; equity avg `0.1216` n `112`; fx avg `-0.1228` n `6`; index avg `-0.1181` n `25`; metal avg `0.2552` n `20`; unknown avg `0.0155` n `765`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
