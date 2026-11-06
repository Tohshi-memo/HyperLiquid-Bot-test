# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T23:22:31.879292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `-0.0071` n `239`; crypto_major avg `0.0246` n `8`; equity avg `-0.0136` n `158`; fx avg `-0.0016` n `6`; index avg `0.0014` n `27`; metal avg `-0.0024` n `20`; unknown avg `-0.1563` n `1259`
- 1h: commodity avg `0.0182` n `13`; crypto_alt avg `-0.2949` n `239`; crypto_major avg `-0.1913` n `8`; equity avg `-0.1087` n `158`; fx avg `0.0025` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0065` n `20`; unknown avg `-0.074` n `1239`
- 4h: commodity avg `-0.0286` n `13`; crypto_alt avg `-0.4685` n `239`; crypto_major avg `-0.0309` n `8`; equity avg `0.3105` n `158`; fx avg `0.0111` n `6`; index avg `-0.0133` n `27`; metal avg `0.021` n `20`; unknown avg `-0.3054` n `1165`
- 24h: commodity avg `0.0389` n `13`; crypto_alt avg `2.0736` n `239`; crypto_major avg `0.4617` n `8`; equity avg `3.3385` n `158`; fx avg `-0.0628` n `6`; index avg `0.4446` n `27`; metal avg `0.0619` n `20`; unknown avg `9.0086` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
