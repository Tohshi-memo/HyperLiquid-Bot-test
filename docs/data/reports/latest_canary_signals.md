# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T03:52:27.315968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0356` n `13`; crypto_alt avg `-0.0169` n `239`; crypto_major avg `-0.0381` n `8`; equity avg `0.0206` n `163`; fx avg `-0.0173` n `6`; index avg `0.0159` n `27`; metal avg `-0.0335` n `20`; unknown avg `10.238` n `1266`
- 1h: commodity avg `-0.066` n `13`; crypto_alt avg `0.5043` n `239`; crypto_major avg `0.4675` n `8`; equity avg `0.6114` n `163`; fx avg `0.0086` n `6`; index avg `0.1104` n `27`; metal avg `-0.0214` n `20`; unknown avg `3.3775` n `1264`
- 4h: commodity avg `-0.2927` n `13`; crypto_alt avg `-0.7288` n `239`; crypto_major avg `-0.6926` n `8`; equity avg `-1.3319` n `163`; fx avg `-0.0744` n `6`; index avg `-0.1421` n `27`; metal avg `-0.577` n `20`; unknown avg `5.3908` n `1258`
- 24h: commodity avg `0.212` n `13`; crypto_alt avg `-0.0118` n `239`; crypto_major avg `0.0706` n `8`; equity avg `-0.5549` n `163`; fx avg `-0.1068` n `6`; index avg `-0.061` n `27`; metal avg `-0.7463` n `20`; unknown avg `240.0312` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
