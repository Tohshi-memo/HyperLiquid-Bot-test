# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T13:14:07.148219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.159` n `8`; equity avg `-0.1522` n `114`; fx avg `-0.0054` n `6`; index avg `-0.015` n `25`; metal avg `-0.0845` n `20`; unknown avg `0.016` n `795`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0152` n `230`; crypto_major avg `-0.3211` n `8`; equity avg `-0.4554` n `114`; fx avg `0.0034` n `6`; index avg `-0.0408` n `25`; metal avg `-0.0421` n `20`; unknown avg `0.066` n `795`
- 4h: commodity avg `0.0468` n `12`; crypto_alt avg `0.1956` n `230`; crypto_major avg `-0.1316` n `8`; equity avg `-0.2778` n `114`; fx avg `-0.0288` n `6`; index avg `0.0061` n `25`; metal avg `0.0109` n `20`; unknown avg `0.0839` n `795`
- 24h: commodity avg `0.6079` n `12`; crypto_alt avg `-0.6417` n `230`; crypto_major avg `0.0982` n `8`; equity avg `-2.5348` n `114`; fx avg `-0.0588` n `6`; index avg `-0.5044` n `25`; metal avg `-0.212` n `20`; unknown avg `-0.0829` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
