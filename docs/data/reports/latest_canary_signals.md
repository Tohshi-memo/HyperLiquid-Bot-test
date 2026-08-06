# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T02:07:33.899449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.1049` n `230`; crypto_major avg `-0.1817` n `8`; equity avg `0.1327` n `108`; fx avg `-0.0247` n `6`; index avg `0.0195` n `25`; metal avg `0.1053` n `20`; unknown avg `-0.007` n `782`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.4245` n `230`; crypto_major avg `-0.3749` n `8`; equity avg `0.1245` n `108`; fx avg `-0.0269` n `6`; index avg `-0.0226` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.098` n `782`
- 4h: commodity avg `0.1137` n `12`; crypto_alt avg `-0.1532` n `230`; crypto_major avg `-0.4397` n `8`; equity avg `-0.3853` n `108`; fx avg `-0.08` n `6`; index avg `-0.1834` n `25`; metal avg `0.369` n `20`; unknown avg `-0.0428` n `782`
- 24h: commodity avg `0.0016` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `-0.1881` n `8`; equity avg `-1.9018` n `108`; fx avg `-0.0546` n `6`; index avg `-0.3884` n `25`; metal avg `1.0811` n `20`; unknown avg `0.9593` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
