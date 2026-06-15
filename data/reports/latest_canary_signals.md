# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T15:07:37.894837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2258` n `12`; crypto_alt avg `0.0769` n `228`; crypto_major avg `0.0492` n `8`; equity avg `0.0777` n `74`; fx avg `0.0101` n `6`; index avg `0.152` n `23`; metal avg `-0.0505` n `18`; unknown avg `0.4359` n `690`
- 1h: commodity avg `0.2999` n `12`; crypto_alt avg `0.2495` n `228`; crypto_major avg `0.3945` n `8`; equity avg `0.3886` n `74`; fx avg `-0.0186` n `6`; index avg `0.0248` n `23`; metal avg `-0.414` n `18`; unknown avg `0.8593` n `690`
- 4h: commodity avg `0.6588` n `12`; crypto_alt avg `1.2542` n `228`; crypto_major avg `1.5669` n `8`; equity avg `0.7601` n `74`; fx avg `-0.0068` n `6`; index avg `0.2675` n `23`; metal avg `0.1716` n `18`; unknown avg `1.2681` n `689`
- 24h: commodity avg `-0.8492` n `12`; crypto_alt avg `6.3464` n `228`; crypto_major avg `6.5311` n `8`; equity avg `2.4768` n `74`; fx avg `0.0765` n `6`; index avg `1.1895` n `23`; metal avg `2.7589` n `18`; unknown avg `2.3637` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
