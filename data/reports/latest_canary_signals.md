# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T19:52:31.931953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `1.3578` n `228`; crypto_major avg `0.8523` n `8`; equity avg `0.218` n `69`; fx avg `-0.0004` n `6`; index avg `0.1698` n `23`; metal avg `0.0791` n `18`; unknown avg `0.5164` n `422`
- 1h: commodity avg `-0.0333` n `12`; crypto_alt avg `0.1415` n `228`; crypto_major avg `0.0789` n `8`; equity avg `0.1711` n `69`; fx avg `0.0196` n `6`; index avg `0.1963` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.0382` n `422`
- 4h: commodity avg `0.3238` n `12`; crypto_alt avg `0.8208` n `228`; crypto_major avg `-0.1314` n `8`; equity avg `0.1389` n `69`; fx avg `-0.0207` n `6`; index avg `0.0824` n `23`; metal avg `-0.5024` n `18`; unknown avg `0.4898` n `422`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `-4.101` n `228`; crypto_major avg `-4.6754` n `8`; equity avg `0.6553` n `69`; fx avg `0.088` n `6`; index avg `0.5435` n `23`; metal avg `0.3788` n `18`; unknown avg `-0.5012` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
