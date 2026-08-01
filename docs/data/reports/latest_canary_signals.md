# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T09:30:30.935486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-0.0901` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `0.0054` n `102`; fx avg `-0.0058` n `6`; index avg `0.01` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0039` n `781`
- 1h: commodity avg `-0.0361` n `12`; crypto_alt avg `-0.1257` n `230`; crypto_major avg `-0.0637` n `8`; equity avg `-0.0659` n `102`; fx avg `-0.0063` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.012` n `781`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `-0.3762` n `230`; crypto_major avg `-0.2087` n `8`; equity avg `0.0931` n `102`; fx avg `0.0023` n `6`; index avg `0.0227` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0098` n `765`
- 24h: commodity avg `0.6057` n `12`; crypto_alt avg `0.3486` n `230`; crypto_major avg `-1.0488` n `8`; equity avg `-2.5311` n `102`; fx avg `-0.0288` n `6`; index avg `-0.2864` n `25`; metal avg `0.0104` n `20`; unknown avg `4.8429` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.104`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0685`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `669`, weak_sample_signal
