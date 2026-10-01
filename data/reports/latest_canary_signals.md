# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T23:52:27.839258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `0.0817` n `234`; crypto_major avg `0.0469` n `8`; equity avg `-0.0013` n `142`; fx avg `0.0029` n `6`; index avg `0.0076` n `26`; metal avg `0.0351` n `20`; unknown avg `0.1666` n `985`
- 1h: commodity avg `-0.032` n `13`; crypto_alt avg `0.4289` n `234`; crypto_major avg `0.2611` n `8`; equity avg `0.0734` n `142`; fx avg `-0.0165` n `6`; index avg `0.0014` n `26`; metal avg `0.0703` n `20`; unknown avg `0.186` n `983`
- 4h: commodity avg `-0.0577` n `13`; crypto_alt avg `-0.2416` n `234`; crypto_major avg `-0.0401` n `8`; equity avg `0.0013` n `142`; fx avg `-0.0103` n `6`; index avg `-0.0284` n `26`; metal avg `0.0482` n `20`; unknown avg `-0.3658` n `891`
- 24h: commodity avg `0.1191` n `13`; crypto_alt avg `-0.5074` n `234`; crypto_major avg `-0.0977` n `8`; equity avg `0.9567` n `142`; fx avg `-0.1274` n `6`; index avg `0.1382` n `26`; metal avg `0.0546` n `20`; unknown avg `0.2964` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
