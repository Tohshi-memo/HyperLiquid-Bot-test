# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T03:22:27.169722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `13`; crypto_alt avg `0.0992` n `236`; crypto_major avg `0.1223` n `8`; equity avg `0.0035` n `151`; fx avg `0.0005` n `6`; index avg `-0.0025` n `26`; metal avg `0.004` n `20`; unknown avg `0.0193` n `1193`
- 1h: commodity avg `0.0109` n `13`; crypto_alt avg `-0.1182` n `236`; crypto_major avg `0.06` n `8`; equity avg `-0.0066` n `151`; fx avg `0.0014` n `6`; index avg `0.007` n `26`; metal avg `0.0243` n `20`; unknown avg `-0.0313` n `1191`
- 4h: commodity avg `0.1291` n `13`; crypto_alt avg `-0.1729` n `236`; crypto_major avg `-0.212` n `8`; equity avg `0.4211` n `151`; fx avg `0.0031` n `6`; index avg `0.0407` n `26`; metal avg `0.0067` n `20`; unknown avg `0.1038` n `1183`
- 24h: commodity avg `0.6793` n `13`; crypto_alt avg `-1.3945` n `236`; crypto_major avg `-1.1897` n `8`; equity avg `-4.0098` n `151`; fx avg `-0.0161` n `6`; index avg `-0.6421` n `26`; metal avg `-0.2257` n `20`; unknown avg `40.3409` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1713`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
