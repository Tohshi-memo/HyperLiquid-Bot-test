# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T18:52:20.939467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0572` n `12`; crypto_alt avg `0.0562` n `228`; crypto_major avg `0.0337` n `8`; equity avg `-0.1408` n `66`; fx avg `-0.0027` n `6`; index avg `-0.1656` n `23`; metal avg `0.0493` n `18`; unknown avg `0.0208` n `383`
- 1h: commodity avg `0.5618` n `12`; crypto_alt avg `-0.0269` n `228`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0753` n `66`; fx avg `0.017` n `6`; index avg `-0.0457` n `23`; metal avg `-0.0944` n `18`; unknown avg `1.2262` n `383`
- 4h: commodity avg `0.5445` n `12`; crypto_alt avg `0.6634` n `228`; crypto_major avg `0.5996` n `8`; equity avg `1.9249` n `66`; fx avg `-0.0423` n `6`; index avg `0.9295` n `23`; metal avg `0.2086` n `18`; unknown avg `1.7834` n `383`
- 24h: commodity avg `0.6155` n `12`; crypto_alt avg `1.5298` n `228`; crypto_major avg `1.3208` n `8`; equity avg `1.538` n `66`; fx avg `0.0831` n `6`; index avg `0.1501` n `23`; metal avg `-1.6962` n `18`; unknown avg `1.6944` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
