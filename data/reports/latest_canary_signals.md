# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T14:22:36.281458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `13`; crypto_alt avg `0.1013` n `239`; crypto_major avg `0.0451` n `8`; equity avg `0.137` n `162`; fx avg `-0.0007` n `6`; index avg `0.0095` n `27`; metal avg `-0.0593` n `20`; unknown avg `31.4147` n `1260`
- 1h: commodity avg `0.0633` n `13`; crypto_alt avg `0.8122` n `239`; crypto_major avg `0.458` n `8`; equity avg `0.3739` n `162`; fx avg `-0.0179` n `6`; index avg `0.0174` n `27`; metal avg `-0.1231` n `20`; unknown avg `163.9893` n `1260`
- 4h: commodity avg `0.109` n `13`; crypto_alt avg `1.1591` n `239`; crypto_major avg `0.7915` n `8`; equity avg `0.3566` n `162`; fx avg `-0.0007` n `6`; index avg `0.0146` n `27`; metal avg `-0.1084` n `20`; unknown avg `45.5929` n `1232`
- 24h: commodity avg `0.5743` n `13`; crypto_alt avg `2.1251` n `239`; crypto_major avg `0.4375` n `8`; equity avg `1.516` n `162`; fx avg `-0.039` n `6`; index avg `0.1607` n `27`; metal avg `-0.2588` n `20`; unknown avg `3.0262` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
