# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T18:08:33.627380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0907` n `12`; crypto_alt avg `-0.3882` n `228`; crypto_major avg `-0.1864` n `8`; equity avg `-0.2776` n `66`; fx avg `-0.0289` n `5`; index avg `-0.1567` n `23`; metal avg `-0.1229` n `18`; unknown avg `-0.1445` n `384`
- 1h: commodity avg `0.2205` n `12`; crypto_alt avg `-0.4113` n `228`; crypto_major avg `-0.222` n `8`; equity avg `-0.4187` n `66`; fx avg `-0.0418` n `5`; index avg `-0.2855` n `23`; metal avg `-0.2771` n `18`; unknown avg `-0.1458` n `384`
- 4h: commodity avg `1.2039` n `12`; crypto_alt avg `-0.7529` n `228`; crypto_major avg `-0.585` n `8`; equity avg `-1.6357` n `66`; fx avg `-0.0497` n `5`; index avg `-0.737` n `23`; metal avg `-0.1979` n `18`; unknown avg `-1.2049` n `384`
- 24h: commodity avg `1.2442` n `12`; crypto_alt avg `-2.5316` n `228`; crypto_major avg `-1.9649` n `8`; equity avg `-1.1319` n `66`; fx avg `-0.0161` n `5`; index avg `-0.6445` n `23`; metal avg `0.5145` n `18`; unknown avg `-0.5753` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
