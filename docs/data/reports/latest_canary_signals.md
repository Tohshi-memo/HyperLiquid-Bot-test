# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T02:07:25.372766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0143` n `230`; crypto_major avg `-0.026` n `8`; equity avg `-0.047` n `114`; fx avg `0.017` n `6`; index avg `0.009` n `25`; metal avg `-0.0318` n `20`; unknown avg `0.1073` n `793`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `-0.3749` n `230`; crypto_major avg `-0.2811` n `8`; equity avg `-0.9348` n `114`; fx avg `0.0118` n `6`; index avg `-0.1136` n `25`; metal avg `-0.2742` n `20`; unknown avg `0.4322` n `793`
- 4h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.5447` n `230`; crypto_major avg `-0.1704` n `8`; equity avg `-0.9724` n `114`; fx avg `-0.0672` n `6`; index avg `-0.1377` n `25`; metal avg `-0.1501` n `20`; unknown avg `-0.1229` n `792`
- 24h: commodity avg `0.5178` n `12`; crypto_alt avg `-0.2642` n `230`; crypto_major avg `0.6185` n `8`; equity avg `0.1474` n `114`; fx avg `0.0152` n `6`; index avg `-0.0676` n `25`; metal avg `-0.1467` n `20`; unknown avg `0.2466` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
