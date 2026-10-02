# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T09:22:30.658167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `13`; crypto_alt avg `0.0724` n `234`; crypto_major avg `0.0649` n `8`; equity avg `0.0803` n `142`; fx avg `0.0014` n `6`; index avg `0.0164` n `26`; metal avg `0.0186` n `20`; unknown avg `-0.05` n `985`
- 1h: commodity avg `-0.1475` n `13`; crypto_alt avg `-0.1261` n `234`; crypto_major avg `-0.2539` n `8`; equity avg `0.0028` n `142`; fx avg `-0.015` n `6`; index avg `0.0066` n `26`; metal avg `-0.0636` n `20`; unknown avg `0.1166` n `983`
- 4h: commodity avg `-0.6317` n `13`; crypto_alt avg `0.4334` n `234`; crypto_major avg `0.2912` n `8`; equity avg `0.4695` n `142`; fx avg `-0.1057` n `6`; index avg `0.1064` n `26`; metal avg `-0.0535` n `20`; unknown avg `-0.181` n `891`
- 24h: commodity avg `-0.7112` n `13`; crypto_alt avg `1.5576` n `234`; crypto_major avg `2.0876` n `8`; equity avg `1.1847` n `142`; fx avg `-0.3305` n `6`; index avg `0.231` n `26`; metal avg `0.2241` n `20`; unknown avg `-0.0329` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
