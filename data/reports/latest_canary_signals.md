# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T18:52:26.357617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.1725` n `239`; crypto_major avg `-0.0733` n `8`; equity avg `0.0252` n `166`; fx avg `-0.0054` n `6`; index avg `0.0218` n `27`; metal avg `0.0656` n `20`; unknown avg `159.4833` n `1260`
- 1h: commodity avg `0.0184` n `13`; crypto_alt avg `-0.0393` n `239`; crypto_major avg `0.1049` n `8`; equity avg `0.0931` n `166`; fx avg `0.0172` n `6`; index avg `0.0253` n `27`; metal avg `0.0804` n `20`; unknown avg `-0.0064` n `1218`
- 4h: commodity avg `0.0187` n `13`; crypto_alt avg `-0.3467` n `239`; crypto_major avg `-0.0627` n `8`; equity avg `0.1261` n `166`; fx avg `0.012` n `6`; index avg `0.0212` n `27`; metal avg `0.0821` n `20`; unknown avg `209.0597` n `1200`
- 24h: commodity avg `0.3109` n `13`; crypto_alt avg `0.6972` n `239`; crypto_major avg `1.8863` n `8`; equity avg `0.0792` n `166`; fx avg `-0.1017` n `6`; index avg `-0.0024` n `27`; metal avg `0.3042` n `20`; unknown avg `0.3615` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
