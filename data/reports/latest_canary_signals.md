# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T18:37:34.459662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0915` n `13`; crypto_alt avg `0.0496` n `237`; crypto_major avg `0.0311` n `8`; equity avg `-0.1344` n `151`; fx avg `-0.0061` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0327` n `20`; unknown avg `0.2024` n `1196`
- 1h: commodity avg `-0.2379` n `13`; crypto_alt avg `-0.0991` n `237`; crypto_major avg `-0.0432` n `8`; equity avg `-0.3228` n `151`; fx avg `-0.009` n `6`; index avg `-0.0273` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.1776` n `1194`
- 4h: commodity avg `0.1305` n `13`; crypto_alt avg `0.2071` n `237`; crypto_major avg `-0.001` n `8`; equity avg `-0.5257` n `151`; fx avg `0.0008` n `6`; index avg `-0.0537` n `26`; metal avg `0.0383` n `20`; unknown avg `3.0781` n `1187`
- 24h: commodity avg `-0.2351` n `13`; crypto_alt avg `1.2714` n `237`; crypto_major avg `1.4182` n `8`; equity avg `2.5205` n `151`; fx avg `-0.0416` n `6`; index avg `0.5365` n `26`; metal avg `0.1109` n `20`; unknown avg `3.4293` n `918`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
