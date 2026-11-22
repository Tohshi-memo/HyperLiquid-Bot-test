# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T06:22:25.870930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.1648` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `-0.071` n `239`; crypto_major avg `-0.167` n `8`; equity avg `-0.0212` n `166`; fx avg `-0.0065` n `6`; index avg `0.0043` n `27`; metal avg `-0.012` n `20`; unknown avg `158.6077` n `1263`
- 1h: commodity avg `0.0125` n `13`; crypto_alt avg `0.234` n `239`; crypto_major avg `0.1232` n `8`; equity avg `0.0879` n `166`; fx avg `-0.0011` n `6`; index avg `0.0126` n `27`; metal avg `0.022` n `20`; unknown avg `1.4445` n `1235`
- 4h: commodity avg `-0.0591` n `13`; crypto_alt avg `-0.5514` n `239`; crypto_major avg `-1.2256` n `8`; equity avg `-0.3411` n `166`; fx avg `-0.0008` n `6`; index avg `-0.0608` n `27`; metal avg `-0.0858` n `20`; unknown avg `3.2242` n `1227`
- 24h: commodity avg `-0.0095` n `13`; crypto_alt avg `3.3934` n `239`; crypto_major avg `4.7902` n `8`; equity avg `1.4768` n `166`; fx avg `-0.0218` n `6`; index avg `0.1769` n `27`; metal avg `0.1499` n `20`; unknown avg `422.5039` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
