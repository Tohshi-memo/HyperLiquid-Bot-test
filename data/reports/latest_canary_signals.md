# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T08:07:25.739722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `13`; crypto_alt avg `0.0315` n `238`; crypto_major avg `-0.0304` n `8`; equity avg `0.002` n `156`; fx avg `-0.0049` n `6`; index avg `-0.0027` n `27`; metal avg `0.0046` n `20`; unknown avg `202.0692` n `1238`
- 1h: commodity avg `-0.0327` n `13`; crypto_alt avg `-0.3075` n `238`; crypto_major avg `-0.1854` n `8`; equity avg `-0.0812` n `156`; fx avg `-0.0015` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0227` n `20`; unknown avg `202.6223` n `1238`
- 4h: commodity avg `-0.0631` n `13`; crypto_alt avg `-0.777` n `238`; crypto_major avg `-0.4634` n `8`; equity avg `-0.109` n `156`; fx avg `0.005` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.721` n `1210`
- 24h: commodity avg `-0.253` n `13`; crypto_alt avg `0.8448` n `238`; crypto_major avg `-0.8813` n `8`; equity avg `-1.9739` n `156`; fx avg `-0.0838` n `6`; index avg `-0.2291` n `27`; metal avg `-0.402` n `20`; unknown avg `4.7595` n `1030`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
