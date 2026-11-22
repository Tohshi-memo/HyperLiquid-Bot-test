# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T19:22:30.607423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `13`; crypto_alt avg `-0.0119` n `239`; crypto_major avg `-0.087` n `8`; equity avg `-0.0544` n `166`; fx avg `-0.0039` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0033` n `20`; unknown avg `0.3301` n `1262`
- 1h: commodity avg `0.0082` n `13`; crypto_alt avg `0.2053` n `239`; crypto_major avg `-0.0453` n `8`; equity avg `-0.0807` n `166`; fx avg `-0.0037` n `6`; index avg `-0.0211` n `27`; metal avg `-0.0572` n `20`; unknown avg `158.5563` n `1260`
- 4h: commodity avg `-0.0233` n `13`; crypto_alt avg `-0.0545` n `239`; crypto_major avg `-0.0793` n `8`; equity avg `0.0383` n `166`; fx avg `0.0185` n `6`; index avg `-0.0045` n `27`; metal avg `-0.0244` n `20`; unknown avg `161.748` n `1231`
- 24h: commodity avg `-0.0946` n `13`; crypto_alt avg `0.7535` n `239`; crypto_major avg `0.5801` n `8`; equity avg `0.9133` n `166`; fx avg `-0.006` n `6`; index avg `0.15` n `27`; metal avg `-0.0327` n `20`; unknown avg `188.2162` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
