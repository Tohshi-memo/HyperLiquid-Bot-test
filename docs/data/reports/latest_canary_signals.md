# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T18:46:07.514036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.0923` n `233`; crypto_major avg `-0.0998` n `8`; equity avg `0.009` n `134`; fx avg `-0.0085` n `6`; index avg `0.0057` n `26`; metal avg `-0.0273` n `20`; unknown avg `0.0418` n `797`
- 1h: commodity avg `0.0776` n `12`; crypto_alt avg `-0.0398` n `233`; crypto_major avg `-0.1905` n `8`; equity avg `-0.047` n `134`; fx avg `-0.0282` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0511` n `20`; unknown avg `14.5892` n `795`
- 4h: commodity avg `-0.1379` n `12`; crypto_alt avg `-0.4071` n `233`; crypto_major avg `-0.4316` n `8`; equity avg `-0.2656` n `134`; fx avg `0.011` n `6`; index avg `-0.0818` n `26`; metal avg `-0.1196` n `20`; unknown avg `10.3067` n `789`
- 24h: commodity avg `0.0445` n `12`; crypto_alt avg `0.0579` n `233`; crypto_major avg `0.1688` n `8`; equity avg `-0.2954` n `134`; fx avg `-0.0498` n `6`; index avg `-0.1656` n `26`; metal avg `0.5952` n `20`; unknown avg `8.2377` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
