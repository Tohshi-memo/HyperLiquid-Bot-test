# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T02:03:23.227464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.0582` n `228`; crypto_major avg `-0.0523` n `8`; equity avg `-0.237` n `86`; fx avg `0.0047` n `6`; index avg `-0.0332` n `23`; metal avg `0.118` n `20`; unknown avg `-0.295` n `765`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.3447` n `228`; crypto_major avg `-0.2362` n `8`; equity avg `-0.3675` n `86`; fx avg `-0.0164` n `6`; index avg `-0.0928` n `23`; metal avg `-0.0495` n `20`; unknown avg `8.6301` n `765`
- 4h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.5844` n `228`; crypto_major avg `-0.5797` n `8`; equity avg `-1.0101` n `86`; fx avg `0.0334` n `6`; index avg `-0.2182` n `23`; metal avg `-0.1498` n `20`; unknown avg `-0.6188` n `749`
- 24h: commodity avg `0.4647` n `12`; crypto_alt avg `-1.843` n `228`; crypto_major avg `-1.9771` n `8`; equity avg `-3.1068` n `86`; fx avg `0.0326` n `6`; index avg `-0.4133` n `23`; metal avg `0.4818` n `20`; unknown avg `0.434` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
