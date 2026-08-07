# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T02:07:29.036189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `-0.0124` n `8`; equity avg `0.3461` n `112`; fx avg `0.0185` n `6`; index avg `0.0556` n `25`; metal avg `0.1098` n `20`; unknown avg `0.0654` n `782`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0209` n `230`; crypto_major avg `-0.04` n `8`; equity avg `0.0231` n `112`; fx avg `-0.0244` n `6`; index avg `-0.0841` n `25`; metal avg `0.1719` n `20`; unknown avg `-0.2142` n `782`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0694` n `230`; crypto_major avg `-0.0351` n `8`; equity avg `-0.0526` n `112`; fx avg `-0.0489` n `6`; index avg `-0.1212` n `25`; metal avg `0.2318` n `20`; unknown avg `0.0682` n `782`
- 24h: commodity avg `0.4714` n `12`; crypto_alt avg `0.7108` n `230`; crypto_major avg `-0.6278` n `8`; equity avg `0.8144` n `109`; fx avg `0.0663` n `6`; index avg `-0.0902` n `25`; metal avg `-0.2491` n `20`; unknown avg `113.1658` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
