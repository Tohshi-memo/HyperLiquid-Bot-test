# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T04:52:26.824403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `0.1217` n `228`; crypto_major avg `0.2318` n `8`; equity avg `0.0483` n `88`; fx avg `-0.0029` n `6`; index avg `0.023` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.2796` n `763`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.095` n `228`; crypto_major avg `-0.2398` n `8`; equity avg `-0.2295` n `88`; fx avg `0.0004` n `6`; index avg `-0.0534` n `25`; metal avg `-0.132` n `20`; unknown avg `0.3006` n `763`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `1.4886` n `228`; crypto_major avg `1.5603` n `8`; equity avg `0.0959` n `88`; fx avg `-0.0195` n `6`; index avg `0.0889` n `25`; metal avg `0.2602` n `20`; unknown avg `-0.2726` n `759`
- 24h: commodity avg `-0.6224` n `12`; crypto_alt avg `1.313` n `228`; crypto_major avg `0.9484` n `8`; equity avg `-1.7724` n `88`; fx avg `0.0208` n `6`; index avg `-0.4507` n `25`; metal avg `1.0213` n `20`; unknown avg `24.7191` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
