# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T06:22:27.860207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0497` n `12`; crypto_alt avg `-0.0754` n `228`; crypto_major avg `0.0265` n `8`; equity avg `0.0143` n `74`; fx avg `-0.0215` n `6`; index avg `0.0646` n `23`; metal avg `-0.0124` n `18`; unknown avg `-0.039` n `643`
- 1h: commodity avg `-0.1111` n `12`; crypto_alt avg `-0.0054` n `228`; crypto_major avg `0.1914` n `8`; equity avg `-0.0372` n `74`; fx avg `-0.0233` n `6`; index avg `0.0066` n `23`; metal avg `-0.0018` n `18`; unknown avg `-0.0715` n `627`
- 4h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.4804` n `228`; crypto_major avg `-0.6415` n `8`; equity avg `-0.4652` n `74`; fx avg `0.0088` n `6`; index avg `-0.0177` n `23`; metal avg `-0.0841` n `18`; unknown avg `-0.56` n `619`
- 24h: commodity avg `-0.7851` n `12`; crypto_alt avg `0.5848` n `228`; crypto_major avg `0.2599` n `8`; equity avg `-0.3173` n `74`; fx avg `0.018` n `6`; index avg `0.9263` n `23`; metal avg `0.5864` n `18`; unknown avg `36.4039` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
