# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T02:22:29.803182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1001` n `12`; crypto_alt avg `-0.0043` n `230`; crypto_major avg `-0.0238` n `8`; equity avg `-0.1132` n `108`; fx avg `-0.0179` n `6`; index avg `-0.0212` n `25`; metal avg `0.0437` n `20`; unknown avg `0.0033` n `781`
- 1h: commodity avg `-0.2088` n `12`; crypto_alt avg `0.2497` n `230`; crypto_major avg `0.4625` n `8`; equity avg `0.4671` n `108`; fx avg `-0.0401` n `6`; index avg `0.0516` n `25`; metal avg `0.1713` n `20`; unknown avg `0.2244` n `781`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.2543` n `230`; crypto_major avg `0.3076` n `8`; equity avg `0.5241` n `108`; fx avg `-0.0905` n `6`; index avg `0.059` n `25`; metal avg `0.1072` n `20`; unknown avg `-0.0843` n `781`
- 24h: commodity avg `-1.438` n `12`; crypto_alt avg `0.2458` n `230`; crypto_major avg `0.77` n `8`; equity avg `3.9406` n `107`; fx avg `0.0453` n `6`; index avg `0.8212` n `25`; metal avg `0.8949` n `20`; unknown avg `0.394` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
