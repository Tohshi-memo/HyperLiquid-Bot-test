# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T05:22:28.397969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0764` n `230`; crypto_major avg `-0.0451` n `8`; equity avg `0.0193` n `107`; fx avg `-0.0022` n `6`; index avg `0.0052` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0437` n `781`
- 1h: commodity avg `0.0529` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `0.0008` n `8`; equity avg `-0.0245` n `107`; fx avg `-0.0265` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0122` n `20`; unknown avg `7.037` n `781`
- 4h: commodity avg `0.1447` n `12`; crypto_alt avg `0.3489` n `230`; crypto_major avg `0.4976` n `8`; equity avg `0.4392` n `107`; fx avg `0.0591` n `6`; index avg `0.0856` n `25`; metal avg `0.2094` n `20`; unknown avg `4.8589` n `780`
- 24h: commodity avg `0.415` n `12`; crypto_alt avg `1.1741` n `230`; crypto_major avg `1.2901` n `8`; equity avg `1.7467` n `107`; fx avg `0.0179` n `6`; index avg `0.1288` n `25`; metal avg `0.0435` n `20`; unknown avg `0.1606` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
