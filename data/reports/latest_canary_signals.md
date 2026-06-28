# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T16:07:32.795419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0526` n `12`; crypto_alt avg `-0.0203` n `228`; crypto_major avg `-0.0582` n `8`; equity avg `-0.0312` n `88`; fx avg `-0.005` n `6`; index avg `-0.0031` n `23`; metal avg `-0.0069` n `20`; unknown avg `-0.1305` n `764`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `-0.0735` n `8`; equity avg `-0.0449` n `88`; fx avg `0.0` n `6`; index avg `-0.0196` n `23`; metal avg `-0.0206` n `20`; unknown avg `-0.3528` n `764`
- 4h: commodity avg `0.0788` n `12`; crypto_alt avg `0.1566` n `228`; crypto_major avg `-0.205` n `8`; equity avg `0.0065` n `88`; fx avg `-0.0099` n `6`; index avg `-0.0053` n `23`; metal avg `-0.057` n `20`; unknown avg `1.3349` n `764`
- 24h: commodity avg `0.3487` n `12`; crypto_alt avg `-0.7687` n `228`; crypto_major avg `-1.6721` n `8`; equity avg `-0.0136` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0742` n `23`; metal avg `-0.0856` n `20`; unknown avg `15.3554` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
