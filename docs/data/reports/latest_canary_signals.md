# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T21:07:30.774687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.0128` n `230`; crypto_major avg `0.0275` n `8`; equity avg `-0.0871` n `94`; fx avg `0.0016` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.1669` n `768`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.1928` n `230`; crypto_major avg `0.2051` n `8`; equity avg `-0.063` n `94`; fx avg `-0.0099` n `6`; index avg `-0.0161` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0114` n `768`
- 4h: commodity avg `0.2119` n `12`; crypto_alt avg `0.1216` n `230`; crypto_major avg `-0.1109` n `8`; equity avg `0.5301` n `94`; fx avg `0.0094` n `6`; index avg `0.1667` n `25`; metal avg `0.4` n `20`; unknown avg `-0.2907` n `768`
- 24h: commodity avg `0.1736` n `12`; crypto_alt avg `0.5759` n `230`; crypto_major avg `0.69` n `8`; equity avg `-0.5818` n `93`; fx avg `0.2002` n `6`; index avg `-0.1461` n `25`; metal avg `0.1603` n `20`; unknown avg `0.1373` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
