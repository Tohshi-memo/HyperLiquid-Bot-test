# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T18:37:24.920699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `-0.0364` n `228`; crypto_major avg `0.0406` n `8`; equity avg `-0.0406` n `66`; fx avg `-0.0308` n `6`; index avg `0.0393` n `23`; metal avg `-0.0277` n `18`; unknown avg `0.2359` n `383`
- 1h: commodity avg `0.3562` n `12`; crypto_alt avg `-0.6355` n `228`; crypto_major avg `-0.4129` n `8`; equity avg `-0.5135` n `66`; fx avg `-0.0787` n `6`; index avg `-0.1956` n `23`; metal avg `-0.3083` n `18`; unknown avg `-0.0346` n `383`
- 4h: commodity avg `0.9801` n `12`; crypto_alt avg `-0.4794` n `228`; crypto_major avg `-0.3592` n `8`; equity avg `-0.8224` n `66`; fx avg `0.0816` n `6`; index avg `-0.4609` n `23`; metal avg `0.0114` n `18`; unknown avg `-0.4453` n `383`
- 24h: commodity avg `1.421` n `12`; crypto_alt avg `-2.7017` n `228`; crypto_major avg `-2.3253` n `8`; equity avg `-1.4661` n `66`; fx avg `0.1358` n `6`; index avg `-0.7273` n `23`; metal avg `0.3658` n `18`; unknown avg `-0.4998` n `362`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
