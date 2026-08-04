# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T07:52:32.537038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.124` n `8`; equity avg `0.0281` n `107`; fx avg `0.0204` n `6`; index avg `0.0158` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0847` n `781`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `0.2283` n `230`; crypto_major avg `0.325` n `8`; equity avg `0.1792` n `107`; fx avg `-0.0055` n `6`; index avg `0.033` n `25`; metal avg `0.1014` n `20`; unknown avg `0.5483` n `781`
- 4h: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.1509` n `230`; crypto_major avg `0.0421` n `8`; equity avg `0.8444` n `107`; fx avg `0.0712` n `6`; index avg `0.1623` n `25`; metal avg `0.1507` n `20`; unknown avg `0.4754` n `765`
- 24h: commodity avg `0.3035` n `12`; crypto_alt avg `1.3717` n `230`; crypto_major avg `1.6443` n `8`; equity avg `2.9625` n `107`; fx avg `0.1005` n `6`; index avg `0.2871` n `25`; metal avg `0.1225` n `20`; unknown avg `0.7381` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
