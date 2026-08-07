# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T14:37:35.808967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0136` n `230`; crypto_major avg `0.1847` n `8`; equity avg `0.1052` n `112`; fx avg `-0.0082` n `6`; index avg `-0.0021` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0228` n `782`
- 1h: commodity avg `0.118` n `12`; crypto_alt avg `-0.1761` n `230`; crypto_major avg `-0.1026` n `8`; equity avg `-0.4561` n `112`; fx avg `0.0149` n `6`; index avg `-0.1242` n `25`; metal avg `-0.126` n `20`; unknown avg `-0.0034` n `782`
- 4h: commodity avg `0.263` n `12`; crypto_alt avg `-0.1523` n `230`; crypto_major avg `0.2471` n `8`; equity avg `-0.0523` n `112`; fx avg `-0.0142` n `6`; index avg `-0.0142` n `25`; metal avg `-0.1521` n `20`; unknown avg `-0.0284` n `782`
- 24h: commodity avg `0.4473` n `12`; crypto_alt avg `-0.0254` n `230`; crypto_major avg `0.3994` n `8`; equity avg `0.4659` n `109`; fx avg `-0.156` n `6`; index avg `-0.1274` n `25`; metal avg `0.2394` n `20`; unknown avg `0.0843` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
