# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T19:07:31.415432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.081` n `12`; crypto_alt avg `-0.5717` n `234`; crypto_major avg `-0.5467` n `8`; equity avg `-0.1581` n `141`; fx avg `0.006` n `6`; index avg `-0.026` n `26`; metal avg `-0.0584` n `20`; unknown avg `6.3514` n `959`
- 1h: commodity avg `0.1177` n `12`; crypto_alt avg `-0.6599` n `234`; crypto_major avg `-0.4096` n `8`; equity avg `-0.151` n `141`; fx avg `0.0009` n `6`; index avg `-0.0247` n `26`; metal avg `-0.0746` n `20`; unknown avg `6.6876` n `959`
- 4h: commodity avg `-0.4288` n `12`; crypto_alt avg `1.1873` n `234`; crypto_major avg `0.9681` n `8`; equity avg `0.6497` n `141`; fx avg `-0.0082` n `6`; index avg `0.1088` n `26`; metal avg `0.0721` n `20`; unknown avg `17.4428` n `952`
- 24h: commodity avg `-0.408` n `12`; crypto_alt avg `-3.6655` n `234`; crypto_major avg `-1.9463` n `8`; equity avg `-3.0806` n `141`; fx avg `0.0419` n `6`; index avg `-0.2853` n `26`; metal avg `-1.0315` n `20`; unknown avg `26.601` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
