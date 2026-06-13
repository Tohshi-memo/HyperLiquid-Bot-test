# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T05:52:34.273506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1124` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.1538` n `228`; crypto_major avg `-0.0988` n `8`; equity avg `-0.0829` n `74`; fx avg `-0.0007` n `6`; index avg `-0.0113` n `23`; metal avg `0.0097` n `18`; unknown avg `2.5383` n `643`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.5743` n `228`; crypto_major avg `-0.4189` n `8`; equity avg `-0.1434` n `74`; fx avg `0.0201` n `6`; index avg `0.0613` n `23`; metal avg `-0.0105` n `18`; unknown avg `0.3173` n `643`
- 4h: commodity avg `-0.1671` n `12`; crypto_alt avg `-0.9489` n `228`; crypto_major avg `-0.9884` n `8`; equity avg `-0.371` n `74`; fx avg `0.029` n `6`; index avg `0.124` n `23`; metal avg `-0.097` n `18`; unknown avg `0.9605` n `635`
- 24h: commodity avg `-0.4626` n `12`; crypto_alt avg `0.0211` n `228`; crypto_major avg `-0.3821` n `8`; equity avg `-0.4559` n `74`; fx avg `0.0425` n `6`; index avg `0.9711` n `23`; metal avg `0.7509` n `18`; unknown avg `40.5745` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
