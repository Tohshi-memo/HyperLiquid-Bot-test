# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T00:22:23.934720+00:00`
- Correlation status: `ready`
- Asset price records: `501`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0465` n `12`; crypto_alt avg `-0.1173` n `228`; crypto_major avg `-0.1444` n `8`; equity avg `-0.1388` n `65`; fx avg `-0.023` n `4`; index avg `-0.0518` n `23`; metal avg `0.0918` n `18`; unknown avg `-0.0253` n `356`
- 1h: commodity avg `0.096` n `12`; crypto_alt avg `0.0882` n `228`; crypto_major avg `-0.0519` n `8`; equity avg `-0.2644` n `65`; fx avg `0.0191` n `4`; index avg `-0.0051` n `23`; metal avg `0.072` n `18`; unknown avg `-0.0139` n `356`
- 4h: commodity avg `0.1986` n `12`; crypto_alt avg `-0.1249` n `228`; crypto_major avg `-0.3978` n `8`; equity avg `-0.6635` n `65`; fx avg `0.0408` n `4`; index avg `-0.1904` n `23`; metal avg `-0.0321` n `18`; unknown avg `-0.0419` n `356`
- 24h: commodity avg `-1.7605` n `7`; crypto_alt avg `1.9576` n `223`; crypto_major avg `0.1355` n `7`; equity avg `1.5116` n `47`; fx avg `-0.3644` n `4`; index avg `1.433` n `6`; metal avg `2.9257` n `7`; unknown avg `3.4377` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `497`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `497`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `493`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0848`, n `493`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `493`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.078`, n `493`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0761`, n `493`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `497`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `493`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0568`, n `497`, weak_sample_signal
