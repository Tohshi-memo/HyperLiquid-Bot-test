# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T11:52:13.449476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0825` n `12`; crypto_alt avg `-0.1039` n `228`; crypto_major avg `-0.0566` n `8`; equity avg `-0.0703` n `67`; fx avg `-0.0119` n `6`; index avg `0.0351` n `23`; metal avg `-0.0014` n `18`; unknown avg `0.1341` n `396`
- 1h: commodity avg `0.1427` n `12`; crypto_alt avg `-0.1853` n `228`; crypto_major avg `-0.0503` n `8`; equity avg `-0.0754` n `67`; fx avg `-0.0082` n `6`; index avg `0.1206` n `23`; metal avg `0.014` n `18`; unknown avg `0.7295` n `396`
- 4h: commodity avg `0.1153` n `12`; crypto_alt avg `0.3831` n `228`; crypto_major avg `0.3619` n `8`; equity avg `-0.087` n `67`; fx avg `-0.0275` n `6`; index avg `0.0583` n `23`; metal avg `-0.0338` n `18`; unknown avg `1.3185` n `386`
- 24h: commodity avg `-0.0044` n `12`; crypto_alt avg `-6.0196` n `228`; crypto_major avg `-4.2432` n `8`; equity avg `-1.7259` n `67`; fx avg `0.0532` n `6`; index avg `-0.0959` n `23`; metal avg `-0.8621` n `18`; unknown avg `-1.4164` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
