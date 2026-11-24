# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T15:37:27.445405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1051` n `13`; crypto_alt avg `0.2019` n `239`; crypto_major avg `0.3967` n `8`; equity avg `0.1528` n `167`; fx avg `0.0102` n `6`; index avg `0.0067` n `27`; metal avg `-0.0808` n `20`; unknown avg `158.2208` n `1266`
- 1h: commodity avg `-0.183` n `13`; crypto_alt avg `-0.9057` n `239`; crypto_major avg `-0.7152` n `8`; equity avg `-0.9777` n `167`; fx avg `-0.0044` n `6`; index avg `-0.0398` n `27`; metal avg `-0.3753` n `20`; unknown avg `158.1662` n `1262`
- 4h: commodity avg `0.1771` n `13`; crypto_alt avg `-1.108` n `239`; crypto_major avg `-0.7312` n `8`; equity avg `-1.1928` n `166`; fx avg `0.0653` n `6`; index avg `-0.0679` n `27`; metal avg `-0.3315` n `20`; unknown avg `0.4353` n `1242`
- 24h: commodity avg `0.3933` n `13`; crypto_alt avg `-5.5555` n `239`; crypto_major avg `-6.1906` n `8`; equity avg `-5.421` n `166`; fx avg `0.1724` n `6`; index avg `-0.4215` n `27`; metal avg `-1.1917` n `20`; unknown avg `6.613` n `1134`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
