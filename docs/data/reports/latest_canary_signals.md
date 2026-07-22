# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T01:22:23.608375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `11`; crypto_alt avg `-0.0944` n `230`; crypto_major avg `-0.1319` n `8`; equity avg `0.2486` n `87`; fx avg `0.0003` n `5`; index avg `0.0348` n `19`; metal avg `0.0054` n `16`; unknown avg `-0.0427` n `754`
- 1h: commodity avg `0.1657` n `11`; crypto_alt avg `-0.2208` n `230`; crypto_major avg `-0.2781` n `8`; equity avg `-0.1375` n `87`; fx avg `0.0123` n `5`; index avg `-0.0335` n `19`; metal avg `0.2948` n `16`; unknown avg `-0.1153` n `754`
- 4h: commodity avg `0.165` n `11`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `0.0784` n `8`; equity avg `0.1887` n `87`; fx avg `0.01` n `5`; index avg `0.037` n `19`; metal avg `0.4329` n `16`; unknown avg `-0.2753` n `754`
- 24h: commodity avg `0.7598` n `11`; crypto_alt avg `0.6651` n `230`; crypto_major avg `0.574` n `8`; equity avg `4.4838` n `87`; fx avg `0.014` n `5`; index avg `0.7584` n `19`; metal avg `1.1825` n `16`; unknown avg `0.3678` n `738`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0963`, n `664`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0583`, n `664`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0511`, n `666`, weak_sample_signal
