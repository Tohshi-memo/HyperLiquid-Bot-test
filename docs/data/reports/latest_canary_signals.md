# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T00:07:13.676352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1592` n `12`; crypto_alt avg `0.1221` n `228`; crypto_major avg `0.1767` n `8`; equity avg `-0.0736` n `66`; fx avg `0.0406` n `6`; index avg `-0.0139` n `23`; metal avg `-0.0334` n `18`; unknown avg `0.0347` n `383`
- 1h: commodity avg `0.1536` n `12`; crypto_alt avg `0.0276` n `228`; crypto_major avg `0.0326` n `8`; equity avg `-0.2607` n `66`; fx avg `0.0735` n `6`; index avg `-0.1392` n `23`; metal avg `-0.0928` n `18`; unknown avg `0.1525` n `383`
- 4h: commodity avg `0.3337` n `12`; crypto_alt avg `0.8273` n `228`; crypto_major avg `0.5287` n `8`; equity avg `0.4218` n `66`; fx avg `0.0525` n `6`; index avg `0.146` n `23`; metal avg `0.6136` n `18`; unknown avg `-0.098` n `383`
- 24h: commodity avg `0.5782` n `12`; crypto_alt avg `1.613` n `228`; crypto_major avg `0.2175` n `8`; equity avg `0.2279` n `66`; fx avg `0.2054` n `6`; index avg `0.3357` n `23`; metal avg `1.2683` n `18`; unknown avg `0.5351` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
