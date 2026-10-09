# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T04:37:28.319520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `-0.0792` n `235`; crypto_major avg `-0.1296` n `8`; equity avg `0.0002` n `150`; fx avg `-0.0183` n `6`; index avg `0.0086` n `26`; metal avg `0.0087` n `20`; unknown avg `0.1933` n `1076`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `0.2084` n `235`; crypto_major avg `0.0573` n `8`; equity avg `0.1996` n `150`; fx avg `-0.0133` n `6`; index avg `0.0313` n `26`; metal avg `0.0538` n `20`; unknown avg `-0.064` n `1068`
- 4h: commodity avg `-0.2321` n `13`; crypto_alt avg `1.3822` n `235`; crypto_major avg `0.68` n `8`; equity avg `0.4611` n `150`; fx avg `-0.0227` n `6`; index avg `0.0723` n `26`; metal avg `0.3191` n `20`; unknown avg `1.3788` n `1068`
- 24h: commodity avg `0.0843` n `13`; crypto_alt avg `-1.1634` n `235`; crypto_major avg `-2.0066` n `8`; equity avg `-1.7202` n `150`; fx avg `0.097` n `6`; index avg `-0.1608` n `26`; metal avg `0.173` n `20`; unknown avg `5.9548` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
