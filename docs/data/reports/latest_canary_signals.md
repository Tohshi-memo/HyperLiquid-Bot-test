# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T01:22:36.574360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `13`; crypto_alt avg `-0.3032` n `234`; crypto_major avg `-0.3164` n `8`; equity avg `-0.0509` n `142`; fx avg `0.0014` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0318` n `20`; unknown avg `-0.002` n `985`
- 1h: commodity avg `-0.1183` n `13`; crypto_alt avg `-0.6792` n `234`; crypto_major avg `-0.4542` n `8`; equity avg `-0.2542` n `142`; fx avg `-0.0197` n `6`; index avg `-0.0515` n `26`; metal avg `-0.1999` n `20`; unknown avg `0.2509` n `983`
- 4h: commodity avg `-0.2267` n `13`; crypto_alt avg `-0.2004` n `234`; crypto_major avg `-0.15` n `8`; equity avg `0.0657` n `142`; fx avg `0.0208` n `6`; index avg `0.0047` n `26`; metal avg `-0.2359` n `20`; unknown avg `-0.2674` n `937`
- 24h: commodity avg `0.3283` n `13`; crypto_alt avg `-1.2154` n `234`; crypto_major avg `-0.5144` n `8`; equity avg `0.7946` n `142`; fx avg `-0.1864` n `6`; index avg `0.1042` n `26`; metal avg `-0.2686` n `20`; unknown avg `-0.0033` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
