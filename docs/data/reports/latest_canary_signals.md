# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T11:07:30.595764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `0.003` n `239`; crypto_major avg `-0.0548` n `8`; equity avg `-0.1131` n `162`; fx avg `0.0023` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0229` n `20`; unknown avg `1.9787` n `1257`
- 1h: commodity avg `-0.0386` n `13`; crypto_alt avg `0.0331` n `239`; crypto_major avg `-0.0182` n `8`; equity avg `-0.208` n `162`; fx avg `0.0035` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0027` n `20`; unknown avg `0.6299` n `1249`
- 4h: commodity avg `-0.1596` n `13`; crypto_alt avg `0.0672` n `239`; crypto_major avg `0.1759` n `8`; equity avg `0.1966` n `162`; fx avg `0.0246` n `6`; index avg `0.0336` n `27`; metal avg `-0.1385` n `20`; unknown avg `-0.0356` n `1233`
- 24h: commodity avg `-0.1201` n `13`; crypto_alt avg `-1.6489` n `239`; crypto_major avg `-0.9613` n `8`; equity avg `-0.949` n `162`; fx avg `-0.0855` n `6`; index avg `-0.0576` n `27`; metal avg `-0.8685` n `20`; unknown avg `1.046` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
