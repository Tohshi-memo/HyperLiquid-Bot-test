# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T05:22:25.339028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.0285` n `228`; crypto_major avg `-0.0143` n `8`; equity avg `-0.0149` n `74`; fx avg `0.004` n `6`; index avg `0.0956` n `23`; metal avg `-0.0013` n `18`; unknown avg `-0.2118` n `643`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.1654` n `228`; crypto_major avg `-0.2825` n `8`; equity avg `-0.1104` n `74`; fx avg `0.0264` n `6`; index avg `0.0164` n `23`; metal avg `0.0068` n `18`; unknown avg `-0.1507` n `635`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.34` n `228`; crypto_major avg `-0.6337` n `8`; equity avg `-0.2462` n `74`; fx avg `0.0342` n `6`; index avg `0.1738` n `23`; metal avg `-0.1002` n `18`; unknown avg `-0.3041` n `635`
- 24h: commodity avg `-0.6475` n `12`; crypto_alt avg `-0.0794` n `228`; crypto_major avg `-0.5821` n `8`; equity avg `-0.9547` n `74`; fx avg `0.0339` n `6`; index avg `0.5901` n `23`; metal avg `0.513` n `18`; unknown avg `40.4928` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
