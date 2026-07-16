# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T15:11:17.806162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `-0.3447` n `230`; crypto_major avg `-0.403` n `8`; equity avg `-0.1585` n `94`; fx avg `-0.0039` n `6`; index avg `-0.0176` n `25`; metal avg `-0.0367` n `20`; unknown avg `-0.0542` n `768`
- 1h: commodity avg `-0.2817` n `12`; crypto_alt avg `-0.2163` n `230`; crypto_major avg `-0.2625` n `8`; equity avg `-0.641` n `94`; fx avg `-0.0421` n `6`; index avg `-0.041` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.074` n `768`
- 4h: commodity avg `-0.1333` n `12`; crypto_alt avg `0.2891` n `230`; crypto_major avg `0.0693` n `8`; equity avg `-1.3392` n `94`; fx avg `0.0147` n `6`; index avg `-0.0781` n `25`; metal avg `-0.249` n `20`; unknown avg `0.1082` n `768`
- 24h: commodity avg `0.0152` n `12`; crypto_alt avg `-1.1016` n `230`; crypto_major avg `-1.9337` n `8`; equity avg `-2.9349` n `94`; fx avg `-0.0777` n `6`; index avg `-0.2562` n `25`; metal avg `-0.4219` n `20`; unknown avg `-0.3176` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
