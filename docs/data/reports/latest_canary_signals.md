# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T21:13:55.159231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `0.0372` n `8`; equity avg `0.0665` n `114`; fx avg `-0.0089` n `6`; index avg `0.0177` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0152` n `792`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.1335` n `230`; crypto_major avg `0.1379` n `8`; equity avg `0.0744` n `114`; fx avg `0.0005` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0552` n `792`
- 4h: commodity avg `0.3056` n `12`; crypto_alt avg `-0.0568` n `230`; crypto_major avg `-0.0321` n `8`; equity avg `-0.5593` n `114`; fx avg `-0.0015` n `6`; index avg `-0.1123` n `25`; metal avg `-0.0921` n `20`; unknown avg `0.0447` n `792`
- 24h: commodity avg `0.395` n `12`; crypto_alt avg `0.2447` n `230`; crypto_major avg `0.9991` n `8`; equity avg `1.0549` n `114`; fx avg `0.0132` n `6`; index avg `0.0593` n `25`; metal avg `0.1983` n `20`; unknown avg `0.2377` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
