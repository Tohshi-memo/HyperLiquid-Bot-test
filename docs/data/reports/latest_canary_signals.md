# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T02:07:25.676033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.1115` n `228`; crypto_major avg `-0.1259` n `8`; equity avg `-0.2481` n `86`; fx avg `0.0072` n `6`; index avg `-0.0399` n `23`; metal avg `0.0046` n `20`; unknown avg `-0.2929` n `765`
- 1h: commodity avg `-0.0526` n `12`; crypto_alt avg `-0.3979` n `228`; crypto_major avg `-0.3095` n `8`; equity avg `-0.3786` n `86`; fx avg `-0.0139` n `6`; index avg `-0.0995` n `23`; metal avg `-0.1622` n `20`; unknown avg `7.7217` n `765`
- 4h: commodity avg `-0.0583` n `12`; crypto_alt avg `-0.6378` n `228`; crypto_major avg `-0.6529` n `8`; equity avg `-1.0203` n `86`; fx avg `0.0359` n `6`; index avg `-0.2248` n `23`; metal avg `-0.2622` n `20`; unknown avg `-0.6136` n `749`
- 24h: commodity avg `0.4593` n `12`; crypto_alt avg `-1.8946` n `228`; crypto_major avg `-2.0484` n `8`; equity avg `-3.1179` n `86`; fx avg `0.0351` n `6`; index avg `-0.4197` n `23`; metal avg `0.3675` n `20`; unknown avg `0.4227` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
