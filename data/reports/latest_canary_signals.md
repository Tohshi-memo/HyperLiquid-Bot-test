# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T23:31:04.098689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0839` n `230`; crypto_major avg `-0.0573` n `8`; equity avg `0.0007` n `114`; fx avg `-0.0001` n `6`; index avg `0.0091` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.0254` n `791`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `0.1119` n `230`; crypto_major avg `0.1046` n `8`; equity avg `0.0159` n `114`; fx avg `0.0093` n `6`; index avg `0.0037` n `25`; metal avg `0.0012` n `20`; unknown avg `0.2081` n `791`
- 4h: commodity avg `-0.1321` n `12`; crypto_alt avg `-0.8755` n `230`; crypto_major avg `-0.7485` n `8`; equity avg `-0.0093` n `114`; fx avg `-0.001` n `6`; index avg `0.014` n `25`; metal avg `-0.011` n `20`; unknown avg `0.8911` n `791`
- 24h: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.6652` n `230`; crypto_major avg `-0.4648` n `8`; equity avg `0.263` n `114`; fx avg `-0.0064` n `6`; index avg `0.0501` n `25`; metal avg `0.0468` n `20`; unknown avg `-0.0068` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
