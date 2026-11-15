# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T18:37:27.585973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `13`; crypto_alt avg `0.0397` n `239`; crypto_major avg `-0.1326` n `8`; equity avg `-0.002` n `162`; fx avg `0.008` n `6`; index avg `-0.0042` n `27`; metal avg `0.0018` n `20`; unknown avg `0.3853` n `1265`
- 1h: commodity avg `-0.0009` n `13`; crypto_alt avg `0.1764` n `239`; crypto_major avg `0.1898` n `8`; equity avg `-0.0461` n `162`; fx avg `0.0258` n `6`; index avg `-0.0002` n `27`; metal avg `0.0323` n `20`; unknown avg `0.6938` n `1263`
- 4h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.5754` n `239`; crypto_major avg `-0.543` n `8`; equity avg `0.0839` n `162`; fx avg `0.0353` n `6`; index avg `0.0135` n `27`; metal avg `0.0563` n `20`; unknown avg `1.1273` n `1256`
- 24h: commodity avg `0.039` n `13`; crypto_alt avg `-1.5164` n `239`; crypto_major avg `-1.0946` n `8`; equity avg `0.0224` n `162`; fx avg `0.0074` n `6`; index avg `0.023` n `27`; metal avg `-0.1046` n `20`; unknown avg `-0.0389` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
