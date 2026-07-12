# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T14:19:21.047809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.0684` n `230`; crypto_major avg `-0.0455` n `8`; equity avg `-0.0053` n `92`; fx avg `0.0` n `6`; index avg `-0.0011` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0033` n `765`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.2286` n `230`; crypto_major avg `-0.141` n `8`; equity avg `-0.0245` n `92`; fx avg `0.0076` n `6`; index avg `0.0211` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.0019` n `765`
- 4h: commodity avg `-0.0573` n `12`; crypto_alt avg `-0.1348` n `230`; crypto_major avg `0.2945` n `8`; equity avg `0.0425` n `92`; fx avg `0.0083` n `6`; index avg `0.008` n `25`; metal avg `-0.021` n `20`; unknown avg `-0.2099` n `763`
- 24h: commodity avg `0.4839` n `12`; crypto_alt avg `-1.3656` n `230`; crypto_major avg `-0.7283` n `8`; equity avg `0.0083` n `92`; fx avg `0.018` n `6`; index avg `-0.1012` n `25`; metal avg `-0.1149` n `20`; unknown avg `0.082` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
