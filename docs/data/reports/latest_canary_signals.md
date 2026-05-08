# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T16:52:20.069410+00:00`
- Correlation status: `ready`
- Asset price records: `663`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.0504` n `228`; crypto_major avg `-0.0439` n `8`; equity avg `0.0144` n `65`; fx avg `0.0082` n `5`; index avg `0.0425` n `23`; metal avg `-0.0412` n `18`; unknown avg `-0.0897` n `375`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.3675` n `228`; crypto_major avg `-0.0909` n `8`; equity avg `0.0014` n `65`; fx avg `-0.0054` n `5`; index avg `0.1182` n `23`; metal avg `0.1084` n `18`; unknown avg `-0.1162` n `375`
- 4h: commodity avg `0.4642` n `12`; crypto_alt avg `1.2031` n `228`; crypto_major avg `0.4092` n `8`; equity avg `0.771` n `65`; fx avg `-0.0222` n `5`; index avg `0.3359` n `23`; metal avg `-0.5713` n `18`; unknown avg `0.212` n `375`
- 24h: commodity avg `0.4285` n `12`; crypto_alt avg `2.7184` n `228`; crypto_major avg `0.2925` n `8`; equity avg `2.0212` n `65`; fx avg `0.1349` n `5`; index avg `1.0431` n `23`; metal avg `0.1215` n `18`; unknown avg `0.0027` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `655`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `655`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `659`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `655`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `659`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0967`, n `655`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `659`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `659`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `659`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `659`, weak_sample_signal
