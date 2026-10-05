# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T17:52:32.175580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.1823` n `235`; crypto_major avg `0.1031` n `8`; equity avg `0.0875` n `144`; fx avg `-0.0074` n `6`; index avg `0.0094` n `26`; metal avg `0.0637` n `20`; unknown avg `0.1444` n `1079`
- 1h: commodity avg `-0.0606` n `13`; crypto_alt avg `0.1505` n `235`; crypto_major avg `0.1179` n `8`; equity avg `0.1185` n `144`; fx avg `0.0024` n `6`; index avg `0.0081` n `26`; metal avg `0.0214` n `20`; unknown avg `0.8389` n `1077`
- 4h: commodity avg `-0.0516` n `13`; crypto_alt avg `-0.7549` n `235`; crypto_major avg `-0.6836` n `8`; equity avg `0.5289` n `144`; fx avg `0.0095` n `6`; index avg `0.1271` n `26`; metal avg `-0.0155` n `20`; unknown avg `1.7656` n `989`
- 24h: commodity avg `-0.3502` n `13`; crypto_alt avg `0.1031` n `235`; crypto_major avg `0.0619` n `8`; equity avg `0.3885` n `144`; fx avg `-0.0932` n `6`; index avg `0.1243` n `26`; metal avg `0.1557` n `20`; unknown avg `0.3149` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
