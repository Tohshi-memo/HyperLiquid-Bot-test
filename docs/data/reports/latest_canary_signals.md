# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T22:37:29.946114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `13`; crypto_alt avg `-0.046` n `234`; crypto_major avg `0.0196` n `8`; equity avg `0.0376` n `142`; fx avg `0.0077` n `6`; index avg `0.0081` n `26`; metal avg `0.0196` n `20`; unknown avg `0.0732` n `985`
- 1h: commodity avg `-0.0771` n `13`; crypto_alt avg `0.0886` n `234`; crypto_major avg `0.2993` n `8`; equity avg `0.0778` n `142`; fx avg `-0.0077` n `6`; index avg `0.0077` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.2607` n `943`
- 4h: commodity avg `0.0452` n `13`; crypto_alt avg `-0.7345` n `234`; crypto_major avg `-0.5093` n `8`; equity avg `0.0155` n `142`; fx avg `0.0207` n `6`; index avg `0.0084` n `26`; metal avg `0.0201` n `20`; unknown avg `-0.2885` n `891`
- 24h: commodity avg `0.1263` n `13`; crypto_alt avg `-0.8568` n `234`; crypto_major avg `-0.4334` n `8`; equity avg `0.9475` n `142`; fx avg `-0.1013` n `6`; index avg `0.1692` n `26`; metal avg `-0.0232` n `20`; unknown avg `-0.1343` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
