# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T17:52:23.979620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.0768` n `230`; crypto_major avg `-0.0308` n `8`; equity avg `0.0245` n `92`; fx avg `-0.0007` n `6`; index avg `0.002` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0134` n `765`
- 1h: commodity avg `0.0851` n `12`; crypto_alt avg `0.135` n `230`; crypto_major avg `0.2704` n `8`; equity avg `0.1333` n `92`; fx avg `0.0282` n `6`; index avg `0.0084` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.1978` n `765`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `0.2148` n `230`; crypto_major avg `0.4022` n `8`; equity avg `0.1302` n `92`; fx avg `-0.0038` n `6`; index avg `0.0198` n `25`; metal avg `-0.025` n `20`; unknown avg `0.2797` n `765`
- 24h: commodity avg `0.1861` n `12`; crypto_alt avg `0.9583` n `229`; crypto_major avg `0.7568` n `8`; equity avg `0.052` n `92`; fx avg `-0.0101` n `6`; index avg `0.017` n `25`; metal avg `0.0602` n `20`; unknown avg `2.4099` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
