# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T11:07:30.253472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.1022` n `239`; crypto_major avg `0.1058` n `8`; equity avg `0.262` n `162`; fx avg `0.0033` n `6`; index avg `0.0228` n `27`; metal avg `-0.0028` n `20`; unknown avg `47.5909` n `1256`
- 1h: commodity avg `0.1024` n `13`; crypto_alt avg `0.2688` n `239`; crypto_major avg `0.2684` n `8`; equity avg `0.3591` n `162`; fx avg `-0.0185` n `6`; index avg `0.0422` n `27`; metal avg `-0.0854` n `20`; unknown avg `250.1325` n `1206`
- 4h: commodity avg `0.0019` n `13`; crypto_alt avg `0.0244` n `239`; crypto_major avg `0.452` n `8`; equity avg `0.4528` n `162`; fx avg `-0.0295` n `6`; index avg `0.0563` n `27`; metal avg `-0.1539` n `20`; unknown avg `264.0888` n `1146`
- 24h: commodity avg `0.7863` n `13`; crypto_alt avg `-0.8514` n `239`; crypto_major avg `-2.6221` n `8`; equity avg `-0.7553` n `162`; fx avg `-0.0539` n `6`; index avg `0.0655` n `27`; metal avg `-0.4662` n `20`; unknown avg `234.7866` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
