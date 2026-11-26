# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T05:52:31.372785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `13`; crypto_alt avg `0.0972` n `239`; crypto_major avg `-0.2743` n `8`; equity avg `-0.3187` n `168`; fx avg `-0.0035` n `6`; index avg `-0.0351` n `27`; metal avg `-0.2116` n `20`; unknown avg `158.3679` n `1267`
- 1h: commodity avg `-0.0459` n `13`; crypto_alt avg `0.0836` n `239`; crypto_major avg `-0.1285` n `8`; equity avg `-0.3841` n `168`; fx avg `0.0025` n `6`; index avg `-0.0302` n `27`; metal avg `-0.0859` n `20`; unknown avg `229.8803` n `1259`
- 4h: commodity avg `0.0926` n `13`; crypto_alt avg `0.0875` n `239`; crypto_major avg `0.1918` n `8`; equity avg `0.1312` n `168`; fx avg `-0.0096` n `6`; index avg `0.0205` n `27`; metal avg `0.3131` n `20`; unknown avg `2.2607` n `1243`
- 24h: commodity avg `0.7169` n `13`; crypto_alt avg `3.222` n `239`; crypto_major avg `3.0579` n `8`; equity avg `2.6614` n `168`; fx avg `0.0169` n `6`; index avg `0.2086` n `27`; metal avg `0.8359` n `20`; unknown avg `770.6095` n `1019`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
