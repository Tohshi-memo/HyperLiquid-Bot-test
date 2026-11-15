# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T22:22:24.610059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `13`; crypto_alt avg `0.0707` n `239`; crypto_major avg `0.0864` n `8`; equity avg `-0.016` n `162`; fx avg `0.0049` n `6`; index avg `-0.0007` n `27`; metal avg `0.0008` n `20`; unknown avg `0.2047` n `1251`
- 1h: commodity avg `-0.0732` n `13`; crypto_alt avg `0.5981` n `239`; crypto_major avg `0.5368` n `8`; equity avg `0.1202` n `162`; fx avg `-0.0166` n `6`; index avg `0.0064` n `27`; metal avg `0.0229` n `20`; unknown avg `-0.5754` n `1241`
- 4h: commodity avg `-0.0185` n `13`; crypto_alt avg `0.9192` n `239`; crypto_major avg `0.983` n `8`; equity avg `0.6327` n `162`; fx avg `0.0293` n `6`; index avg `0.0543` n `27`; metal avg `0.0692` n `20`; unknown avg `1.3353` n `1215`
- 24h: commodity avg `-0.0539` n `13`; crypto_alt avg `2.8861` n `239`; crypto_major avg `3.5694` n `8`; equity avg `1.1814` n `162`; fx avg `0.0244` n `6`; index avg `0.0923` n `27`; metal avg `0.2456` n `20`; unknown avg `1.5639` n `1140`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
