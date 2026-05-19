# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T20:07:22.193538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0575` n `12`; crypto_alt avg `0.1058` n `228`; crypto_major avg `-0.0112` n `8`; equity avg `-0.0309` n `66`; fx avg `-0.0009` n `6`; index avg `0.0619` n `23`; metal avg `-0.147` n `18`; unknown avg `0.3405` n `383`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1277` n `228`; crypto_major avg `-0.1078` n `8`; equity avg `-0.2243` n `66`; fx avg `0.0349` n `6`; index avg `-0.1214` n `23`; metal avg `-0.2525` n `18`; unknown avg `-0.0336` n `383`
- 4h: commodity avg `0.3714` n `12`; crypto_alt avg `0.3472` n `228`; crypto_major avg `0.2122` n `8`; equity avg `0.5806` n `66`; fx avg `0.019` n `6`; index avg `0.3947` n `23`; metal avg `-0.3819` n `18`; unknown avg `1.3283` n `383`
- 24h: commodity avg `1.3895` n `12`; crypto_alt avg `-0.1949` n `228`; crypto_major avg `-0.1343` n `8`; equity avg `0.1681` n `66`; fx avg `0.0833` n `6`; index avg `-0.4333` n `23`; metal avg `-2.6054` n `18`; unknown avg `0.9248` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
