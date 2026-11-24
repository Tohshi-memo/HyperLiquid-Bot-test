# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T04:52:28.423138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1541` n `239`; crypto_major avg `-0.3142` n `8`; equity avg `-0.0166` n `166`; fx avg `-0.0036` n `6`; index avg `-0.004` n `27`; metal avg `0.0769` n `20`; unknown avg `158.2034` n `1264`
- 1h: commodity avg `-0.0423` n `13`; crypto_alt avg `0.7051` n `239`; crypto_major avg `0.4488` n `8`; equity avg `0.1032` n `166`; fx avg `0.0007` n `6`; index avg `0.012` n `27`; metal avg `0.0091` n `20`; unknown avg `1.5256` n `1246`
- 4h: commodity avg `-0.193` n `13`; crypto_alt avg `0.1549` n `239`; crypto_major avg `-0.3478` n `8`; equity avg `-0.5425` n `166`; fx avg `-0.0212` n `6`; index avg `0.0323` n `27`; metal avg `-0.4625` n `20`; unknown avg `161.4329` n `1244`
- 24h: commodity avg `-1.2742` n `13`; crypto_alt avg `0.7558` n `239`; crypto_major avg `0.3188` n `8`; equity avg `4.8061` n `166`; fx avg `-0.2706` n `6`; index avg `0.6477` n `27`; metal avg `0.03` n `20`; unknown avg `243.7226` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
