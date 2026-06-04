# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T12:22:25.472904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.175` n `12`; crypto_alt avg `0.4387` n `228`; crypto_major avg `0.4832` n `8`; equity avg `-0.0122` n `73`; fx avg `0.0054` n `6`; index avg `0.0178` n `23`; metal avg `0.1611` n `18`; unknown avg `0.266` n `424`
- 1h: commodity avg `-0.2504` n `12`; crypto_alt avg `0.7466` n `228`; crypto_major avg `0.9159` n `8`; equity avg `0.2081` n `73`; fx avg `0.0072` n `6`; index avg `-0.041` n `23`; metal avg `0.4765` n `18`; unknown avg `0.0587` n `424`
- 4h: commodity avg `-0.5079` n `12`; crypto_alt avg `-1.0129` n `228`; crypto_major avg `-0.5237` n `8`; equity avg `-0.5941` n `73`; fx avg `0.0165` n `6`; index avg `-0.3153` n `23`; metal avg `0.9421` n `18`; unknown avg `-0.7366` n `424`
- 24h: commodity avg `-1.0546` n `12`; crypto_alt avg `-7.4422` n `228`; crypto_major avg `-5.9464` n `8`; equity avg `-4.685` n `73`; fx avg `0.1301` n `6`; index avg `-1.6054` n `23`; metal avg `-0.2206` n `18`; unknown avg `-1.2037` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
