# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T20:37:33.792552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `13`; crypto_alt avg `0.1184` n `239`; crypto_major avg `0.0509` n `8`; equity avg `0.1131` n `166`; fx avg `0.0015` n `6`; index avg `0.0082` n `27`; metal avg `-0.0084` n `20`; unknown avg `0.0545` n `1246`
- 1h: commodity avg `0.0151` n `13`; crypto_alt avg `0.1878` n `239`; crypto_major avg `-0.0205` n `8`; equity avg `0.138` n `166`; fx avg `0.0074` n `6`; index avg `0.0047` n `27`; metal avg `-0.022` n `20`; unknown avg `140.7267` n `1240`
- 4h: commodity avg `0.0936` n `13`; crypto_alt avg `0.1542` n `239`; crypto_major avg `0.6096` n `8`; equity avg `0.2981` n `166`; fx avg `0.0285` n `6`; index avg `0.0676` n `27`; metal avg `0.0695` n `20`; unknown avg `0.1213` n `1188`
- 24h: commodity avg `0.0302` n `13`; crypto_alt avg `1.7438` n `239`; crypto_major avg `3.429` n `8`; equity avg `2.0364` n `166`; fx avg `-0.0679` n `6`; index avg `0.3187` n `27`; metal avg `0.3573` n `20`; unknown avg `0.6816` n `1074`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
