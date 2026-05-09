# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T14:49:05.323087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0609` n `12`; crypto_alt avg `0.1236` n `228`; crypto_major avg `0.0863` n `8`; equity avg `0.0218` n `65`; fx avg `0.0021` n `5`; index avg `0.0025` n `23`; metal avg `-0.0209` n `18`; unknown avg `0.1601` n `376`
- 1h: commodity avg `0.2114` n `12`; crypto_alt avg `-0.316` n `228`; crypto_major avg `-0.2218` n `8`; equity avg `-0.0543` n `65`; fx avg `0.0196` n `5`; index avg `-0.0479` n `23`; metal avg `-0.0531` n `18`; unknown avg `0.1178` n `376`
- 4h: commodity avg `0.2991` n `12`; crypto_alt avg `-0.7933` n `228`; crypto_major avg `-0.3228` n `8`; equity avg `0.0232` n `65`; fx avg `-0.0017` n `5`; index avg `-0.0167` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.3787` n `376`
- 24h: commodity avg `-0.2024` n `12`; crypto_alt avg `1.5694` n `228`; crypto_major avg `1.2912` n `8`; equity avg `1.7415` n `65`; fx avg `0.0133` n `5`; index avg `0.6307` n `23`; metal avg `-0.2016` n `18`; unknown avg `0.3507` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
