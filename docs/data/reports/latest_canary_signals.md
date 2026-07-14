# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T22:22:27.056598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `0.2764` n `230`; crypto_major avg `0.3215` n `8`; equity avg `0.0408` n `92`; fx avg `0.0051` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.1538` n `768`
- 1h: commodity avg `0.0432` n `12`; crypto_alt avg `0.2205` n `230`; crypto_major avg `0.1173` n `8`; equity avg `0.0117` n `92`; fx avg `0.0086` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0134` n `20`; unknown avg `2.2117` n `768`
- 4h: commodity avg `0.1808` n `12`; crypto_alt avg `0.3054` n `230`; crypto_major avg `0.5013` n `8`; equity avg `0.0446` n `92`; fx avg `0.0085` n `6`; index avg `-0.047` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.1883` n `768`
- 24h: commodity avg `0.3377` n `12`; crypto_alt avg `2.3708` n `230`; crypto_major avg `3.7349` n `8`; equity avg `1.3674` n `92`; fx avg `-0.0029` n `6`; index avg `0.3859` n `25`; metal avg `0.5413` n `20`; unknown avg `0.2477` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
