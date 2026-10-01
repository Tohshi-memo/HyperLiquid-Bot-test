# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T03:52:33.934330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2781` n `13`; crypto_alt avg `0.2521` n `234`; crypto_major avg `0.1864` n `8`; equity avg `0.1288` n `142`; fx avg `-0.006` n `6`; index avg `0.0362` n `26`; metal avg `0.0593` n `20`; unknown avg `0.4176` n `974`
- 1h: commodity avg `-0.6358` n `13`; crypto_alt avg `0.847` n `234`; crypto_major avg `0.3502` n `8`; equity avg `0.2661` n `142`; fx avg `-0.0064` n `6`; index avg `0.0423` n `26`; metal avg `0.0945` n `20`; unknown avg `0.6964` n `972`
- 4h: commodity avg `-0.7071` n `13`; crypto_alt avg `0.9325` n `234`; crypto_major avg `0.1051` n `8`; equity avg `0.5509` n `142`; fx avg `0.0832` n `6`; index avg `0.1436` n `26`; metal avg `0.1033` n `20`; unknown avg `0.3648` n `942`
- 24h: commodity avg `-0.6608` n `13`; crypto_alt avg `1.9833` n `234`; crypto_major avg `1.1392` n `8`; equity avg `0.5372` n `142`; fx avg `0.2045` n `6`; index avg `0.1788` n `26`; metal avg `-0.015` n `20`; unknown avg `777.9957` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
