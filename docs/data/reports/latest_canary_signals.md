# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T19:07:35.923632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.1423` n `237`; crypto_major avg `-0.1775` n `8`; equity avg `0.0048` n `151`; fx avg `0.0032` n `6`; index avg `0.0056` n `26`; metal avg `-0.0341` n `20`; unknown avg `-0.3115` n `1194`
- 1h: commodity avg `-0.2785` n `13`; crypto_alt avg `-0.159` n `237`; crypto_major avg `-0.2866` n `8`; equity avg `0.0518` n `151`; fx avg `-0.0024` n `6`; index avg `0.0163` n `26`; metal avg `-0.0395` n `20`; unknown avg `-0.5239` n `1194`
- 4h: commodity avg `0.1109` n `13`; crypto_alt avg `-0.2522` n `237`; crypto_major avg `-0.4081` n `8`; equity avg `-0.6996` n `151`; fx avg `-0.0046` n `6`; index avg `-0.0789` n `26`; metal avg `0.0186` n `20`; unknown avg `2.4847` n `1188`
- 24h: commodity avg `-0.2898` n `13`; crypto_alt avg `1.4146` n `237`; crypto_major avg `1.2389` n `8`; equity avg `2.6956` n `151`; fx avg `-0.0369` n `6`; index avg `0.5616` n `26`; metal avg `0.0978` n `20`; unknown avg `3.3811` n `920`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
