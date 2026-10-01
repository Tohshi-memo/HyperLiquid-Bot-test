# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T00:52:29.706096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.068` n `234`; crypto_major avg `0.0494` n `8`; equity avg `0.1548` n `142`; fx avg `0.0073` n `6`; index avg `0.0454` n `26`; metal avg `0.0195` n `20`; unknown avg `-0.0643` n `975`
- 1h: commodity avg `0.1109` n `12`; crypto_alt avg `0.0383` n `234`; crypto_major avg `-0.1177` n `8`; equity avg `-0.0843` n `142`; fx avg `0.1067` n `6`; index avg `-0.0106` n `26`; metal avg `-0.1364` n `20`; unknown avg `1.8971` n `943`
- 4h: commodity avg `0.0161` n `12`; crypto_alt avg `0.4545` n `234`; crypto_major avg `-0.036` n `8`; equity avg `0.084` n `142`; fx avg `0.1222` n `6`; index avg `0.0642` n `26`; metal avg `-0.1578` n `20`; unknown avg `0.5296` n `941`
- 24h: commodity avg `0.2389` n `12`; crypto_alt avg `1.0885` n `234`; crypto_major avg `0.9507` n `8`; equity avg `-0.2214` n `142`; fx avg `0.1372` n `6`; index avg `0.0202` n `26`; metal avg `-0.363` n `20`; unknown avg `776.7546` n `797`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
