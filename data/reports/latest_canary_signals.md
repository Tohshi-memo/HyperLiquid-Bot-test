# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T23:52:13.514966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0497` n `12`; crypto_alt avg `-0.0862` n `228`; crypto_major avg `-0.1129` n `8`; equity avg `-0.0754` n `66`; fx avg `0.003` n `6`; index avg `0.0226` n `23`; metal avg `-0.0015` n `18`; unknown avg `-0.0327` n `383`
- 1h: commodity avg `-0.0823` n `12`; crypto_alt avg `0.2534` n `228`; crypto_major avg `0.2461` n `8`; equity avg `0.1621` n `66`; fx avg `-0.0047` n `6`; index avg `0.2031` n `23`; metal avg `0.2779` n `18`; unknown avg `-0.0098` n `383`
- 4h: commodity avg `-0.131` n `12`; crypto_alt avg `-0.0944` n `228`; crypto_major avg `-0.0961` n `8`; equity avg `0.0776` n `66`; fx avg `-0.0475` n `6`; index avg `0.1364` n `23`; metal avg `0.2152` n `18`; unknown avg `0.0646` n `383`
- 24h: commodity avg `1.0194` n `12`; crypto_alt avg `-1.0856` n `228`; crypto_major avg `-0.5767` n `8`; equity avg `-0.2157` n `66`; fx avg `0.0246` n `6`; index avg `-0.5169` n `23`; metal avg `-2.8759` n `18`; unknown avg `0.7658` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
