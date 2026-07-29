# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T16:07:39.363404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.76` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.2881` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0841` n `12`; crypto_alt avg `-0.1513` n `230`; crypto_major avg `-0.0934` n `8`; equity avg `-0.4706` n `102`; fx avg `0.0061` n `6`; index avg `-0.117` n `25`; metal avg `-0.0463` n `20`; unknown avg `-0.0761` n `778`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.3634` n `230`; crypto_major avg `-0.3245` n `8`; equity avg `-1.0235` n `102`; fx avg `-0.0552` n `6`; index avg `-0.176` n `25`; metal avg `-0.0148` n `20`; unknown avg `-0.0027` n `778`
- 4h: commodity avg `0.608` n `12`; crypto_alt avg `-0.7431` n `230`; crypto_major avg `-0.6747` n `8`; equity avg `-2.9628` n `102`; fx avg `-0.0408` n `6`; index avg `-0.4573` n `25`; metal avg `-0.1904` n `20`; unknown avg `0.3047` n `777`
- 24h: commodity avg `1.4849` n `12`; crypto_alt avg `-2.7927` n `230`; crypto_major avg `-0.6699` n `8`; equity avg `-2.8452` n `102`; fx avg `-0.108` n `6`; index avg `-0.6456` n `25`; metal avg `-0.4007` n `20`; unknown avg `-0.1091` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
